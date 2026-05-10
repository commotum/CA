# Experiment Architecture

This document defines the positional-encoding experiment architecture. It is
the target contract for Phase 1 using the normalized repo layout in
`context/REFACTOR_TARGET.md`.

The central rule is:

```text
Sequence order is serialization.
Position identity is explicit.
Positional encoding is cached from explicit positions.
```

A token's position should never be implicit merely because it appears at index
`i` in a serialized tensor. Even standard RoPE should receive a position derived
from the dataset's canonical coordinates. For ordinary training data, that
derived scalar position may match row-major sequence order. For transformed or
OOD coordinates, it may not.

## Core Objects

Each experiment has four separable model-facing objects. Raw cellular-automata
mechanics live below these objects in the `ankos` package, imported as `ca`.

### 1. Domain/Dataset

The domain defines the native state shape and its canonical 4D coordinate
system:

```text
t+0D: scalar sequence
t+1D: [t, x, 0, 0]
t+2D: [t, x, y, 0]
t+3D: [t, x, y, z]
```

Spatial axes use centered coordinates. For the base Phase 1 datasets:

```text
t+1D: x in [-61, 61]
t+2D: x,y in [-5, 5]
t+3D: x,y,z in [-2, 2]
```

Model-facing serialized state tokens shift real states to `t >= 1`, reserving
`[0, 0, 0, 0]` for BOS/domain tokens.

Prepared PE datasets live under:

```text
data/0d-ar2-97
data/1d-dyadrads
data/2d-dyadaxes
data/3d-dyadaxes
```

Each dataset branch has a `manifest/` directory plus a dataset-local
`prepare.py`. The reusable CA dynamics, seed, rule, boundary, and rollout
mechanics live in `ankos/src/ca`.

### 2. Positional Encoder

Each trained model has exactly one positional encoding method.

Examples:

```text
rope
2d-axial
3d-axial
4d-axial
monster
```

An experiment may compare several trained models, but each individual model has
one PE method and one corresponding cache layout.

### 3. Canonical Sequence

The canonical sequence is the deterministic serialization order for one
domain. It maps native positions to token positions.

The default order is time-major:

```text
state t=0, row-major native order
state t=1, row-major native order
...
```

Within a state:

```text
t+1D: increasing x
t+2D: y outer, x inner
t+3D: z outer, y middle, x inner
```

The sequence is owned by the data representation layer, not the PE math layer.
`components/tokenizer.py` should own canonical sequence construction,
model-facing coordinates, position ids, and value-to-token serialization.
`components/batch.py` should pad/collate those fields and select the
domain/cache key for each episode.

### 4. PE Cache

The PE cache precomputes the positional encoding factors for every explicit
position that a model may see in a given experiment.

The cache is keyed by:

```text
pe_mode
domain/layout id
position set id
head_dim
device/dtype when materialized
```

`components/posenc.py` should not decide sequence order. It should only:

```text
positions + pe_mode -> cached PE factors
q/k + position_ids + cache -> position-encoded q/k
```

No axial RoPE or MonSTER factors should be recomputed inside the model forward
pass once the cache exists.

## Experiment Families

The target config files are:

```text
configs/t0d.py    -> data/0d-ar2-97
configs/t1d.py    -> data/1d-dyadrads
configs/t2d.py    -> data/2d-dyadaxes
configs/t3d.py    -> data/3d-dyadaxes
configs/multi.py  -> all four dataset branches
```

Each single-domain config may compare several PE methods, but each trained
model still has exactly one PE method. `configs/multi.py` is the only
multi-domain family.

## Single-Domain Experiment

For a single-domain run:

```text
Domain/Dataset
  -> Canonical Sequence
  -> Position Set
  -> one PE method
  -> one PE cache
  -> batches map tokens to cache ids
  -> model forward gathers cached PE
```

Example:

```text
configs/t2d.py with dataset 2d-dyadaxes and pe=monster
  -> one t+2D canonical sequence
  -> one t+2D position set
  -> one monster cache
  -> exported checkpoint ckpts/t2d/ckpts/t2d_monster.pt
```

The same dataset with standard RoPE is a different trained model:

```text
configs/t2d.py with dataset 2d-dyadaxes and pe=rope
  -> one t+2D canonical sequence
  -> one t+2D position set
  -> one rope cache
  -> exported checkpoint ckpts/t2d/ckpts/t2d_rope.pt
```

Both models use the same dataset and canonical sequence. They differ only in
how their single PE method transforms explicit positions into cached PE
factors.

## Multi-Domain Experiment

The multi-domain setup is the special case. It still trains one model with one
PE method. It does not mix PE methods inside one model.

The difference is that `configs/multi.py` has four domain layouts:

```text
t+0D canonical sequence
t+1D canonical sequence
t+2D canonical sequence
t+3D canonical sequence
```

Therefore one multi-domain model has one same-method cache bundle:

```text
multi with pe=monster
  -> monster cache for t+0D
  -> monster cache for t+1D
  -> monster cache for t+2D
  -> monster cache for t+3D
  -> exported checkpoint ckpts/multi/ckpts/multi_monster.pt
```

The same pattern applies to every PE mode:

