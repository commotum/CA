## Project Description

This project is a research library for studying transformers as
**next-state predictors** over simple procedural worlds. The central problem is
positional encoding: standard RoPE is natural for 1D autoregressive text, but
spatiotemporal prediction across `0D+t`, `1D+t`, `2D+t`, and `3D+t` does not
have a single obvious positional scheme.

The project builds controlled dynamical systems - scalar recurrences and
cellular automata - where the model must infer a latent rule from observed
states and predict the next full state. By keeping alphabets tiny, rules
procedural, and data synthetic, the experiments isolate spatiotemporal
structure instead of burying it under language, search, or task-specific
engineering.

The main comparison target is positional encoding under a shared transformer
backbone and matched training/evaluation budgets. Experiments can compare
standard RoPE, axial RoPE at different dimensionalities, and MonSTER, a 4D
spacetime generalization of RoPE over `(t, x, y, z)`.

The experiment and positional-cache architecture is specified in
[experiment_architecture.md](experiment_architecture.md).

## Core Objective

The library should answer one practical question:

```text
Which positional encoding gives a domain-agnostic transformer the best
geometric prior for next-state prediction across temporal, spatial, and mixed
spatiotemporal procedural domains?
```

That requires the data layer to be reproducible, cheap to regenerate, and clear
about what is fixed before training versus what is realized at runtime.

## Indexing Convention

We use Wolfram's dynamical-update convention. `t` indexes the current source
state, and the update relation maps the full state at `t` to the predicted full
state at `t+1`.

A token at coordinate `[t, x, y, z]` is consumed as part of the current state.
Its supervised target is the corresponding value at `[t+1, x, y, z]` when that
coordinate exists. This matches transformer shifted-logit semantics while
keeping the cellular-automaton update law explicit.

Raw generated trajectories use natural state times `0..T-1`. Model-facing
serialized coordinates reserve `[0, 0, 0, 0]` for BOS/domain tokens and shift
real state tokens to `t=1..T`, with unused spatial axes set to zero. Dense
state-causal masks use token type metadata, so BOS/domain remain visible to
state tokens without being treated as state cells.

## Construction Principle

The pipeline follows a layered construction principle:

- keep primitive layers minimal and generic
- build named Python factory families by composing primitives
- build complete dataset specs by composing named singular families
- freeze source identity before training
- generate trajectories on demand at runtime

Catalog modules such as `loci.py`, `neighborhoods.py`, `frontiers.py`,
`seeds.py`, `rules.py`, `alphabets.py`, `datasets.py`, and `evals.py` define
declarative dataset and evaluation components. They do not create batches,
train models, or decide runtime sampling.

## Revised Responsibility Split

The original `autoresearch` `prepare.py` mixed three responsibilities in one
file: source creation, tokenization, and dataloading. This project splits those
responsibilities and adds a pure rollout layer for next-state dynamics.

### `prepare.py`: Source And Manifest Freezer

`prepare.py` is a one-time pre-runtime script. It freezes procedural dataset
sources, not raw trajectories.

It should:

- read `configs/*.json`
- resolve dataset ids through `data.components.datasets`
- resolve eval ids through `data.components.evals`
- build deterministic rule pools by id and policy only
- define train/eval seed stream namespaces
- write deterministic train stream specs
- write deterministic eval stream specs
- call `data.tokenize.vocab(...)` to freeze a compact `vocab.json` recipe
- write hashes and version metadata under `data/datasets/`

It should not:

- call `data.generate.py`
- call `data.batch.py`
- run rollout-based rule filtering
- store raw trajectories by default

### `data/generate.py`: Pure Rollout

`generate.py` owns deterministic next-state evolution from an initial seed
state.

It should:

- accept a resolved update contract, an initial seed state, a rule id, shape,
  boundary policy, and step count
- apply the rule over time
- preserve native dimensional state structure
- return raw states and canonical coordinates when useful

It should not:

- choose train/eval splits
- sample rule ids
- sample seed streams
- tokenize
- pad
- create labels or batches
- filter rules

