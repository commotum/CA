# PE Target

This document describes the PE repo target layout using the normalized file
and directory names from `context/REFACTOR_TARGET.md`.

## Major Branches

### `pe/`

`pe/` is the top-level positional-encoding experiment repo. It studies
transformers as next-state predictors over generated cellular-automata and
scalar recurrence streams. The repo is organized around a compact causal-model
core: configs define experiments, data branches define streamable training and
evaluation contents, components implement reusable model/training primitives,
`model.py` composes those primitives into a transformer, and `train.py`
orchestrates runs. Raw CA mechanics come from the external `ankos` repo via the
`ca` import package.

### `configs/`

`configs/` contains one Python config file per experiment family:

- `configs/t0d.py`
- `configs/t1d.py`
- `configs/t2d.py`
- `configs/t3d.py`
- `configs/multi.py`

Each config declares the dataset ids, positional encoders, model depth, token
budget, split policy, evaluation plan, and any sweep variables needed for a
run. Config files should be simple Python assignment modules in the nanoGPT
style. They should not implement model internals, dataset generation,
tokenization, batching, optimizer algorithms, or checkpoint IO.

Family mapping:

- `configs/t0d.py` uses `data/0d-ar2-97/`
- `configs/t1d.py` uses `data/1d-dyadrads/`
- `configs/t2d.py` uses `data/2d-dyadaxes/`
- `configs/t3d.py` uses `data/3d-dyadaxes/`
- `configs/multi.py` uses all four dataset branches

### `data/`

`data/` contains dataset branches and shared dataset registry/build logic. The
dataset branch names are fixed lowercase hyphen slugs:

- `data/0d-ar2-97/`
- `data/1d-dyadrads/`
- `data/2d-dyadaxes/`
- `data/3d-dyadaxes/`

Each dataset branch should expose prepared-source metadata, a preparation
script, and a human-facing doc. These branches represent generated and streamed
procedural training contents rather than downloaded text corpora. They describe
CA sources; reusable CA primitives and raw rollout live in `ankos/src/ca`.

### `ckpts/`

`ckpts/` contains exported checkpoint groups by experiment family:

- `ckpts/t0d/`
- `ckpts/t1d/`
- `ckpts/t2d/`
- `ckpts/t3d/`
- `ckpts/multi/`

Each group contains a `ckpts/` subfolder for `.pt` files and a lowercase
`readme.md` describing the checkpoint group. This is the export shelf for
evaluation and sharing, not the internal training-run checkpoint layout.
Exported artifacts should follow the normalized checkpoint names from
`REFACTOR_TARGET.md`.

### `components/`

`components/` contains reusable implementation pieces used by the model,
configs, training loop, evaluation loop, and checkpointing utilities:

- `components/attention.py`
- `components/posenc.py`
- `components/optimizer.py`
- `components/tokenizer.py`
- `components/evals.py`
- `components/checkpoint.py`
- `components/batch.py`

The goal is to keep each experimental axis independently swappable without
turning the repo into a heavyweight framework.

## Data Branch Pattern

### `data/<dataset>/`

Each `data/<dataset>/` branch represents one prepared or preparable procedural
source. The rest of the repo should interact with it through shared dataset and
batch interfaces, so the model and training loop do not need to know how the
underlying episodes are produced.

### `data/<dataset>/manifest/`

`data/<dataset>/manifest/` contains the machine-readable metadata for a dataset
branch:

- `manifest.json`
- `vocab.json`
- `rule_pools.json`
- `train_streams.json`
- `eval_streams.json`

These files record vocabulary information, stream definitions, rule pools,
split metadata, CA world/source identity, and other structured assets needed by
dataset `prepare.py`, `data/datasets.py`, `components/tokenizer.py`, and
`components/batch.py`.

### `data/<dataset>/prepare.py`

`data/<dataset>/prepare.py` builds or verifies one dataset branch. It should
create or validate the manifest artifacts and leave the dataset in a
ready-to-stream state. It should not train models or implement model-facing
batch construction.

### `data/<dataset>/readme.md`

`data/<dataset>/readme.md` is the human-facing description of a dataset branch.
It should explain what the dataset is for, how to prepare it, what streams it
exposes, and which experiment families normally use it. Machine-readable
training metadata belongs in `manifest/*.json`, not in this file.

### `data/datasets.py`

`data/datasets.py` is the shared dataset registry and preparation orchestrator.
It should know which dataset branches exist, how to check whether they are
prepared, how to invoke each branch's `prepare.py`, and how to return stream
descriptors to configs and batch builders. It should not own raw CA mechanics,
model-facing tokenization, or tensor batch collation.

## Checkpoint Pattern

### `ckpts/<experiment>/`

Each `ckpts/<experiment>/` directory groups exported model artifacts for one
experiment family. Valid experiment directory names are:

- `t0d`
- `t1d`
- `t2d`
- `t3d`
- `multi`

