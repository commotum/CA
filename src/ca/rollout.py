"""Pure next-state trajectory generation.

`generate.py` has one narrow responsibility: roll an already chosen initial
seed state forward under a resolved next-state update contract.

Inputs should be explicit and already resolved by callers such as
`data.batch.py`:

- dataset/domain metadata,
- native shape,
- initial seed state or seed history,
- instantiated rule or rule id plus rule family,
- neighborhoods and frontier/update schedule,
- boundary policy,
- number of raw states to produce.

Outputs should be raw native-dimensional trajectories, plus canonical
coordinates when useful for downstream serialization. Generation follows the
Wolfram dynamical-update convention: current state `t` determines next state
`t+1`.

This module should not choose train/eval splits, sample rule streams, sample
seed streams, tokenize, pad, create labels, build batches, write manifests, or
filter rules. Runtime sampling and rollout-based filtering belong to
`data.batch.py`; representation and target construction belong to
`data.tokenize.py`.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np

from . import boundary as boundary_lib
from . import loci, rules


@dataclass(frozen=True)
class Episode:
    """Raw generated episode before tokenization or batching."""

    dataset_id: str
    domain: str
    rule_id: int
    shape: tuple[int, ...]
    steps: int
    states: Any
    coords: Any | None = None
    metadata: Mapping[str, Any] | None = None


def _not_implemented() -> None:
    raise NotImplementedError("data.generate next-state scaffolding is not implemented yet")


# ---------------------------------------------------------------------------
# Phase 1 Public Surface
# ---------------------------------------------------------------------------


def generate_episode(
    dataset_spec: Any,
    initial_state: Any,
    rule_id: int,
    steps: int,
    boundary: Mapping[str, Any] | None = None,
) -> Episode:
    """Generate one deterministic raw episode from an already rendered seed state."""

    steps = int(steps)
    if steps < 2:
        raise ValueError(f"steps must be at least 2 for next-state targets, got {steps}")

    boundary = dict(getattr(dataset_spec, "boundary", {}) if boundary is None else boundary)
    rule = rules.instantiate(dataset_spec.rule, int(rule_id))
    states = rollout(
        initial_state=initial_state,
        rule=rule,
        neighborhoods=dataset_spec.neighborhoods,
        frontier=dataset_spec.frontier,
        boundary=boundary,
        steps=steps,
    )

    state_shape = tuple(int(size) for size in np.asarray(states).shape[1:])

    return Episode(
        dataset_id=dataset_spec.id,
        domain=dataset_spec.domain,
        rule_id=int(rule_id),
        shape=state_shape,
        steps=steps,
        states=states,
        coords=canonical_coords(state_shape, steps),
        metadata={"boundary": boundary},
    )


def rollout(
    initial_state: Any,
    rule: Any,
    neighborhoods: Sequence[Any],
    frontier: Any,
    boundary: Mapping[str, Any],
    steps: int,
) -> Any:
    """Roll native states forward without tokenization or batch construction."""

    _ensure_full_next_slice(frontier)

    if rule.family == "ar2_modular_0d":
        return _rollout_ar2(initial_state, rule, steps)

    if rule.family in {"dyadrads_1d", "dyadaxes_2d", "dyadaxes_3d"}:
        return _rollout_spatial_lookup(
            initial_state=initial_state,
            rule=rule,
            neighborhoods=neighborhoods,
            boundary=boundary,
            steps=steps,
        )

    raise NotImplementedError(f"unsupported phase-1 rule family {rule.family!r}")


def canonical_coords(shape: Sequence[int], steps: int) -> Any:
    """Return canonical `[t, x, y, z]` coordinates in time-major order."""

    space = loci.coordinate_space(tuple(int(size) for size in shape), steps=int(steps))
    return loci.coord_grid(space)


def apply_boundary_read(
    state: Any,
    coord: Sequence[int],
    boundary: Mapping[str, Any],
) -> Any:
    """Resolve one read coordinate according to the spatial boundary policy."""

    return boundary_lib.apply_boundary_read(state, coord, boundary)


def apply_rule(rule: Any, reads: Sequence[Any], rule_id: int) -> Any:
    """Apply one instantiated or decodable next-state rule to gathered reads."""

    instantiated = rules.instantiate(rule, rule_id) if getattr(rule, "rule_id", None) is None else rule

    if instantiated.family == "ar2_modular_0d":
        return instantiated.fn(reads[0], reads[1])

    if instantiated.family in {"dyadrads_1d", "dyadaxes_2d", "dyadaxes_3d"}:
        channel_bits = []
        for channel in instantiated.channels:
            component_reads = np.asarray(reads[channel.component])
            channel_bits.append(_channel_state(component_reads, channel))

        index = _lookup_index(channel_bits)
        return (int(instantiated.rule_id) >> int(index)) & 1

    raise NotImplementedError(f"unsupported phase-1 rule family {instantiated.family!r}")


def _rollout_ar2(initial_state: Any, rule: rules.Rule, steps: int) -> np.ndarray:
    """Roll a scalar AR2 episode.

    The seed pair is interpreted as hidden previous value and first serialized
    value: `(x[-1], x[0])`. Returned states start at `x[0]`, so every serialized
    source token has a rule-generated next-state target.
    """

    seed = np.asarray(initial_state, dtype=np.int64).reshape(-1)
    if seed.size != 2:
        raise ValueError(f"AR2 initial_state must contain 2 values, got {seed.size}")

    previous = int(seed[0])
    current = int(seed[1])
    states = np.empty((int(steps),), dtype=np.int64)
    states[0] = current

    for index in range(1, int(steps)):
        nxt = int(rule.fn(current, previous))
        states[index] = nxt
        previous, current = current, nxt

    return states


def _rollout_spatial_lookup(
    initial_state: Any,
    rule: rules.Rule,
    neighborhoods: Sequence[Any],
    boundary: Mapping[str, Any],
    steps: int,
) -> np.ndarray:
    state = np.asarray(initial_state, dtype=np.int64)
    if state.ndim < 1 or state.ndim > 3:
        raise ValueError(f"spatial state rank must be 1..3, got {state.ndim}")

    states = np.empty((int(steps), *state.shape), dtype=np.int64)
    states[0] = state

    for index in range(1, int(steps)):
        states[index] = _next_spatial_state(
            state=states[index - 1],
            rule=rule,
            neighborhoods=neighborhoods,
            boundary=boundary,
        )

    return states


def _next_spatial_state(
    state: np.ndarray,
    rule: rules.Rule,
    neighborhoods: Sequence[Any],
    boundary: Mapping[str, Any],
) -> np.ndarray:
    component_reads = [
        _read_component(state, selector, boundary)
        for neighborhood in neighborhoods
        for selector in neighborhood.components
    ]

    channel_bits = [
        _channel_state(component_reads[channel.component], channel)
        for channel in rule.channels
    ]
    index = _lookup_index(channel_bits)
    return np.bitwise_and(np.right_shift(int(rule.rule_id), index), 1).reshape(state.shape).astype(np.int64)


def _read_component(
    state: np.ndarray,
    selector: loci.Selector,
    boundary: Mapping[str, Any],
) -> np.ndarray:
    shape = tuple(int(size) for size in state.shape)
    space = loci.coordinate_space(shape, steps=1)
    current_coords = loci.absolute_universe(space, t=0)
    selection = loci.select(selector)
    offsets = selection.coords

    if offsets is None:
        offsets = selection.universe.reshape(-1, 4)[selection.mask.reshape(-1)]

    query_coords = current_coords[:, None, :] + offsets[None, :, :]
    boundary = {**dict(boundary), "coordinate_space": space}
    gathered = boundary_lib.gather(
        query_coords.reshape(-1, 4),
        np.expand_dims(state, axis=0),
        boundary,
    )
    return gathered.reshape(current_coords.shape[0], offsets.shape[0])


def _channel_state(reads: np.ndarray, channel: rules.RuleChannel) -> np.ndarray:
    values = np.asarray(reads)
    state: np.ndarray | None = None
    group_size = values.shape[-1]

    for step in channel.pipeline:
        rule_type = step["rule_type"]

        if rule_type == "exhaustive":
            if values.shape[-1] != 1:
                alphabet_size = int(step["alphabet_size"])
                weights = alphabet_size ** np.arange(
                    values.shape[-1],
                    dtype=np.int64,
                )
                state = (values.astype(np.int64) * weights).sum(axis=-1)
            else:
                state = values[..., 0].astype(np.int64)
            continue

        if rule_type == "totalistic":
            state = values.astype(np.int64).sum(axis=-1)
            continue

        if rule_type == "gate":
            if state is None:
                state = values.astype(np.int64).sum(axis=-1)
            state = _apply_gate(state, step, group_size)
            continue

        raise NotImplementedError(f"unsupported rule pipeline step {rule_type!r}")

    if state is None:
        raise ValueError("rule channel pipeline produced no state")

    return state.astype(np.int64)


def _apply_gate(values: np.ndarray, params: Mapping[str, Any], group_size: int) -> np.ndarray:
    gate_type = params["type"]

    if gate_type == "any":
        return values > 0
    if gate_type == "all":
        return values >= group_size
    if gate_type == "majority":
        return values > (group_size / 2)
    if gate_type == "atLeast":
        return values >= int(params["value"])
    if gate_type == "atMost":
        return values <= int(params["value"])
    if gate_type == "exactly":
        return values == int(params["value"])
    if gate_type == "min":
        return values >= int(params["value"])
    if gate_type == "max":
        return values <= int(params["value"])
    if gate_type == "clamp":
        low = int(params["min"])
        high = int(params["max"])
        return np.clip(values, low, high)
    if gate_type == "ceil":
        return np.ceil(values.astype(float)).astype(np.int64)
    if gate_type == "floor":
        return np.floor(values.astype(float)).astype(np.int64)

    raise NotImplementedError(f"unsupported gate type {gate_type!r}")


def _lookup_index(channel_bits: Sequence[Any]) -> np.ndarray:
    index = None

    for bit_index, bit_values in enumerate(channel_bits):
        bit_tensor = np.asarray(bit_values, dtype=np.int64)
        contribution = bit_tensor << bit_index
        index = contribution if index is None else index + contribution

    if index is None:
        raise ValueError("lookup rules require at least one channel")

    return index.astype(np.int64)


def _ensure_full_next_slice(frontier: Any) -> None:
    name = getattr(frontier, "name", None)
    family = getattr(frontier, "family", None)
    if name in {"time_slice", "full_next_slice"} or family == "full_next_slice":
        return
    raise NotImplementedError("ankos Phase 1 supports only full_next_slice rollout")
