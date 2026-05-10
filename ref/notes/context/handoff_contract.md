# CA/PE Handoff Contract

This document defines the tight runtime boundary between `ankos` and `pe`.
It is subordinate to `context/REFACTOR_TARGET.md`.

## Boundary

```text
PE manifest / stream policy
  -> ca.WorldSpec + rule_id + seed_state + steps
  -> ca.rollout(...)
  -> ca.RawEpisode
  -> pe/components/tokenizer.py
  -> pe/components/batch.py
  -> torch tensors for model/PE/masks/losses
```

`ankos` owns raw CA mechanics and NumPy-compatible rollout arrays. `pe` owns
dataset policy, tokenization, masks, PE caches, model batches, and torch/device
movement.

## PE To `ankos`

PE passes only raw-world inputs into `ca`:

```text
world: ca.WorldSpec
rule_id: int
seed_state: np.ndarray-like
steps: int
rng: optional NumPy-compatible RNG or seed
return_coords: bool
```

`ca.WorldSpec` is the normalized form of the old dataset catalog facts:

```text
dataset_id: PE-side identity, not required by ca rollout
domain: t+0d | t+1d | t+2d | t+3d
shape: spatial shape only
alphabet: raw value space
neighborhood: source-relative read structure
frontier: Phase 1 full_next_slice
rule: rule family and rule count
seed: seed family/spec
boundary: none | fixed | periodic | reflective
```

PE keeps these out of `ca`:

```text
train/eval split
rule-pool policy
held-out-rule policy
seed-stream policy beyond derived rng
vocab ids
BOS/domain tokens
position ids
layout ids
attention masks
loss masks
PE mode/cache
torch device placement
checkpoint/eval policy
```

## `ankos` To PE

`ca.rollout()` returns a raw episode:

```text
RawEpisode
  domain: str
  shape: tuple[int, ...]
  rule_id: int
  steps: int
  states: np.ndarray-like
  coords: np.ndarray-like | None
  metadata: dict
```

Array shapes:

```text
unbatched states: (T, *spatial_shape)
batched states:   (B, T, *spatial_shape), if batch rollout is added
coords:           (T * cell_count, 4), integer, when materialized
```

`states` and `coords` are raw CA arrays. They contain no token ids, no model
targets, no masks, no PE layout ids, and no torch tensors as part of the
baseline public contract.

## PE Batch Boundary

`pe/components/batch.py` is the first torch-native boundary.

It should:

```text
load prepared manifest and stream specs
derive episode rng with ca.rng helpers
select rule ids from prepared PE rule pools
render seed states through ca
call ca.rollout()
send RawEpisode to components/tokenizer.py
convert NumPy-compatible arrays with torch.from_numpy(...)
collate token ids, targets, loss masks, coords, position ids, layout ids
build dense state-causal masks
move tensors to the target device
```

`pe/components/tokenizer.py` owns model representation:

```text
vocab expansion
raw value -> token id mapping
BOS/domain token insertion
canonical sequence construction
model-facing [t,x,y,z] coordinates
position sets and position ids
layout/domain ids
next-state targets
loss metadata
```

## Old Form Mapping

From old `data/components/datasets.py`:

```text
DatasetSpec.id        -> PE dataset_id / manifest identity
DatasetSpec.domain    -> ca.WorldSpec.domain
DatasetSpec.shape     -> ca.WorldSpec.shape
DatasetSpec.alphabet  -> ca.WorldSpec.alphabet
neighborhoods         -> ca.WorldSpec.neighborhood
frontier              -> ca.WorldSpec.frontier
rule                  -> ca.WorldSpec.rule
seeds                 -> ca.WorldSpec.seed or PE stream seed choices
boundary              -> ca.WorldSpec.boundary
params                -> PE manifest metadata, unless raw-world specific
```

From old `data/generate.py`:

```text
Episode.domain   -> RawEpisode.domain
Episode.shape    -> RawEpisode.shape
Episode.rule_id  -> RawEpisode.rule_id
Episode.steps    -> RawEpisode.steps
Episode.states   -> RawEpisode.states, NumPy-compatible
Episode.coords   -> RawEpisode.coords, integer array or None
Episode.metadata -> RawEpisode.metadata
```

## Phase 1 Constraint

`ca.rollout()` must enforce the executable frontier:

```python
if world.frontier.family != "full_next_slice":
    raise NotImplementedError(
        "ankos Phase 1 supports only full_next_slice rollout"
    )
```

Old `data/generate.py` accepted frontier-like inputs but ignored them. The new
contract must reject unsupported frontiers rather than silently running a full
synchronous update.