### `data/tokenize.py`: Vocabulary And Episode Serialization

`tokenize.py` owns the representation boundary between raw trajectory values
and model tokens.

It should:

- build and freeze vocabularies from selected dataset alphabets
- persist compact vocab recipes, not expanded lookup tables
- build canonical sequence layouts for each dataset/domain
- construct explicit model-facing position sets
- serialize one generated episode at runtime
- map raw values to token ids
- attach domain and BOS tokens when requested
- emit token coordinates, position ids, layout/domain ids, time indices,
  next-state targets, and mask metadata

It should not:

- generate trajectories
- sample examples
- own split logic
- prebuild batches
- materialize dense attention masks
- apply positional-encoding math

### `data/batch.py`: Runtime Stream, Filtering, And Buffering

`batch.py` is the runtime data-stream layer used by training and evaluation.

It should:

- read prepared train stream specs and eval stream specs
- derive per-episode RNGs with `splitmix64(base_rng, episode_index)`
- sample rule ids from prepared rule pools
- render seed states from seed specs or seed streams
- call `data.generate.py`
- apply runtime rule/example filtering by inspecting rollouts
- call `data.tokenize.py`
- pad or pack to fixed shapes without cropping spatial state semantics
- build inputs, next-state targets, dense state-causal masks, coordinates,
  position ids, and cache/layout ids
- preallocate buffers and move tensors efficiently

`train.py` should consume `data.batch.py`, not construct datasets directly.

The first mask implementation should be simple and dense: a `[B, T, T]`
boolean mask where `T=max_tokens`. It is state-causal, not token-causal. A
query token in source state `t` may attend BOS/domain tokens and every state
token from times `<= t`, including all tokens in its own state.

## Experiment Architecture

Each trained model has exactly one positional encoding method. A single-domain
experiment has one domain, one canonical sequence, one explicit position set,
and one PE cache:

```text
Domain/Dataset
  -> Canonical Sequence
  -> Position Set
  -> one PE method
  -> one PE cache
  -> batches map tokens to cache ids
  -> model forward gathers cached PE
```

For example, `v1-t+2d` with `monster` has only the `monster` cache for the
`t+2D` canonical sequence. `v1-t+2d` with standard RoPE is a separate model
with only a RoPE cache for the same canonical sequence, using RoPE's
layout-specific scalarization of explicit positions.

The multi-domain setup is the special case. It still trains one model with one
PE method, but that model has a same-method cache bundle:

```text
v1-multi --pe monster
  -> monster cache for t+0D
  -> monster cache for t+1D
  -> monster cache for t+2D
  -> monster cache for t+3D
```

The same applies to `rope`, axial RoPE, and MonSTER. Episode domain/layout id
selects the cache from the bundle, and token-level position ids gather from
that cache.

Standard RoPE is also explicit. It should not rely on the incidental sequence
index. Its intended path is:

```text
[t, x, y, z]
  -> layout-specific scalarization
  -> rope cache index
  -> cached cos/sin factors
```

`pe.py` should do positional-encoding math and cache application only. Sequence
layout, position sets, and token-to-position-id mapping belong to
`data.tokenize.py`; `data.batch.py` pads and collates those ids.

## Manifest Model

Prepared artifacts should describe deterministic sources rather than storing
large raw trajectory corpora.

Evaluation streams are pinned deterministic episode families. They should not
enumerate every row when the row can be derived from stream identity, rule
pools, and `splitmix64` seed streams:

```json
{
  "id": "v1-t+2d/2d-dyadaxes/held-out-rule",
  "split": "eval",
  "eval": "held-out-rule",
  "dataset_id": "2d-dyadaxes",
  "count": 256,
  "row_id_format": "v1-t+2d/2d-dyadaxes/held-out-rule/{index:06d}",
  "rule_selection": {"policy": "cycle", "pool": "eval", "pool_count": 52},
  "seed_stream": {
    "family": "dataset-seed-catalog",
    "policy": "splitmix64",
    "base_rng": 810421
  },
  "shape": [11, 11],
  "max_tokens": 2048,
  "special_tokens_per_episode": 2,
  "source_states_per_episode": 16,
  "raw_states_per_episode": 17,
  "loss_tokens_per_episode": 1936,
  "token_window_slack": 110,
  "boundary": {"policy": "fixed", "value": 0},
  "transform": null
}
```