```text
multi with pe=rope
  -> rope cache for t+0D
  -> rope cache for t+1D
  -> rope cache for t+2D
  -> rope cache for t+3D

multi with pe=4d-axial
  -> 4d-axial cache for t+0D
  -> 4d-axial cache for t+1D
  -> 4d-axial cache for t+2D
  -> 4d-axial cache for t+3D
```

At batch time, each episode carries its domain/layout id. The model uses that
id to select the appropriate cache from the bundle, then gathers PE factors by
the token-level position ids.

This avoids padding every domain to one shared 4x context window while still
using one model and one PE method.

## Position Sets

A position set is the deduplicated set of explicit coordinates used by one
unique domain/position configuration. It is not enough to have only one
training set and one generic eval set. The cache bundle should contain one
layout for every distinct coordinate universe the model may see.

The layout identity should include:

```text
dataset/domain id
native shape
source-state horizon
coordinate transform id, when present
```

Boundary policy is not part of the position layout because it changes rule
reads, not token coordinates. Rule id and seed id are also not part of the
position layout because they change values, not positions.

For training:

```text
1. Build the training position set from the train stream layout.
2. Build one PE cache for the model's PE method.
3. Tokenization maps each token to a position id.
4. Batching pads/collates position ids.
5. Forward gathers cached PE factors.
```

For single-domain runs there is one training position set. For multi-domain
runs there are four training position sets, one per layout, assembled into a
same-method cache bundle.

Eval adds more layouts to the same-method cache bundle:

```text
OOD horizon
  -> same domain/shape
  -> longer source-state horizon
  -> separate layout/cache entry

OOD scale
  -> same domain
  -> larger native shape
  -> separate layout/cache entry

Invariance transform
  -> same domain/shape/horizon
  -> transformed coordinate frame
  -> separate layout/cache entry per transform
```

So `multi` with `pe=monster` during training has four layouts. During a full
eval it may temporarily use a larger eval cache bundle containing:

```text
4 train layouts
OOD horizon layouts
OOD scale layouts
invariance transform layouts
```

The trained model is unchanged. Only the active cache bundle changes for eval.

## Standard RoPE Is Still Explicit

Standard RoPE should be treated as a PE method over explicit positions, not as
an implicit use of token index.

The intended path is:

```text
[t, x, y, z]
  -> layout-specific scalarization
  -> rope cache index
  -> cached cos/sin factors
```

For ordinary untransformed data, scalarization can match the canonical
row-major sequence. For OOD translations, axis lifts, or plane changes, the
scalarized coordinate should reflect the transformed absolute position rather
than renumbering from zero.

This is necessary for fair invariance and OOD tests. Otherwise standard RoPE
would be insensitive to coordinate shifts that should be visible to it.

## Invariance Evaluation

Invariance eval is separate from training.

The intended process is:

```text
1. Collect an invariance episode subset from train rule/seed distributions.
2. Create transformed coordinates for those episodes.
3. Build the invariance eval position set:
     training positions + transformed positions
4. Build an eval PE cache or cache bundle for the same PE method.
5. Map original and transformed episodes through the normal tokenizer/batcher.
6. Compare original score against transformed score.
```

The model is not retrained. Only the eval cache extends the position universe
to include transformed coordinates.

Useful Phase 1 transforms should cover easy and hard coordinate shifts:

```text
small translations outside the native range, such as +10
large translations far outside the native range, such as +100 or +1000
single-axis translations
axis reflections, such as x -> -x
multi-axis reflections
axis permutations, such as xyz -> yzx
plane rotations, such as 90 degrees in xy
axis lifts, such as x -> y for 1D
plane lifts, such as xy -> yz for 2D
```

The main metric is degradation:

```text
delta_loss = transformed_loss - original_loss
delta_accuracy = transformed_accuracy - original_accuracy
```

## Responsibility Split

`ankos/src/ca` owns:

```text
CA dynamics
coordinate/loci primitives
alphabet, neighborhood, frontier, seed, rule, and boundary primitives
deterministic RNG primitives
raw rollout
raw canonical coordinates
no PE stream policy, seed-recipe selection, tokens, masks, losses, or model batches
no rollout-time RNG; stochastic seeds are rendered before rollout
```

`data/<dataset>/prepare.py` owns:

```text
dataset-specific source compilation
manifest/manifest.json
manifest/vocab.json
manifest/rule_pools.json
manifest/train_streams.json
manifest/eval_streams.json
```

`data/datasets.py` owns:

```text
dataset branch registry
dataset preparation orchestration
manifest loading
stream descriptor access for configs and batch builders
shared dataset preparation helpers
```

`components/tokenizer.py` owns:

```text
canonical sequence construction
model-facing [t,x,y,z] coordinates
position set construction
token-to-position-id mapping
layout/domain ids emitted with serialized episodes
raw value to token id serialization
next-state target metadata
```

`components/batch.py` owns:

```text
runtime episode realization
padding/collation of input ids, targets, masks, and position ids
domain/cache-key collation for multi-domain batches
device transfer
```

`components/posenc.py` owns:

```text
building cached PE factors from explicit position sets
applying cached PE factors to q/k tensors
no sequence construction
no dataset semantics
```

`components/attention.py` owns:

```text
attention execution
dense state-causal mask handling
backend-specific attention details
no PE cache construction
```

`model.py` owns:

```text
one PE mode per model
one PE cache for single-domain models
one same-method PE cache bundle for multi-domain models
cache selection by domain/layout id
cache gather by position ids
```
