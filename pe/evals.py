"""Evaluation protocol catalog factories.

This module defines declarative evaluation protocols for prepared datasets. An
eval spec describes how a base dataset should be partitioned, extended, or
viewed during evaluation; it does not generate trajectories, sample manifests,
or write artifacts.

The construction hierarchy is intentionally shallow:

- `datasets.py` defines base dataset families and their available rule, seed,
  shape, and horizon information.
- `evals.py` defines named protocols such as held-out rules, held-out seeds,
  longer horizons, larger scales, boundary variants, and positional invariance
  checks.
- `prepare.py` or a manifest layer materializes those protocols into concrete
  train/eval splits and artifact paths.

Held-out evals reserve parts of the rule or seed set using the top-level split
policy. OOD evals request larger horizons, spatial scales, or boundary
policies. Invariance evals apply coordinate/position transforms to examples
while keeping the underlying seed and rule identities fixed.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal


EvalKind = Literal[
    "held-out-rule",
    "held-out-seed",
    "ood-horizon",
    "ood-scale",
    "ood-boundary",
    "invariance",
]


@dataclass(frozen=True)
class EvalSpec:
    """Declarative evaluation protocol.

    `id` is the stable config-facing name. `kind` records the protocol family.
    `params` stores only protocol parameters; concrete rule ids, seed ids,
    shapes, horizons, and manifest paths are resolved later by preparation.
    """

    id: str
    kind: EvalKind
    params: Mapping[str, Any]


def _base_params(
    rule_pool: str = "train",
    seed_stream: str = "eval",
    variants: Sequence[Mapping[str, Any]] | None = None,
    variant_policy: str = "cycle",
    **extra: Any,
) -> Mapping[str, Any]:
    """Build common manifest-layer policy for an eval protocol."""

    if variants is None:
        variants = ({"id": "base"},)

    return {
        "rule_pool": rule_pool,
        "seed_stream": seed_stream,
        "variant_policy": variant_policy,
        "variants": tuple(dict(variant) for variant in variants),
        **extra,
    }


def _multiplier_id(multiplier: float) -> str:
    return f"x{multiplier:g}"


# ---------------------------------------------------------------------------
# Phase 1 Evaluation Protocols
# ---------------------------------------------------------------------------


def held_out_rule() -> EvalSpec:
    """Reserve a portion of the rule set for evaluation.

    The manifest layer should use the top-level split policy and dataset rule
    metadata to choose which rule ids are train-visible and which are held out.
    """

    return EvalSpec(
        id="held-out-rule",
        kind="held-out-rule",
        params=_base_params(rule_pool="eval"),
    )


def held_out_seed() -> EvalSpec:
    """Reserve a portion of the seed set for evaluation.

    The manifest layer should use the top-level split policy and dataset seed
    pool to choose which seed ids are train-visible and which are held out.
    """

    return EvalSpec(
        id="held-out-seed",
        kind="held-out-seed",
        params=_base_params(rule_pool="train", seed_stream="eval"),
    )


def ood_horizon(multiplier: float = 2.0) -> EvalSpec:
    """Evaluate on longer rollouts or context windows than training.

    The manifest layer should derive the concrete horizon from the base
    `max_tokens` or dataset horizon convention.
    """

    if multiplier <= 1.0:
        raise ValueError(f"ood_horizon multiplier must be > 1, got {multiplier}")

    return EvalSpec(
        id="ood-horizon",
        kind="ood-horizon",
        params=_base_params(
            rule_pool="train",
            variants=(
                {
                    "id": _multiplier_id(multiplier),
                    "horizon_multiplier": float(multiplier),
                },
            ),
        ),
    )


def ood_scale(multiplier: float = 2.0) -> EvalSpec:
    """Evaluate on larger native shapes than training.

    The manifest layer should derive the concrete shape from the base dataset
    shape and this scale policy.
    """

    if multiplier <= 1.0:
        raise ValueError(f"ood_scale multiplier must be > 1, got {multiplier}")

    return EvalSpec(
        id="ood-scale",
        kind="ood-scale",
        params=_base_params(
            rule_pool="train",
            variants=(
                {
                    "id": _multiplier_id(multiplier),
                    "shape_multiplier": float(multiplier),
                },
            ),
        ),
    )


def ood_boundary() -> EvalSpec:
    """Evaluate boundary policies outside the fixed-zero training default.

    The base datasets stay fixed-zero. This eval asks the manifest layer to
    reuse matched rule/seed examples under fixed-one, periodic, and reflective
    boundary reads.
    """

    return EvalSpec(
        id="ood-boundary",
        kind="ood-boundary",
        params=_base_params(
            rule_pool="train",
            variants=(
                {
                    "id": "fixed-1",
                    "boundary": {"policy": "fixed", "value": 1},
                },
                {
                    "id": "periodic",
                    "boundary": {"policy": "periodic"},
                },
                {
                    "id": "reflective",
                    "boundary": {"policy": "reflective"},
                },
            ),
        ),
    )


def invariance(
    transforms: Sequence[str] = ("translate", "rotate"),
) -> EvalSpec:
    """Evaluate coordinate/position transforms of held-out examples.

    This protocol changes coordinates or coordinate frames while keeping the
    underlying seed identity and rule identity fixed.
    """

    transforms = tuple(str(transform) for transform in transforms)
    if not transforms:
        raise ValueError("invariance requires at least one transform")

    return EvalSpec(
        id="invariance",
        kind="invariance",
        params=_base_params(
            rule_pool="train",
            variants=tuple(
                {
                    "id": transform,
                    "transform": transform,
                }
                for transform in transforms
            ),
        ),
    )


# ---------------------------------------------------------------------------
# Phase 2 Helpers
# ---------------------------------------------------------------------------


def from_config(ids: Sequence[Any]) -> tuple[EvalSpec, ...]:
    """Build eval specs from config-facing ids.

    Config ids are expected to be the literal eval names, such as
    `held-out-rule`, `held-out-seed`, `ood-horizon`, `ood-scale`,
    `ood-boundary`, and `invariance`. Mapping entries may pass factory
    keyword arguments, for example `{"id": "ood-horizon", "multiplier": 3}`.
    """

    specs = []

    for item in ids:
        if isinstance(item, EvalSpec):
            specs.append(item)
            continue

        if isinstance(item, str):
            eval_id = item
            kwargs = {}
        elif isinstance(item, Mapping):
            eval_id = str(item["id"])
            kwargs = {key: value for key, value in item.items() if key != "id"}
        else:
            raise TypeError(
                f"eval config entries must be strings or mappings, got {item!r}"
            )

        try:
            factory = EVAL_FACTORIES[eval_id]
        except KeyError as exc:
            known = ", ".join(sorted(EVAL_FACTORIES))
            raise ValueError(f"unknown eval kind {eval_id!r}; known: {known}") from exc

        specs.append(factory(**kwargs))

    return tuple(specs)


EVAL_FACTORIES: Mapping[str, Callable[..., EvalSpec]] = {
    "held-out-rule": held_out_rule,
    "held-out-seed": held_out_seed,
    "ood-horizon": ood_horizon,
    "ood-scale": ood_scale,
    "ood-boundary": ood_boundary,
    "invariance": invariance,
}
