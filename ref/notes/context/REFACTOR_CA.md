# CA Refactor Guide

This document is a subordinate migration guide for extracting reusable cellular
automata mechanics from PE into the standalone `ankos` repo.

The source of truth for names, final file layout, and repo boundaries is:

```text
context/REFACTOR_TARGET.md
```

If this document conflicts with `context/REFACTOR_TARGET.md`, use
`context/REFACTOR_TARGET.md`.

## Scope

For the current refactor, only these two goals are in scope:

1. Move reusable CA mechanics into `/home/jake/Developer/ankos/src/ca`.
2. Repair PE around the normalized GPT/common-core layout from
   `context/REFACTOR_TARGET.md`.

Out of scope for this phase:

- vectorization and speed optimization
- the custom attention mask module
- new research features beyond preserving Phase 1 behavior
- broad redesign of experiment policy

## Array Backend Target

`ankos` should use NumPy-compatible raw arrays as its public CA rollout form
factor. PyTorch remains the right representation inside PE, but the conversion
belongs at the PE batch boundary.

Target contract:

```text
ankos public API:
  NumPy semantics
  states as ndarray-like arrays
  coords as integer ndarray-like arrays or layout metadata plus a materializer
  no device/runtime policy

pe/components/batch.py:
  convert CA arrays with torch.from_numpy(...)
  collate torch tensors for model, masks, PE caches, and losses
```

Preferred rollout shapes:

```text
unbatched states: (T, *spatial_shape)
batched states:   (B, T, *spatial_shape)
coords:           (T * cell_count, 4), when materialized
rule_ids:         (B,), for batchable rollout inputs
seed_states:      (B, *spatial_shape), for batchable rollout inputs
```

A future backend option such as `backend="numpy" | "torch"` can be added if
GPU-resident rollout becomes important. That should be treated as an
optimization, not the baseline public contract.

## Source Paths

The old CA catalog source files live under:

```text
old/data/components
```

Use that directory as the source for the CA catalog modules. Do not treat
`data/components` as the migration source when this guide says to move old CA
code.

Expected source-to-target mapping:

```text
old/data/components/loci.py          -> ankos/src/ca/loci.py
old/data/components/alphabets.py     -> ankos/src/ca/alphabets.py
old/data/components/neighborhoods.py -> ankos/src/ca/neighborhoods.py
old/data/components/frontiers.py     -> ankos/src/ca/frontiers.py
old/data/components/seeds.py         -> ankos/src/ca/seeds.py
old/data/components/rules.py         -> ankos/src/ca/rules.py
```

These old component files do not transfer into `ankos` as-is:

```text
old/data/components/datasets.py
old/data/components/evals.py
```

`old/data/components/datasets.py` contains PE dataset composition and policy
ideas. Re-express the useful dataset facts through PE's target dataset layout:

```text
pe/data/<dataset>/prepare.py
pe/data/datasets.py
```

`old/data/components/evals.py` is PE experiment/evaluation policy. Re-express
useful evaluation logic through:

```text
pe/components/evals.py
```

The following `ankos` target modules are new normalized modules. They may be
assembled from old behavior where available, but their final shape is governed
by the target layout:

```text
ankos/src/ca/specs.py
ankos/src/ca/boundary.py
ankos/src/ca/rng.py
ankos/src/ca/rollout.py
ankos/src/ca/__init__.py
ankos/src/ca/py.typed
```

Detailed source lookup for the normalized modules:

```text
ankos/src/ca/specs.py
  old/data/components/datasets.py: DatasetSpec shape and dynamics fields
  old/data/generate.py: Episode runtime result shape
  old/data/components/alphabets.py: Alphabet shape
  old/data/components/neighborhoods.py: Neighborhood shape
  old/data/components/frontiers.py: Frontier shape
  old/data/components/seeds.py: Seed shape
  old/data/components/rules.py: Rule and RuleChannel shape
  old/data/components/loci.py: CoordinateSpace / Selector / Selection shape

ankos/src/ca/boundary.py
  old/data/components/loci.py: _BOUNDARY_POLICIES
  old/data/components/loci.py: gather policy mechanics
  old/data/generate.py: apply_boundary_read
  old/data/generate.py: _read_component boundary setup
  old/data/generate.py: boundary metadata on Episode

ankos/src/ca/rng.py
  old/data/batch.py: splitmix64
  old/data/batch.py: derive_episode_rng
  old/data/batch.py: render_seed_state torch-generator call site, as a NumPy replacement guide only
```

