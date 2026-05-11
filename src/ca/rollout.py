"""Pure CA next-state trajectory rollout.

This module evolves an already resolved CA setup forward under the Wolfram
dynamical-update convention: current state `t` determines next state `t+1`.

The public entry point accepts only the handoff contract inputs:

- `Dynamics`: reusable raw CA mechanics,
- `rule_id`: the concrete rule to instantiate,
- `seed_state`: an already rendered raw seed state,
- `steps`: the number of raw states to produce.

Outputs are raw native-dimensional trajectories plus optional canonical
`[t, x, y, z]` coordinates. This module does not choose train/eval splits,
sample streams, render seed specs, serialize representations, pad, create
labels, build batches, write manifests, or manage device policy.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np

from . import loci, rules
from .specs import Dynamics, RawBatch, RawEpisode


# ---------------------------------------------------------------------------
# Phase 1 Public Surface
# ---------------------------------------------------------------------------


def rollout(
    dynamics: Dynamics,
    rule_id: int,
    seed_state: Any,
    steps: int,
    *,
    return_coords: bool = True,
) -> RawEpisode:
    """Roll CA dynamics forward and return a raw episode."""

    if not isinstance(dynamics, Dynamics):
        raise TypeError("rollout requires a ca.Dynamics instance")

    steps = int(steps)
    if steps <= 0:
        raise ValueError(f"steps must be positive, got {steps}")

    _validate_domain_shape(dynamics.domain, tuple(dynamics.shape))

    rule = rules.instantiate(dynamics.rule, int(rule_id))
    states = _rollout_states(
        seed_state=seed_state,
        rule=rule,
        neighborhoods=dynamics.neighborhoods,
        frontier=dynamics.frontier,
        boundary=dynamics.boundary,
        steps=steps,
    )

    shape = tuple(int(size) for size in np.asarray(states).shape[1:])
    if shape != tuple(dynamics.shape):
        raise ValueError(
            f"seed_state produced spatial shape {shape}, but dynamics.shape is {tuple(dynamics.shape)}"
        )

    coords = canonical_coords(dynamics.domain, shape, steps) if return_coords else None

    return RawEpisode(
        domain=dynamics.domain,
        shape=shape,
        rule_id=int(rule_id),
        steps=steps,
        states=np.asarray(states),
        coords=coords,
        metadata={
            "boundary": dict(dynamics.boundary),
            **dict(dynamics.metadata or {}),
        },
    )


def rollout_batch(
    dynamics: Dynamics,
    rule_ids: Any,
    seed_states: Any,
    steps: int,
    *,
    return_coords: bool = True,
) -> RawBatch:
    """Roll same-dynamics CA episodes forward and return a raw batch."""

    if not isinstance(dynamics, Dynamics):
        raise TypeError("rollout_batch requires a ca.Dynamics instance")

    steps = int(steps)
    if steps <= 0:
        raise ValueError(f"steps must be positive, got {steps}")

    shape = tuple(dynamics.shape)
    _validate_domain_shape(dynamics.domain, shape)

    rule_id_array = _normalize_rule_ids(rule_ids)
    if rule_id_array.size == 0:
        raise ValueError("rollout_batch requires at least one rule_id")

    rule = rules.instantiate(dynamics.rule, int(rule_id_array[0]))
    _validate_rule_ids(dynamics.rule, rule_id_array)

    states = _rollout_batch_states(
        seed_states=seed_states,
        rule=rule,
        rule_ids=rule_id_array,
        neighborhoods=dynamics.neighborhoods,
        frontier=dynamics.frontier,
        boundary=dynamics.boundary,
        steps=steps,
        expected_shape=shape,
    )

    batch_shape = tuple(int(size) for size in np.asarray(states).shape[2:])
    if batch_shape != shape:
        raise ValueError(
            f"seed_states produced spatial shape {batch_shape}, but dynamics.shape is {shape}"
        )

    coords = canonical_coords(dynamics.domain, shape, steps) if return_coords else None

    return RawBatch(
        domain=dynamics.domain,
        shape=shape,
        rule_ids=rule_id_array.copy(),
        steps=steps,
        states=np.asarray(states),
        coords=coords,
        metadata={
            "boundary": dict(dynamics.boundary),
            **dict(dynamics.metadata or {}),
        },
    )


def _rollout_states(
    seed_state: Any,
    rule: Any,
    neighborhoods: Sequence[Any],
    frontier: Any,
    boundary: Mapping[str, Any],
    steps: int,
) -> np.ndarray:
    """Roll native states forward without representation or batch construction."""

    _ensure_time_slice(frontier)

    if rule.family == "ar2_modular_0d":
        return _rollout_ar2(seed_state, rule, steps)

    if rule.family in {"dyadrads_1d", "dyadaxes_2d", "dyadaxes_3d"}:
        return _rollout_spatial_lookup(
            initial_state=seed_state,
            rule=rule,
            neighborhoods=neighborhoods,
            boundary=boundary,
            steps=steps,
        )

    raise ValueError(f"unsupported rule family {rule.family!r}")


def _rollout_batch_states(
    seed_states: Any,
    rule: Any,
    rule_ids: np.ndarray,
    neighborhoods: Sequence[Any],
    frontier: Any,
    boundary: Mapping[str, Any],
    steps: int,
    expected_shape: tuple[int, ...],
) -> np.ndarray:
    """Roll a same-dynamics batch without downstream representation work."""

    _ensure_time_slice(frontier)

    if rule.family == "ar2_modular_0d":
        return _rollout_ar2_batch(seed_states, rule, rule_ids, steps)

    if rule.family in {"dyadrads_1d", "dyadaxes_2d", "dyadaxes_3d"}:
        return _rollout_spatial_lookup_batch(
            initial_states=seed_states,
            rule=rule,
            rule_ids=rule_ids,
            neighborhoods=neighborhoods,
            boundary=boundary,
            steps=steps,
            expected_shape=expected_shape,
        )

    raise ValueError(f"unsupported rule family {rule.family!r}")


def canonical_coords(
    domain_or_shape: str | Sequence[int],
    shape_or_steps: Sequence[int] | int,
    steps: int | None = None,
) -> np.ndarray:
    """Return flattened canonical `[t, x, y, z]` coordinates in time-major order."""

    if steps is None:
        domain = None
        shape = domain_or_shape
        steps = int(shape_or_steps)  # type: ignore[arg-type]
    else:
        domain = str(domain_or_shape).lower()
        shape = shape_or_steps

    shape_tuple = tuple(int(size) for size in shape)  # type: ignore[arg-type]
    if domain is not None:
        _validate_domain_shape(domain, shape_tuple)

    space = loci.coordinate_space(shape_tuple, steps=int(steps))
    return loci.coord_grid(space).reshape(-1, 4)


def _validate_domain_shape(domain: str, shape: tuple[int, ...]) -> None:
    ranks = {
        "t+0d": 0,
        "t+1d": 1,
        "t+2d": 2,
        "t+3d": 3,
    }
    expected_rank = ranks.get(str(domain).lower())
    if expected_rank is None:
        raise ValueError(f"unsupported CA domain {domain!r}")
    if len(shape) != expected_rank:
        raise ValueError(
            f"domain {domain!r} requires spatial rank {expected_rank}, got shape {shape}"
        )


def _normalize_rule_ids(rule_ids: Any) -> np.ndarray:
    raw = np.asarray(rule_ids)
    if raw.ndim == 0:
        raw = raw.reshape(1)
    else:
        raw = raw.reshape(-1)

    if not np.issubdtype(raw.dtype, np.integer):
        raise TypeError("rule_ids must be an integer array")

    return raw.astype(np.int64, copy=False)


def _validate_rule_ids(rule: rules.Rule, rule_ids: np.ndarray) -> None:
    metadata = dict(rule.metadata or {})
    if "R" not in metadata:
        for rule_id in rule_ids.tolist():
            rules.instantiate(rule, int(rule_id))
        return

    rule_count = int(metadata["R"])
    bad = rule_ids[(rule_ids < 0) | (rule_ids >= rule_count)]
    if bad.size:
        raise ValueError(
            f"rule_ids must be in range 0..{rule_count - 1}; got {bad.astype(int).tolist()}"
        )


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

    raise ValueError(f"unsupported rule family {instantiated.family!r}")


def _rollout_ar2(initial_state: Any, rule: rules.Rule, steps: int) -> np.ndarray:
    """Roll a scalar AR2 episode.

    The seed pair is interpreted as hidden previous value and first serialized
    value: `(x[-1], x[0])`. Returned states start at `x[0]`, so every serialized
    source value has a rule-generated next-state target.
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


