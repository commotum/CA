"""Rule catalog factories for next-state update laws.

This module defines rule-type primitives and named rule families for
cellular-automata style next-state generation. A rule is the update interface:
it receives already-gathered neighborhood component reads and returns the next
raw value for one update site.

The construction hierarchy mirrors `neighborhoods.py`:

- Rule-type primitives describe how one neighborhood component is summarized,
  such as exhaustive, totalistic, or gated totalistic channels.
- Output rules consume one or more summarized channels, either through a lookup
  family or through a formulaic callable.
- Named experiment families are built by composing the primitives rather than
  duplicating component logic.

This keeps spatial construction in neighborhoods/frontiers, value-space
construction in alphabets, and rollout mechanics in `generate.py`. `datasets.py`
chooses the alphabet, neighborhood, frontier, seed, boundary, shape, horizon,
and named rule family.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal


UpdateFn = Callable[..., Any]

Aggregate = Literal["sum", "count"]
DecodeMode = Literal["lsb_rule_bits"]
GateType = Literal[
    "any",
    "all",
    "majority",
    "atLeast",
    "atMost",
    "exactly",
    "min",
    "max",
    "clamp",
    "ceil",
    "floor",
]


@dataclass(frozen=True)
class RuleChannel:
    """One summarized input channel for a composed rule.

    `component` indexes the corresponding neighborhood component. `pipeline`
    records the rule-type transforms applied to that component in order, such
    as exhaustive, totalistic, then gate.
    """

    component: int
    pipeline: tuple[Mapping[str, Any], ...]
    name: str | None = None
    params: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class Rule:
    """Structured rule definition or instantiated update law.

    `family` and `params` preserve the catalog recipe. `rule_id` identifies one
    concrete member of the family when applicable. `fn` stores the tiny callable
    used by `generate.py` after instantiation.
    """

    family: str
    params: Mapping[str, Any] | None = None
    rule_id: int | None = None
    fn: UpdateFn | None = None
    channels: tuple[RuleChannel, ...] = ()
    metadata: Mapping[str, Any] | None = None


def _not_implemented() -> None:
    raise NotImplementedError("rules.py currently contains catalog specs only")


def instantiate(rule: Rule, rule_id: int) -> Rule:
    """Instantiate one concrete callable from a rule family and `rule_id`.

    `generate.py` should call this before rollout instead of decoding private
    rule-id semantics itself.
    """

    rule_id = int(rule_id)
    metadata = dict(rule.metadata or {})

    if "R" in metadata and not 0 <= rule_id < int(metadata["R"]):
        raise ValueError(
            f"rule_id {rule_id} is outside {rule.family!r} rule range 0..{int(metadata['R']) - 1}"
        )

    if rule.family == "ar2_modular_0d":
        params = dict(rule.params or {})
        grid_a, grid_b = params.get("coefficient_grid", (16, 16))
        a = rule_id // int(grid_b) + 1
        b = rule_id % int(grid_b)
        modulus = int(params["modulus"])
        constant = int(params.get("constant", 1))

        def fn(current: Any, previous: Any) -> Any:
            return (a * current + b * previous + constant) % modulus

        metadata.update({"a": a, "b": b})

        return Rule(
            family=rule.family,
            params=rule.params,
            rule_id=rule_id,
            fn=fn,
            channels=rule.channels,
            metadata=metadata,
        )

    return Rule(
        family=rule.family,
        params=rule.params,
        rule_id=rule_id,
        fn=rule.fn,
        channels=rule.channels,
        metadata=metadata,
    )


def validate(a: int, *S_i: int) -> dict[str, int]:
    """Return basic finite-rule counts from already-known channel sizes.

    Args:
        a: Output alphabet size. For binary cellular automata, `a = 2`.
        *S_i: State count for each rule-input channel. For Dyadaxes, the three
            compressed binary channels are `S_i = (2, 2, 2)`.

    Returns:
        A dict with `a`, `S`, and `R`, where `S = product(S_i)` is the number
        of input table entries and `R = a**S` is the number of possible rules.
    """

    S = 1
    for channel_state_count in S_i:
        S *= channel_state_count

    return {
        "a": a,
        "S": S,
        "R": a**S,
    }



# ---------------------------------------------------------------------------
# Phase 1 Rule-Type Primitives
# ---------------------------------------------------------------------------


def exhaustive(component: int = 0, alphabet_size: int | None = None) -> RuleChannel:
    """Represent one component by its full ordered local pattern.

    For a single binary self component, this reduces to the self value. For
    larger components, this is the ordinary exhaustive cellular-automata input
    representation over the component's deterministic read order.
    """

    params = {
        "rule_type": "exhaustive",
        "component": component,
        "alphabet_size": alphabet_size,
    }

    if alphabet_size is not None:
        params["state_count"] = alphabet_size

    return RuleChannel(
        component=component,
        pipeline=(params,),
        name="exhaustive",
        params=params,
    )


def totalistic(component: int = 0, aggregate: Aggregate = "sum") -> RuleChannel:
    """Represent one component by a permutation-invariant aggregate.

    `aggregate="sum"` handles numeric alphabets. For binary alphabets, sum is
    the active count, so `aggregate="count"` and `aggregate="sum"` are the same
    Phase 1 information when values are only `0` and `1`.
    """

    params = {
        "rule_type": "totalistic",
        "component": component,
        "aggregate": aggregate,
    }

    return RuleChannel(
        component=component,
        pipeline=(params,),
        name="totalistic",
        params=params,
    )


def gate(
    source: RuleChannel | Mapping[str, Any],
    type: GateType,
    value: int | float | None = None,
    min: int | float | None = None,
    max: int | float | None = None,
) -> RuleChannel:
    """Map a source aggregate to a smaller state, usually binary.

    Supported gate types are `any`, `all`, `majority`, `atLeast`, `atMost`,
    `exactly`, `min`, `max`, `clamp`, `ceil`, and `floor`. This is a primitive
    transform/factory, not a dataclass.
    """

    if isinstance(source, RuleChannel):
        component = source.component
        pipeline = source.pipeline
        source_params = dict(source.params or {})
    else:
        component = source["component"]
        pipeline = tuple(source.get("pipeline", ()))
        source_params = dict(source.get("params", {}))

    gate_params = {
        "rule_type": "gate",
        "type": type,
        "value": value,
        "min": min,
        "max": max,
        "state_count": 2,
    }
    params = dict(source_params)
    params.update(gate_params)

    return RuleChannel(
        component=component,
        pipeline=(*pipeline, gate_params),
        name="gate",
        params=params,
    )


def lookup(
    channels: Sequence[RuleChannel],
    alphabet_size: int,
    decode: DecodeMode = "lsb_rule_bits",
) -> Rule:
    """Build an exhaustive final lookup over compressed channel outputs.

    Dyadrads and Dyadaxes use this after compressing each neighborhood
    component to a binary channel, giving an eight-entry binary lookup for
    three channels.
    """

    channels = tuple(channels)
    params = {
        "alphabet_size": alphabet_size,
        "decode": decode,
    }
    metadata = dict(params)

    channel_state_counts = []
    for channel in channels:
        if channel.params is None or "state_count" not in channel.params:
            break
        channel_state_counts.append(channel.params["state_count"])

    if len(channel_state_counts) == len(channels):
        metadata.update(validate(alphabet_size, *channel_state_counts))

    return Rule(
        family="lookup",
        params=params,
        channels=channels,
        metadata=metadata,
    )


def compose(channels: Sequence[RuleChannel], output: Rule) -> Rule:
    """Compose channel pipelines with a final output rule.

    This is the rule-level counterpart to neighborhood composition: channels
    preserve component boundaries, and the final output rule consumes the
    compressed channel states.
    """

    return Rule(
        family=output.family,
        params=output.params,
        rule_id=output.rule_id,
        fn=output.fn,
        channels=tuple(channels),
        metadata=output.metadata,
    )


def formulaic(fn: UpdateFn | None = None, params: Mapping[str, Any] | None = None) -> Rule:
    """Build a direct callable rule family.

    Formulaic rules compute outputs from reads and parameters without a lookup
    table. The 0D AR2 modular recurrence is the Phase 1 use case.
    """

    return Rule(
        family="formulaic",
        params=dict(params or {}),
        fn=fn,
        metadata={"rule_type": "formulaic"},
    )


# ---------------------------------------------------------------------------
# Phase 1 Named Experiment Rule Families
# ---------------------------------------------------------------------------


def ar2_modular_0d(
    modulus: int = 97,
    coefficient_grid: tuple[int, int] = (16, 16),
    constant: int = 1,
) -> Rule:
    """Build the 0D second-order modular recurrence rule family.

    The intended `rule_id` decode is:

    ```text
    a = floor(rule_id / 16) + 1
    b = rule_id % 16
    next = (a*x[t] + b*x[t-1] + constant) % modulus
    ```
    """

    params = {
        "modulus": modulus,
        "coefficient_grid": coefficient_grid,
        "constant": constant,
    }
    metadata = dict(params)
    metadata["rule_type"] = "formulaic"
    metadata["R"] = coefficient_grid[0] * coefficient_grid[1]

    return Rule(
        family="ar2_modular_0d",
        params=params,
        metadata=metadata,
    )


def dyadrads_1d() -> Rule:
    """Build the 1D Dyadrads composed binary rule family.

    Component 0 is self/exhaustive, component 1 is radius-1 any-gated
    totalistic count, component 2 is radius-2 any-gated totalistic count, and
    the final output is a binary exhaustive lookup over the three channel
    outputs.
    """

    channels = (
        exhaustive(component=0, alphabet_size=2),
        gate(totalistic(component=1, aggregate="count"), type="any"),
        gate(totalistic(component=2, aggregate="count"), type="any"),
    )
    output = lookup(channels, alphabet_size=2)

    return Rule(
        family="dyadrads_1d",
        params={},
        channels=channels,
        metadata=output.metadata,
    )


def dyadaxes_2d() -> Rule:
    """Build the 2D Dyadaxes composed binary rule family.

    Component 0 is self/exhaustive, component 1 is cardinal-neighbor majority,
    component 2 is diagonal-neighbor majority, and the final output is a binary
    exhaustive lookup over the three channel outputs.
    """

    channels = (
        exhaustive(component=0, alphabet_size=2),
        gate(totalistic(component=1, aggregate="count"), type="majority"),
        gate(totalistic(component=2, aggregate="count"), type="majority"),
    )
    output = lookup(channels, alphabet_size=2)

    return Rule(
        family="dyadaxes_2d",
        params={},
        channels=channels,
        metadata=output.metadata,
    )


def dyadaxes_3d() -> Rule:
    """Build the 3D Dyadaxes composed binary rule family.

    Component 0 is self/exhaustive, component 1 is face-neighbor majority,
    component 2 is edge/corner at-least-10, and the final output is a binary
    exhaustive lookup over the three channel outputs.
    """

    channels = (
        exhaustive(component=0, alphabet_size=2),
        gate(totalistic(component=1, aggregate="count"), type="majority"),
        gate(totalistic(component=2, aggregate="count"), type="atLeast", value=10),
    )
    output = lookup(channels, alphabet_size=2)

    return Rule(
        family="dyadaxes_3d",
        params={},
        channels=channels,
        metadata=output.metadata,
    )


# ---------------------------------------------------------------------------
# Phase 2 General Rule Types
# ---------------------------------------------------------------------------


def isotropic(
    component: int = 0,
    symmetries: Sequence[Any] = (),
    input_order: str = "lex",
) -> RuleChannel:
    """Represent one component modulo a symmetry group.

    This collapses exhaustive ordered patterns into symmetry orbits. The
    symmetry machinery itself should stay explicit here rather than being
    hidden in neighborhood construction.
    """

    _not_implemented()


def histographic(component: int = 0, alphabet_size: int | None = None) -> RuleChannel:
    """Represent one component by a finite-value histogram.

    This is the Phase 2 histogram-totalistic channel for non-binary finite
    alphabets. It keeps counts per value instead of only a scalar sum.
    """

    _not_implemented()


def stochastic(
    source: Rule | RuleChannel | None = None,
    distribution: Any | None = None,
    params: Mapping[str, Any] | None = None,
) -> Rule:
    """Build a stochastic output rule.

    A stochastic rule returns or samples from a distribution over alphabet
    values. It may consume exhaustive, isotropic, totalistic, histographic, or
    formulaic sufficient statistics.
    """

    _not_implemented()


# ---------------------------------------------------------------------------
# Phase 3 Aliases and Convenience Builders
# ---------------------------------------------------------------------------


def any_gate(source: RuleChannel | Mapping[str, Any]) -> RuleChannel:
    """Alias for `gate(source, type="any")`."""

    _not_implemented()


def all_gate(source: RuleChannel | Mapping[str, Any]) -> RuleChannel:
    """Alias for `gate(source, type="all")`."""

    _not_implemented()


def majority_gate(source: RuleChannel | Mapping[str, Any]) -> RuleChannel:
    """Alias for `gate(source, type="majority")`."""

    _not_implemented()


def at_least_gate(
    source: RuleChannel | Mapping[str, Any],
    value: int | float,
) -> RuleChannel:
    """Alias for `gate(source, type="atLeast", value=value)`."""

    _not_implemented()


def at_most_gate(
    source: RuleChannel | Mapping[str, Any],
    value: int | float,
) -> RuleChannel:
    """Alias for `gate(source, type="atMost", value=value)`."""

    _not_implemented()


def exactly_gate(
    source: RuleChannel | Mapping[str, Any],
    value: int | float,
) -> RuleChannel:
    """Alias for `gate(source, type="exactly", value=value)`."""

    _not_implemented()


def min_gate(
    source: RuleChannel | Mapping[str, Any],
    value: int | float,
) -> RuleChannel:
    """Alias for `gate(source, type="min", value=value)`."""

    _not_implemented()


def max_gate(
    source: RuleChannel | Mapping[str, Any],
    value: int | float,
) -> RuleChannel:
    """Alias for `gate(source, type="max", value=value)`."""

    _not_implemented()


def clamp_gate(
    source: RuleChannel | Mapping[str, Any],
    min: int | float,
    max: int | float,
) -> RuleChannel:
    """Alias for `gate(source, type="clamp", min=min, max=max)`."""

    _not_implemented()


def ceil_gate(source: RuleChannel | Mapping[str, Any]) -> RuleChannel:
    """Alias for `gate(source, type="ceil")`."""

    _not_implemented()


def floor_gate(source: RuleChannel | Mapping[str, Any]) -> RuleChannel:
    """Alias for `gate(source, type="floor")`."""

    _not_implemented()


def binary_lookup(num_bits: int, decode: DecodeMode = "lsb_rule_bits") -> Rule:
    """Alias for a binary exhaustive lookup over `num_bits` channel outputs."""

    _not_implemented()


def modular_ar(
    order: int,
    modulus: int,
    coefficients: Sequence[int] | None = None,
    constant: int = 1,
    decode: str | None = None,
) -> Rule:
    """Alias family for modular autoregressive scalar recurrences."""

    _not_implemented()


def dyadaxes(
    rank: Literal[2, 3],
    primary_gate: Mapping[str, Any] | None = None,
    secondary_gate: Mapping[str, Any] | None = None,
) -> Rule:
    """Alias for rank-specific Dyadaxes rule families."""

    _not_implemented()