The group should contain enough structure to make evaluation, sampling, and
comparison reproducible without forcing metadata into checkpoint filenames.

### `ckpts/<experiment>/ckpts/`

`ckpts/<experiment>/ckpts/` stores exported `.pt` artifacts. Normalized
filenames are shaped as `{experiment}_{pe}.pt`, for example:

- `ckpts/t0d/ckpts/t0d_rope.pt`
- `ckpts/t0d/ckpts/t0d_axial4d.pt`
- `ckpts/t0d/ckpts/t0d_monster.pt`
- `ckpts/t1d/ckpts/t1d_axial2d.pt`
- `ckpts/t2d/ckpts/t2d_axial3d.pt`
- `ckpts/multi/ckpts/multi_monster.pt`

These exported files are separate from training-run checkpoints. They may be
weight-only exports loaded by `components/checkpoint.py`, while richer resume
state remains in the run directory.

### Training-Run Checkpoints

`components/checkpoint.py` writes resumable run checkpoints under a run
directory:

```text
run_dir/checkpoints/step_000500/
├── model.pt
├── optim_rank0.pt
├── train_state_rank0.pt
└── meta.json
```

Named pointers such as `latest.json` and `best_val.json` live under
`run_dir/checkpoints/`. The metadata records run identity, domain, PE method,
model/training config, data hashes, PE-cache spec hashes, metrics, and step
counts.

### `ckpts/<experiment>/readme.md`

`ckpts/<experiment>/readme.md` documents the checkpoint group. It should
summarize which config produced the artifacts, what variables were compared,
which datasets were used, which checkpoints matter, and what evaluation results
or qualitative observations distinguish the runs.

## Component Files

### `components/attention.py`

`components/attention.py` implements attention execution and mask handling. It
owns how queries, keys, and values are routed, what each token is allowed to
attend to, and which backend executes the operation. Positional encoding should
remain separate except where attention receives already-positioned Q/K tensors
or mask instructions. The first PE target consumes dense state-causal masks.

### `components/posenc.py`

`components/posenc.py` implements positional-encoding methods as
interchangeable modules. It should cover RoPE, axial RoPE, MonSTER, and future
methods being tested. It owns explicit-position cache construction,
layout-keyed cache bundles, and cached Q/K position encoding. It should not
decide sequence order or dataset semantics.

### `components/optimizer.py`

`components/optimizer.py` owns optimizer construction, parameter grouping, and
optimizer-specific runtime policy. The model may identify parameter roles, but
this component translates those roles into optimizer instances and update
behavior.

### `components/tokenizer.py`

`components/tokenizer.py` defines the boundary between generated procedural
contents and integer token sequences. It should provide vocabulary handling,
special-token handling, canonical sequence construction, model-facing
`[t,x,y,z]` coordinates, position ids, layout/domain ids, next-state targets,
and metadata needed by `components/batch.py` and `components/evals.py`.

### `components/evals.py`

`components/evals.py` contains reusable evaluation routines for training-time
validation and standalone model assessment. Metrics should be designed around
the procedural next-state prediction experiments, including OOD and invariance
comparisons, rather than inherited text-only metrics.

### `components/checkpoint.py`

`components/checkpoint.py` owns checkpoint persistence and loading helpers. It
should handle model state, metadata, optimizer state, training state, checkpoint
pointers, RNG state helpers, compile-prefix cleanup, and weight-only loading.
It does not build the model, tokenizer, PE caches, or data streams.

### `components/batch.py`

`components/batch.py` turns prepared or generated dataset streams into
model-ready training batches. It should read prepared train/eval stream specs,
derive episode RNGs, select rule ids from prepared pools, render CA seeds, call
`ca.rollout()`, invoke `components/tokenizer.py`, build dense state-causal
masks, collate coordinates/position ids/cache-layout ids, and move tensors
efficiently.

## Root Files

### `model.py`

`model.py` defines the composable transformer model. It assembles token
embeddings, attention blocks, MLPs, normalization, output heads, and
parameter-role metadata needed by the optimizer. Each model has one PE method;
single-domain models use one cache, while multi-domain models use a
same-method cache bundle selected by layout id.

### `train.py`

`train.py` is the main CLI entrypoint for running experiments. It accepts a
config from `configs/`, ensures required datasets are prepared, instantiates
the tokenizer, batch streams, PE cache bundle, model, optimizer, evaluator, and
checkpoint paths, then runs the training loop.

### `eval.py`

`eval.py` is the standalone evaluation entrypoint for trained checkpoints. It
loads a checkpoint from `ckpts/` or another checkpoint path, reconstructs the
needed config, tokenizer, batch/eval streams, PE caches, and components, runs
evaluation routines from
`components/evals.py`, and reports comparable metrics.

### `README.md`

`README.md` is the top-level project guide. It explains the purpose of the
repo, how configs define experiments, how dataset branches are prepared, how to
launch training, how to evaluate checkpoints, and how `components/`, `data/`,
`configs/`, and `ckpts/` fit together.