Phase-1 eval streams use the same compact format with per-stream token-window
budgets:

```text
ID             max_tokens=2048, train shapes, held-out rules/seeds
OOD horizon    max_tokens=4096, train shapes, fill the larger window
OOD scale      larger shapes, fixed 16 source states
OOD boundary   max_tokens=2048, train shapes, alternate read boundaries
```

The clean OOD-scale shapes are `[255]`, `[15, 15]`, and `[7, 7, 7]`. The 3D
scale stream uses `max_tokens=5632` so `[7, 7, 7]` fits 16 source states; the
1D and 2D scale streams use `max_tokens=4096`.

Training manifests are deterministic stream specs. They should not enumerate
every possible training example:

```json
{
  "split": "train",
  "dataset_id": "2d-dyadaxes",
  "rule_pool": "train",
  "seed_stream": {
    "family": "bernoulli",
    "base_rng": 12345
  },
  "shape": [11, 11],
  "steps": 17
}
```

An eval row derived from a stream still resolves to one deterministic seed
instance. For train and eval streams, `base_rng` defines a deterministic
sequence of episode seeds:

```text
episode_rng = splitmix64(base_rng, episode_index)
```

`vocab.json` is also a recipe. It records alphabet offsets, special-token ids,
and dataset-to-alphabet ids. Runtime code reconstructs expanded maps such as
`token_to_id` or `value_to_id` in memory when needed.

PE caches follow the same explicit-source principle. Training caches are built
from the training position sets. Invariance and OOD eval caches extend those
sets with transformed or larger-horizon/scale coordinates, without retraining
the model.

Rule/example filtering is a runtime responsibility of `batch.py`, because a
rule's usefulness depends on the seed and generated rollout.

## Dependency Chain

The intended dependency direction is one-way:

```text
loci.py
  -> neighborhoods.py
  -> frontiers.py
  -> seeds.py

alphabets.py
  -> rules.py

alphabets.py
  -> tokenize.py

alphabets.py + seeds.py + neighborhoods.py + frontiers.py + rules.py
  -> datasets.py

configs + datasets.py + evals.py
  -> prepare.py
  -> source manifests + stream specs + vocab artifacts

source manifests + stream specs + vocab artifacts
  -> batch.py
  -> generate.py
  -> tokenize.py
  -> train.py / eval.py

pe.py
  -> model.py
  -> train.py / eval.py
```

The short rule is:

```text
prepare.py freezes deterministic sources
batch.py realizes examples from those sources
generate.py rolls one seed state forward
tokenize.py turns one realized episode into model representation
pe.py builds and applies cached PE factors from explicit position ids
```

## Repository Directory

Target structure:

```text
.
├── data
│   ├── components
│   │   ├── loci.py
│   │   ├── alphabets.py
│   │   ├── neighborhoods.py
│   │   ├── frontiers.py
│   │   ├── seeds.py
│   │   ├── rules.py
│   │   ├── datasets.py
│   │   └── evals.py
│   ├── datasets
│   │   ├── 0d-ar2-97
│   │   ├── 1d-dyadrads
│   │   ├── 2d-dyadaxes
│   │   └── 3d-dyadaxes
│   ├── generate.py
│   ├── tokenize.py
│   ├── batch.py
│   └── eval.py
├── configs
│   ├── v1-multi.json
│   ├── v1-t+0d.json
│   ├── v1-t+1d.json
│   ├── v1-t+2d.json
│   └── v1-t+3d.json
├── model.py
├── pe.py
├── prepare.py
├── train.py
└── README.md
```
