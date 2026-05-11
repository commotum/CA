# ANKoS Batch Rollout Report

This report summarizes Stage 1 of the Phase 9 batching plan: ANKoS now exposes
a raw batched rollout primitive that PE can call for same-domain episode
generation.

## Status

Stage 1 is implemented and tested in `/home/jake/Developer/ankos`.

Public additions:

- `ca.rollout_batch(...)`
- `ca.RawBatch`

Verification run:

```bash
uv run pytest -q
```

Result:

```text
57 passed
```

Import check:

```bash
uv run python -c "import ca; print(ca.RawBatch.__name__); print(callable(ca.rollout_batch))"
```

Result:

```text
RawBatch
True
```

## Public API

```python
batch = ca.rollout_batch(
    dynamics=dynamics,
    rule_ids=rule_ids,
    seed_states=seed_states,
    steps=steps,
    return_coords=True,
)
```

Inputs:

- `dynamics`: one shared `ca.Dynamics`
- `rule_ids`: integer array-like with shape `(B,)`
- `seed_states`: already rendered raw seeds
- `steps`: shared positive integer horizon
- `return_coords`: whether to materialize shared canonical coordinates

Output:

```python
ca.RawBatch(
    domain: str,
    shape: tuple[int, ...],
    rule_ids: np.ndarray,
    steps: int,
    states: np.ndarray,
    coords: np.ndarray | None,
    metadata: Mapping[str, Any] | None,
)
```

State shape:

```text
(B, T, *spatial_shape)
```

Coordinate shape when requested:

```text
(T * cell_count, 4)
```

Coordinates are shared across rows because every row in one batch call shares
domain, shape, and steps. They do not include a batch coordinate.

## Seed Shapes

For `t+0d` AR2:

```text
seed_states: (B, 2)
states:      (B, T)
```

For spatial lookup families:

```text
seed_states: (B, *dynamics.shape)
states:      (B, T, *dynamics.shape)
```

Supported spatial families in this pass:

- `dyadrads_1d`
- `dyadaxes_2d`
- `dyadaxes_3d`

## Files Changed

- `src/ca/specs.py`
  - Added `RawBatch`.

- `src/ca/rollout.py`
  - Added `rollout_batch(...)`.
  - Added batched AR2 rollout.
  - Added batched spatial lookup rollout.
  - Reused existing rule-channel and `loci.gather` machinery.

- `src/ca/__init__.py`
  - Exported `RawBatch`.
  - Exported `rollout_batch`.

- `tests/test_rollout.py`
  - Added parity tests for `t+0d`, `t+1d`, `t+2d`, and `t+3d`.
  - Added `return_coords=False` coverage.
  - Added shape and batch-size mismatch coverage.

## Correctness Contract

The tests compare each batched row against repeated calls to:

```python
ca.rollout(
    dynamics=dynamics,
    rule_id=rule_id,
    seed_state=seed_state,
    steps=steps,
)
```

Parity is covered for:

- scalar AR2 recurrence, `t+0d`
- 1D Dyadrads, `t+1d`
- 2D Dyadaxes, `t+2d`
- 3D Dyadaxes, `t+3d`

For the supported Phase 1 families, PE can treat `rollout_batch` as equivalent
to looping over `rollout`, with batched output layout.

## Implementation Notes For PE

Batch calls should be homogeneous by rollout signature:

```text
domain + dynamics + shape + steps + layout-compatible policy
```

PE should group planned examples before calling ANKoS. A good Stage 2 shape is:

```text
plan examples
  -> group by rollout signature
  -> render seed_states with shape (B, ...)
  -> call ca.rollout_batch(...)
  -> restore row identity
  -> serialize/tokenize/collate in PE
```

`rule_ids` may vary within a batch. `seed_states` may vary within a batch. The
`Dynamics` object, shape, and step count must be shared.

Current `multi` row-mixed batches will not benefit unless PE regroups by domain
or changes scheduling to homogeneous physical batches. A mixed physical batch
with one row each from `t0d`, `t1d`, `t2d`, and `t3d` still becomes four
batch-size-one rollout calls.

## Boundary

ANKoS consumes already rendered seed states and returns raw NumPy-compatible
arrays. PE should continue to choose streams, rule pools, seed recipes, splits,
tokenization, masks, device placement, training, evaluation, and checkpoints.

No torch dependency or PE runtime concept was added to ANKoS.

## Error Behavior

The new API raises clear errors for:

- non-`Dynamics` input
- non-positive `steps`
- empty `rule_ids`
- non-integer `rule_ids`
- rule IDs outside a finite rule family's range
- AR2 seeds not shaped `(B, 2)`
- spatial seeds not shaped `(B, *dynamics.shape)`
- `rule_ids` batch size not matching `seed_states`
- unsupported domains or unsupported rule/frontier families

## Known Limitation

The batched spatial path supports current-time spatial neighborhoods, which
covers the Phase 1 spatial families listed above. Temporal-memory spatial
neighborhoods are rejected in the batched path until a future family needs
them.

The scalar AR2 temporal recurrence is supported separately and is vectorized
across rows.

## Minimal PE Example

```python
import numpy as np
import ca

dynamics = ca.Dynamics(
    domain="t+1d",
    shape=(123,),
    rule=ca.dyadrads_1d_rule(),
    neighborhoods=(ca.dyadrads_1d_neighborhood(),),
    frontier=ca.time_slice((123,)),
    boundary={"policy": "fixed", "value": 0},
)

rule_ids = np.array([0, 37, 255], dtype=np.int64)
seed_states = np.zeros((3, 123), dtype=np.int64)
seed_states[0, 61] = 1
seed_states[1, 30:35] = 1
seed_states[2, ::2] = 1

batch = ca.rollout_batch(
    dynamics=dynamics,
    rule_ids=rule_ids,
    seed_states=seed_states,
    steps=16,
)

assert batch.states.shape == (3, 16, 123)
assert batch.coords is not None
```

## Next PE Work

PE can now implement Stage 2:

- create planned-example records before realization;
- group by rollout signature;
- call `ca.rollout_batch(...)` per group;
- restore original row order after grouped realization;
- keep a looped `ca.rollout(...)` fallback only as a transition aid;
- compare grouped realization against ungrouped realization for fixed seeds.