def _rollout_ar2_batch(
    initial_states: Any,
    rule: rules.Rule,
    rule_ids: np.ndarray,
    steps: int,
) -> np.ndarray:
    seeds = np.asarray(initial_states, dtype=np.int64)
    if seeds.ndim != 2 or seeds.shape[1] != 2:
        raise ValueError(f"AR2 seed_states must have shape (B, 2), got {tuple(seeds.shape)}")
    if seeds.shape[0] != rule_ids.size:
        raise ValueError(
            f"rule_ids has batch size {rule_ids.size}, but seed_states has batch size {seeds.shape[0]}"
        )

    params = dict(rule.params or {})
    _, grid_b = params.get("coefficient_grid", (16, 16))
    a = rule_ids // int(grid_b) + 1
    b = rule_ids % int(grid_b)
    modulus = int(params["modulus"])
    constant = int(params.get("constant", 1))

    previous = seeds[:, 0].copy()
    current = seeds[:, 1].copy()
    states = np.empty((rule_ids.size, int(steps)), dtype=np.int64)
    states[:, 0] = current

    for index in range(1, int(steps)):
        nxt = (a * current + b * previous + constant) % modulus
        states[:, index] = nxt
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


def _rollout_spatial_lookup_batch(
    initial_states: Any,
    rule: rules.Rule,
    rule_ids: np.ndarray,
    neighborhoods: Sequence[Any],
    boundary: Mapping[str, Any],
    steps: int,
    expected_shape: tuple[int, ...],
) -> np.ndarray:
    state_batch = np.asarray(initial_states, dtype=np.int64)
    if state_batch.ndim != len(expected_shape) + 1:
        raise ValueError(
            "spatial seed_states must have shape "
            f"(B, *dynamics.shape); got {tuple(state_batch.shape)}"
        )
    if tuple(state_batch.shape[1:]) != expected_shape:
        raise ValueError(
            f"seed_states spatial shape {tuple(state_batch.shape[1:])} does not match "
            f"dynamics.shape {expected_shape}"
        )
    if state_batch.shape[0] != rule_ids.size:
        raise ValueError(
            f"rule_ids has batch size {rule_ids.size}, but seed_states has batch size {state_batch.shape[0]}"
        )
    if len(expected_shape) < 1 or len(expected_shape) > 3:
        raise ValueError(f"spatial state rank must be 1..3, got {len(expected_shape)}")

    states = np.empty((rule_ids.size, int(steps), *expected_shape), dtype=np.int64)
    states[:, 0] = state_batch

    for index in range(1, int(steps)):
        states[:, index] = _next_spatial_state_batch(
            state_batch=states[:, index - 1],
            rule=rule,
            rule_ids=rule_ids,
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


def _next_spatial_state_batch(
    state_batch: np.ndarray,
    rule: rules.Rule,
    rule_ids: np.ndarray,
    neighborhoods: Sequence[Any],
    boundary: Mapping[str, Any],
) -> np.ndarray:
    component_reads = [
        _read_component_batch(state_batch, selector, boundary)
        for neighborhood in neighborhoods
        for selector in neighborhood.components
    ]

    channel_bits = [
        _channel_state(component_reads[channel.component], channel)
        for channel in rule.channels
    ]
    index = _lookup_index(channel_bits)
    shifted = np.right_shift(rule_ids[:, None], index)
    return np.bitwise_and(shifted, 1).reshape(state_batch.shape).astype(np.int64)


def _read_component(
    state: np.ndarray,
    selector: loci.Selector,
    boundary: Mapping[str, Any],
) -> np.ndarray:
    shape = tuple(int(size) for size in state.shape)
    space = loci.coordinate_space(shape, steps=1)
    current_coords = loci.absolute_universe(space, t=0)
    offsets = _selector_offsets(selector)

    query_coords = current_coords[:, None, :] + offsets[None, :, :]
    boundary = {**dict(boundary), "coordinate_space": space}
    gathered = loci.gather(
        query_coords.reshape(-1, 4),
        np.expand_dims(state, axis=0),
        boundary,
    )
    return gathered.reshape(current_coords.shape[0], offsets.shape[0])


def _read_component_batch(
    state_batch: np.ndarray,
    selector: loci.Selector,
    boundary: Mapping[str, Any],
) -> np.ndarray:
    shape = tuple(int(size) for size in state_batch.shape[1:])
    batch_size = int(state_batch.shape[0])
    space = loci.coordinate_space(shape, steps=1)
    current_coords = loci.absolute_universe(space, t=0)
    offsets = _selector_offsets(selector)

    if np.any(offsets[:, 0] != 0):
        raise ValueError("batched spatial lookup supports current-time neighborhoods only")

    query_coords = current_coords[:, None, :] + offsets[None, :, :]
    batched_query_coords = np.broadcast_to(
        query_coords,
        (batch_size, *query_coords.shape),
    ).copy()
    batched_query_coords[..., 0] = np.arange(batch_size, dtype=np.int64)[:, None, None]

    batch_space = loci.coordinate_space(shape, steps=batch_size)
    boundary = {**dict(boundary), "coordinate_space": batch_space}
    gathered = loci.gather(batched_query_coords, state_batch, boundary)
    return gathered.reshape(batch_size, current_coords.shape[0], offsets.shape[0])


def _selector_offsets(selector: loci.Selector) -> np.ndarray:
    selection = loci.select(selector)
    offsets = selection.coords

    if offsets is None:
        offsets = selection.universe.reshape(-1, 4)[selection.mask.reshape(-1)]

    return np.asarray(offsets, dtype=np.int64).reshape(-1, 4)


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

        raise ValueError(f"unsupported rule pipeline step {rule_type!r}")

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

    raise ValueError(f"unsupported gate type {gate_type!r}")


def _lookup_index(channel_bits: Sequence[Any]) -> np.ndarray:
    index = None

    for bit_index, bit_values in enumerate(channel_bits):
        bit_tensor = np.asarray(bit_values, dtype=np.int64)
        contribution = bit_tensor << bit_index
        index = contribution if index is None else index + contribution

    if index is None:
        raise ValueError("lookup rules require at least one channel")

    return index.astype(np.int64)


def _ensure_time_slice(frontier: Any) -> None:
    family = getattr(frontier, "family", None)
    if isinstance(frontier, Mapping):
        family = frontier.get("family", family)
    if family == "time_slice":
        return
    raise ValueError(f"unsupported frontier family {family!r}")