Boundary defaults and eval variants are PE policy, not CA mechanics:

```text
pe/data/datasets.py and pe/data/<dataset>/prepare.py
  old/data/components/datasets.py: default dataset boundaries
  old/prepare.py: manifest/train/eval stream boundary propagation

pe/components/evals.py or pe/data/datasets.py, depending on policy ownership
  old/data/components/evals.py: ood_boundary fixed-one / periodic / reflective variants
  old/data/batch.py: eval-row variant boundary override behavior
```

Do not preserve a reverse-compatibility boundary path as a target. The target is
direct ownership: `ca.boundary` implements boundary mechanics, `ca.loci`
provides coordinate/index helpers, and PE owns boundary selection policy.

## Target Repo Boundaries

### `ankos`

`ankos` is the reusable cellular automata package and research reference repo.
Its Python import package is:

```python
import ca
```

Target layout:

```text
ankos
├── src
│   └── ca
│       ├── __init__.py
│       ├── py.typed
│       ├── specs.py
│       ├── loci.py
│       ├── alphabets.py
│       ├── neighborhoods.py
│       ├── frontiers.py
│       ├── seeds.py
│       ├── rules.py
│       ├── boundary.py
│       ├── rng.py
│       └── rollout.py
├── ref
├── tests
├── pyproject.toml
├── uv.lock
└── README.md
```

`ankos` owns this question:

```text
Given reusable CA dynamics, a rule id, seed state, and step
count, what raw trajectory is generated?
```

`ankos` should not know about:

```text
dataset train/eval splits
held-out rule policy
train/eval stream JSON
BOS tokens
domain tokens
token ids
position ids
layout ids
attention masks
PyTorch transformer batches
torch tensors or device placement
loss masks
PE modes
training loops
evaluation metrics
checkpoint policy
```

### `pe`

`pe` is the positional-encoding experiment repo. Its target layout is:

```text
pe
├── configs
│   ├── t0d.py
│   ├── t1d.py
│   ├── t2d.py
│   ├── t3d.py
│   └── multi.py
├── data
│   ├── 0d-ar2-97
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   ├── 1d-dyadrads
│   ├── 2d-dyadaxes
│   ├── 3d-dyadaxes
│   └── datasets.py
├── ckpts
│   ├── t0d
│   ├── t1d
│   ├── t2d
│   ├── t3d
│   └── multi
├── components
│   ├── attention.py
│   ├── posenc.py
│   ├── optimizer.py
│   ├── tokenizer.py
│   ├── evals.py
│   ├── checkpoint.py
│   └── batch.py
├── model.py
├── train.py
├── eval.py
└── README.md
```

PE owns:

```text
dataset branches and manifests
rule pool split policy
train/eval stream policy
tokenization
torch conversion at the batch boundary
position ids and layout ids
state-causal attention masks
batch collation
PE cache construction and application
model/training/evaluation/checkpoint orchestration
```

## Normalized Responsibility Split

### `ankos/src/ca/specs.py`

Small shared dataclasses and JSON-friendly specs.

Recommended Phase 1 objects:

```text
AlphabetSpec
BoundarySpec
NeighborhoodSpec
FrontierSpec
SeedSpec
RuleSpec
Dynamics
RawEpisode
```

Keep specs plain and serializable. Avoid callable predicates, open Python
objects, tensors, or arrays inside source specs. `RawEpisode` is a runtime
result and should expose NumPy-compatible arrays for public `ankos` output.

Use lowercase domain strings:

```text
t+0d
t+1d
t+2d
t+3d
```

### `ankos/src/ca/loci.py`

Move and clean the old coordinate-space logic from:

```text
old/data/components/loci.py
```

This module owns canonical `[t, x, y, z]` coordinate spaces, coordinate
universes, selection helpers, ordering, and native array index conversion.

Keep useful behavior:

```text
CoordinateSpace
coordinate_space()
active_axes()
axis_values()
coord_vectors()
coord_grid()
absolute_universe()
offset_universe()
select()
mask()
order_lex()
native_indices()
gather()
```

Cleanup requirements:

- make rank-0 coordinate generation return a 2D integer coordinate array
- standardize domain/rank behavior around `t+0d` through `t+3d`
- keep `frame` and `read_mode` as metadata unless implemented fully
- make `CoordinateSpace` the source of truth for native indexing

### `ankos/src/ca/alphabets.py`

Move finite alphabet behavior from:

```text
old/data/components/alphabets.py
```

Phase 1 supported factories:

```text
boolean()
int_range_alphabet()
float_range_alphabet()
symbolic()
```

The current PE benchmarks primarily need:

```text
binary alphabet
mod-97 integer alphabet
```

Future factories may remain in the source tree, but they should raise clear
`NotImplementedError`s and should not be exported as supported public API unless
they are actually implemented.

### `ankos/src/ca/neighborhoods.py`

Move implemented neighborhood factories from:

```text
old/data/components/neighborhoods.py
```

Phase 1 supported factories:

```text
self_at()
axis_shell()
l1_shell()
change_count_shell()
ar2_0d()
dyadrads_1d()
dyadaxes_2d()
dyadaxes_3d()
compose()
```

Behavior to preserve:

```text
ar2_0d:
  scalar history reads

dyadrads_1d:
  previous self
  radius-1 x shell
  radius-2 x shell

dyadaxes_2d:
  previous self
  cardinal shell
  diagonal shell

dyadaxes_3d:
  previous self
  face shell
  edge/corner shell
```

`compose()` preserves component boundaries. Merged/unioned neighborhood
supports should be added later as an explicit support-algebra operation, not as
metadata on `compose()`.

### `ankos/src/ca/frontiers.py`

Move the old frontier schema from:

```text
old/data/components/frontiers.py
```

Phase 1 executable frontier:

```text
time_slice()
```

The target module is still named `frontiers.py`, but Phase 1 rollout should
reject unsupported frontier families:

```python
if dynamics.frontier.family != "time_slice":
    raise NotImplementedError(...)
```

This fixes the old mismatch where a frontier existed in the API but rollout
ignored it.

### `ankos/src/ca/seeds.py`

Move seed specs and rendering from:

```text
old/data/components/seeds.py
```

Phase 1 supported, manifest-safe seeds:

```text
pair()
uniform_pair()
bernoulli()
constant()
point()
selector_seed(), if its params are JSON-safe
render()
dedupe()
structured(), only for supported JSON-safe structured seeds
```

Keep future/experimental seeds clearly separated from manifest-safe seeds:

```text
fractal
spiral
path with temporal ambiguity
transform variants with unimplemented rotate/reflect/permute behavior
symmetry dedupe
callable predicates
```

PE manifests should only write seed specs that round-trip through JSON.
Seed rendering should produce NumPy-compatible arrays in `ankos`. PE batch code
is responsible for converting rendered seed states to torch tensors if needed.

### `ankos/src/ca/rules.py`

Move rule catalog behavior from:

```text
old/data/components/rules.py
```

This is one of the most important cleanup points. Phase 1 rule instantiation
must always produce executable behavior for supported Phase 1 rules.

Supported Phase 1 rule families:

```text
ar2_modular_0d
dyadrads_1d
dyadaxes_2d
dyadaxes_3d
```

Useful public helpers:

```text
rule_count(rule)
valid_rule_ids(rule)
instantiate(rule, rule_id)
```

`instantiate()` should validate the rule id and return an executable rule for
all supported Phase 1 families.

Do not put train/eval rule-pool splitting in `ca.rules`. `ca.rules` knows which
rule ids exist. PE decides which ids are train, eval, held out, or sampled.

### `ankos/src/ca/boundary.py`

Centralize boundary handling here.

Supported Phase 1 policies:

```text
none
fixed
periodic
reflective
```

Useful surface:

```text
none()
fixed(value=0)
periodic()
reflective()
apply_boundary_read(...)
```

For default PE datasets:

```text
t+0d AR2: no spatial boundary
spatial CA: fixed zero
OOD boundary eval: fixed one, periodic, reflective
```

The fact that OOD eval should use alternate boundaries is PE experiment policy,
not CA package policy.

### `ankos/src/ca/rng.py`

Generic deterministic RNG primitives live here.

Useful surface:

```text
splitmix64()
derive_episode_rng()
numpy_rng()
```

`ca.rng` should provide deterministic NumPy RNG construction. A torch generator
helper is PE-side or future backend-specific code, not part of the baseline
`ankos` public API.

Do not put these PE policies in `ca.rng`:

```text
cycle through train rule pool
cycle through eval rule pool
held-out-rule stream construction
held-out-seed stream construction
eval row formatting
```

### `ankos/src/ca/rollout.py`

This module is the cleaned-up standalone successor to old `data/generate.py`.
The rename is intentional:

```text
generate.py  old PE-local name
rollout.py   CA-library name for evolving one dynamics setup forward
```

This module owns raw next-state trajectory generation. It answers:

```text
Given CA dynamics, seed state, rule id, and step count, what raw trajectory is
generated?
```

Useful surface:

```python
def rollout(
    dynamics,
    rule_id,
    seed_state,
    steps,
    *,
    rng=None,
    return_coords=True,
):
    ...
```

Public rollout inputs and outputs should be NumPy-compatible. `seed_state`
should be an ndarray-like raw state, and returned `states` should be an
ndarray-like trajectory.

Also expose:

```text
canonical_coords(domain, shape, steps)
```

Move these old `data/generate.py` concepts here:

```text
Episode / RawEpisode dataclass
rollout
canonical_coords
apply_boundary_read
apply_rule
_rollout_ar2
_rollout_spatial_lookup
_next_spatial_state
_read_component
_channel_state
_apply_gate
_lookup_index
```

Phase 1 rollout behavior:

```text
0D:
  AR2 scalar recurrence

1D/2D/3D:
  full synchronous next-state update
  configured boundary
  dyadrads/dyadaxes lookup rule
  raw values only
```

Old `data/generate.py` accepted a frontier argument but ignored it. The new
rollout must not silently do that. Phase 1 supports only current time-slice
synchronous rollout:

```python
if dynamics.frontier.family != "time_slice":
    raise NotImplementedError(
        "ankos Phase 1 supports only time_slice rollout"
    )
```

Rollout returns raw CA output:

```text
states  # NumPy-compatible array, (T, *spatial_shape)
coords  # integer array, (T * cell_count, 4), when materialized
rule_id
metadata
```

It returns no token ids, BOS/domain tokens, position ids, layout ids, attention
masks, loss masks, labels, batch padding, train/eval split decisions,
held-out-rule policy, PE caches, torch tensors, device placement, or
transformer batch metadata.

### `ankos/src/ca/__init__.py`

Export the supported Phase 1 surface only. Do not export every future stub
unless it is intentionally part of the public API.

Example export categories:

```text
spec dataclasses
supported alphabet factories
supported boundary factories
supported neighborhood factories
time_slice
supported seed factories and render()
supported rule factories and instantiate()
rule_count() and valid_rule_ids()
splitmix64(), derive_episode_rng(), and numpy_rng()
rollout() and canonical_coords()
```

## PE Integration

### `pe/data/datasets.py`

This file is the shared PE dataset registry and preparation substrate. It is
not the CA package and should not become a second model framework.

It should know:

```text
which dataset branches exist
how to find each dataset manifest directory
how to check whether a dataset is prepared
how to invoke or route to each dataset's prepare.py
how to load manifest/vocab/rule-pool/train/eval stream descriptors
how to return stream descriptors to configs and batch builders
```

Appropriate shared helpers:

```text
read_json()
atomic_write_json()
json_ready()
stable_hash64()
stable_digest()
dataset_root()
manifest_dir()
load_manifest_bundle()
write_manifest_bundle()
build_rule_pools()
cycle_rule_selection()
seed_stream()
train_stream()
eval_stream()
held_out_rule_eval()
held_out_seed_eval()
ood_horizon_eval()
ood_scale_eval()
ood_boundary_eval()
invariance_eval()
```

Do not put transformer model code, optimizer code, PE math, attention backend
logic, checkpoint policy, or full training loops in `data/datasets.py`.

### `pe/data/<dataset>/prepare.py`

Each dataset branch has its own small preparation script:

```text
pe/data/0d-ar2-97/prepare.py
pe/data/1d-dyadrads/prepare.py
pe/data/2d-dyadaxes/prepare.py
pe/data/3d-dyadaxes/prepare.py
```

Each prepare script should define:

```text
dataset id
domain
shape
CA Dynamics
source-state count
raw-state count
default boundary
rule family
seed family
rule-pool split choices
train stream choices
eval stream choices
vocab/domain token choices
```

Each prepare script should write exactly the target manifest files:

```text
manifest/manifest.json
manifest/vocab.json
manifest/rule_pools.json
manifest/train_streams.json
manifest/eval_streams.json
```

It should not train a model, build PE caches, build attention masks, instantiate
a transformer, write dense batches by default, or own common eval policy code.

### `pe/components/tokenizer.py`

Model-facing tokenization belongs here.

It owns:

```text
vocab expansion
raw value to token id mapping
BOS/domain token insertion
canonical sequence construction
model-facing [t, x, y, z] coordinates
position set construction
token-to-position-id mapping
layout/domain ids emitted with serialized episodes
next-state targets
loss token metadata
```

This is the target destination for the useful next-state tokenizer behavior
from the old/current PE code. Legacy text/parquet/BPE compatibility should not
pollute this path unless explicitly preserved for a separate reason.

### `pe/components/batch.py`

Runtime stream realization and collation belong here.

It owns:

```text
reading prepared train/eval stream specs
deriving per-episode RNGs
sampling or cycling rule ids from prepared rule pools
rendering CA seed states through ca
calling ca.rollout()
applying runtime rollout filters when implemented
calling components.tokenizer
converting NumPy-compatible CA arrays with torch.from_numpy(...)
padding/collating input ids, targets, masks, coordinates, position ids
domain/cache-key collation for multi-domain batches
device transfer
```

The first mask implementation remains the simple dense state-causal mask from
the older design:

```text
[B, T, T] boolean mask
state tokens attend BOS/domain plus state times <= query source time
```

The custom attention mask module is out of scope for this phase.

### `pe/components/posenc.py`

Move PE cache-bundle math here.

It owns:

```text
RoPE
axial RoPE
MonSTER
position-set based cache construction
layout-keyed cache bundles
cached Q/K position encoding
```

Keep the explicit-coordinate cache path as the model-facing path:

```text
positions + pe mode -> cached factors
q/k + layout ids + position ids + cache -> encoded q/k
```

Do not make sequence order implicit inside PE math.

### `pe/components/attention.py`

Attention execution and mask handling belong here.

It owns:

```text
Q/K/V routing
attention backend selection
mask handling
GQA details
state-causal dense mask consumption
```

Positional encoding should remain separate except where attention receives
already-positioned Q/K tensors.

### `pe/components/evals.py`

Evaluation routines belong here.

It owns:

```text
training-time validation routines
standalone checkpoint evaluation routines
next-state loss/accuracy metrics
invariance/OOD metric helpers
```

The target file is `components/evals.py`, not `data/components/evals.py`.

### `pe/components/optimizer.py`

Optimizer construction, parameter grouping, and optimizer update policy belong
here.

### `pe/components/checkpoint.py`

Checkpoint persistence/loading helpers belong here.

It should handle:

```text
model state
optimizer state
training state
metadata
checkpoint pointers
compile-prefix cleanup
weight-only loading
```

It should not know how to build CA dynamics, tokenizers, PE caches, or data
streams.

## PE Configs And Entrypoints

Use the normalized config filenames:

```text
configs/t0d.py
configs/t1d.py
configs/t2d.py
configs/t3d.py
configs/multi.py
```

Do not use the old JSON config names as target names:

```text
v1-t+0d.json
v1-t+1d.json
v1-t+2d.json
v1-t+3d.json
v1-multi.json
```

The target root entrypoints are:

```text
train.py
eval.py
```

Do not introduce separate root experiment files as a target requirement unless
that decision is made later. `context/REFACTOR_TARGET.md` lists only
`train.py` and `eval.py`.

## Manifests

Each dataset branch uses this exact manifest layout:

```text
data/<dataset>/manifest
├── manifest.json
├── vocab.json
├── rule_pools.json
├── train_streams.json
└── eval_streams.json
```

### `manifest.json`

Source identity and CA dynamics.

Recommended contents:

```json
{
  "dataset_id": "2d-dyadaxes",
  "manifest_version": "v1",
  "domain": "t+2d",
  "shape": [11, 11],
  "source_states_per_episode": 16,
  "raw_states_per_episode": 17,
  "alphabet": {"family": "boolean", "values": [0, 1]},
  "seed": {"family": "bernoulli", "params": {"p": 0.5}},
  "dynamics": {
    "neighborhood": {"family": "dyadaxes_2d"},
    "frontier": {"family": "time_slice"},
    "rule": {"family": "dyadaxes_2d", "rule_count": 256},
    "boundary": {"policy": "fixed", "value": 0}
  },
  "hashes": {
    "dynamics": "...",
    "rule_pools": "...",
    "vocab": "..."
  }
}
```

### `vocab.json`

Compact token recipe.

Recommended contents:

```json
{
  "special_tokens": {
    "<pad>": 0,
    "<bos>": 1,
    "<domain:t+2d>": 2
  },
  "alphabets": {
    "binary": {
      "offset": 3,
      "values": [0, 1]
    }
  },
  "dataset_to_alphabet": {
    "2d-dyadaxes": "binary"
  }
}
```

### `rule_pools.json`

Prepared rule split.

Recommended contents:

```json
{
  "train": [0, 1, 2],
  "eval": [17, 99, 144],
  "policy": {
    "family": "deterministic_hash_shuffle",
    "salt": "v1",
    "train_fraction": 0.8
  }
}
```

### `train_streams.json`

Train streams are deterministic recipes, not enumerated rows.

Recommended contents:

```json
[
  {
    "split": "train",
    "dataset_id": "2d-dyadaxes",
    "rule_selection": {
      "pool": "train",
      "policy": "cycle"
    },
    "seed_stream": {
      "family": "bernoulli",
      "policy": "splitmix64",
      "base_rng": 12345
    }
  }
]
```

### `eval_streams.json`

Pinned eval stream recipes.

Prefer `kind`, not the old `eval` key.

Recommended contents:

```json
[
  {
    "kind": "held_out_rule",
    "split": "eval",
    "dataset_id": "2d-dyadaxes",
    "count": 256,
    "rule_selection": {
      "pool": "eval",
      "policy": "cycle"
    },
    "seed_stream": {
      "family": "bernoulli",
      "policy": "splitmix64",
      "base_rng": 810421
    }
  }
]
```

## Dataset Readmes

Use lowercase `readme.md` inside PE dataset and checkpoint branches.

Each dataset `readme.md` should be short and concrete:

```text
# 2d-dyadaxes

Domain:
  t+2d

Shape:
  11 x 11

Rule family:
  256-rule Dyadaxes lookup family

State:
  binary

Update:
  current time-slice synchronous update

Neighborhood:
  previous self
  cardinal aggregate
  diagonal aggregate

Boundary:
  fixed zero for train/default eval

Prepared files:
  manifest/manifest.json
  manifest/vocab.json
  manifest/rule_pools.json
  manifest/train_streams.json
  manifest/eval_streams.json

Regenerate:
  uv run python data/2d-dyadaxes/prepare.py
```

## Migration Order

### Step 1: Extract `ankos/src/ca`

Move CA catalog code from `old/data/components` into the normalized `ankos`
package:

```text
old/data/components/loci.py          -> ankos/src/ca/loci.py
old/data/components/alphabets.py     -> ankos/src/ca/alphabets.py
old/data/components/neighborhoods.py -> ankos/src/ca/neighborhoods.py
old/data/components/frontiers.py     -> ankos/src/ca/frontiers.py
old/data/components/seeds.py         -> ankos/src/ca/seeds.py
old/data/components/rules.py         -> ankos/src/ca/rules.py
```

Create or normalize:

```text
ankos/src/ca/specs.py
ankos/src/ca/boundary.py
ankos/src/ca/rng.py
ankos/src/ca/rollout.py
ankos/src/ca/__init__.py
ankos/src/ca/py.typed
```

Immediately fix these old ambiguities:

```text
frontier must be enforced or rejected by rollout
Phase 1 rule instantiation must be executable
boundary handling should be centralized
manifest-facing specs must be JSON-safe
domain strings should be lowercase
public rollout arrays should use NumPy semantics, not torch tensors
torch conversion belongs in pe/components/batch.py
```

### Step 2: Build PE Dataset Branches

Create target dataset directories:

```text
data/0d-ar2-97
data/1d-dyadrads
data/2d-dyadaxes
data/3d-dyadaxes
```

Each gets:

```text
manifest/
prepare.py
readme.md
```

Build shared registry/preparation helpers in:

```text
data/datasets.py
```

### Step 3: Move PE Common-Core Components

Normalize PE component destinations:

```text
positional encoding     -> components/posenc.py
attention execution     -> components/attention.py
tokenization            -> components/tokenizer.py
batch collation         -> components/batch.py
evaluation routines     -> components/evals.py
optimizer helpers       -> components/optimizer.py
checkpoint helpers      -> components/checkpoint.py
```

Remove legacy text/parquet/BPE paths from the active next-state component path
unless explicitly preserved outside the Phase 1 training flow.

### Step 4: Repair Root Entrypoints

Keep target root files:

```text
model.py
train.py
eval.py
README.md
```

`model.py` composes the transformer from components. `train.py` orchestrates
training. `eval.py` performs standalone evaluation. `README.md` documents the
repo.

### Step 5: Check Target Naming

Before considering the refactor complete, verify:

```text
PE configs are t0d.py, t1d.py, t2d.py, t3d.py, multi.py
PE dataset dirs are 0d-ar2-97, 1d-dyadrads, 2d-dyadaxes, 3d-dyadaxes
PE checkpoint dirs are ckpts/t0d, ckpts/t1d, ckpts/t2d, ckpts/t3d, ckpts/multi
checkpoint filenames are {experiment}_{pe}.pt
ankos import package is ca
ankos references are under ref
ankos notes are under ref/notes
ankos archived notes are under ref/notes/archived
ankos uv docs are under ref/uv-docs
```

## Direct Boundary Summary

Use this line when deciding where code belongs:

```text
ankos/src/ca:
  generic CA mechanics and NumPy-compatible raw rollout

pe/data/datasets.py:
  PE dataset registry, manifest IO, and shared stream/preparation policy

pe/data/<dataset>/prepare.py:
  dataset-specific source compilation

pe/components/tokenizer.py:
  model-facing serialization, vocab, coordinates, position ids, targets

pe/components/batch.py:
  runtime example realization, torch conversion, masking, collation, device movement

pe/components/posenc.py:
  explicit-position PE cache math

pe/model.py, pe/train.py, pe/eval.py:
  model composition, training orchestration, standalone evaluation
```
