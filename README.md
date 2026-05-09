# Refactor Target

This document is the normalized target layout for the two repos:

- `pe`: positional-encoding experiment repo. It consumes CA primitives and
  writes transformer-ready data, checkpoints, and evaluation artifacts.
- `CA`: standalone cellular-automata library and research notes.

## Naming Rules

- Use `CA` and `pe` as repo-root names in tree views.
- Use `ca_lattice` only for the CA Python import package.
- Use `README.md` for repo roots. Use `readme.md` for PE dataset and
  checkpoint entry docs as shown in the target tree.
- Use lowercase hyphen slugs for datasets and notes: `0d-ar2-97`,
  `ca-types.md`, `repo-plan.md`.
- Keep the NKS source as a top-level `A-New-Kind-of-Science` directory.
  Preserve its `FRONT-MATTER`, `CHAPTERS`, and `BACK-MATTER` layout.
- Use PE config filenames: `t0d.py`, `t1d.py`, `t2d.py`, `t3d.py`,
  `multi.py`.
- Use root `ckpts` for PE checkpoint groups, with experiment directories
  `t0d`, `t1d`, `t2d`, `t3d`, and `multi`.
- Use checkpoint filenames shaped as `{experiment}_{pe}.pt`, for example
  `t2d_axial3d.pt` and `multi_monster.pt`.

## PE

### High-Level View

```text
pe
├── configs
├── data
├── ckpts
├── components
├── model.py
├── train.py
├── eval.py
└── README.md
```

### Components View

```text
pe
├── configs
├── data
├── ckpts
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

### Configs View

```text
pe
├── configs
│   ├── t0d.py
│   ├── t1d.py
│   ├── t2d.py
│   ├── t3d.py
│   └── multi.py
├── data
├── ckpts
├── components
├── model.py
├── train.py
├── eval.py
└── README.md
```

### Data View

```text
pe
├── configs
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
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   ├── 2d-dyadaxes
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   ├── 3d-dyadaxes
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   └── datasets.py
├── ckpts
├── components
├── model.py
├── train.py
├── eval.py
└── README.md
```

### CKPTs View

```text
pe
├── configs
├── data
├── ckpts
│   ├── t0d
│   │   ├── ckpts
│   │   │   ├── t0d_rope.pt
│   │   │   ├── t0d_axial4d.pt
│   │   │   └── t0d_monster.pt
│   │   └── readme.md
│   ├── t1d
│   │   ├── ckpts
│   │   │   ├── t1d_rope.pt
│   │   │   ├── t1d_axial2d.pt
│   │   │   ├── t1d_axial4d.pt
│   │   │   └── t1d_monster.pt
│   │   └── readme.md
│   ├── t2d
│   │   ├── ckpts
│   │   │   ├── t2d_rope.pt
│   │   │   ├── t2d_axial3d.pt
│   │   │   ├── t2d_axial4d.pt
│   │   │   └── t2d_monster.pt
│   │   └── readme.md
│   ├── t3d
│   │   ├── ckpts
│   │   │   ├── t3d_rope.pt
│   │   │   ├── t3d_axial4d.pt
│   │   │   └── t3d_monster.pt
│   │   └── readme.md
│   └── multi
│       ├── ckpts
│       │   ├── multi_rope.pt
│       │   ├── multi_axial4d.pt
│       │   └── multi_monster.pt
│       └── readme.md
├── components
├── model.py
├── train.py
├── eval.py
└── README.md
```

### Expanded View

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
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   ├── 2d-dyadaxes
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   ├── 3d-dyadaxes
│   │   ├── manifest
│   │   │   ├── manifest.json
│   │   │   ├── vocab.json
│   │   │   ├── rule_pools.json
│   │   │   ├── train_streams.json
│   │   │   └── eval_streams.json
│   │   ├── prepare.py
│   │   └── readme.md
│   └── datasets.py
├── ckpts
│   ├── t0d
│   │   ├── ckpts
│   │   │   ├── t0d_rope.pt
│   │   │   ├── t0d_axial4d.pt
│   │   │   └── t0d_monster.pt
│   │   └── readme.md
│   ├── t1d
│   │   ├── ckpts
│   │   │   ├── t1d_rope.pt
│   │   │   ├── t1d_axial2d.pt
│   │   │   ├── t1d_axial4d.pt
│   │   │   └── t1d_monster.pt
│   │   └── readme.md
│   ├── t2d
│   │   ├── ckpts
│   │   │   ├── t2d_rope.pt
│   │   │   ├── t2d_axial3d.pt
│   │   │   ├── t2d_axial4d.pt
│   │   │   └── t2d_monster.pt
│   │   └── readme.md
│   ├── t3d
│   │   ├── ckpts
│   │   │   ├── t3d_rope.pt
│   │   │   ├── t3d_axial4d.pt
│   │   │   └── t3d_monster.pt
│   │   └── readme.md
│   └── multi
│       ├── ckpts
│       │   ├── multi_rope.pt
│       │   ├── multi_axial4d.pt
│       │   └── multi_monster.pt
│       └── readme.md
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

## CA

### High-Level View

```text
CA
├── A-New-Kind-of-Science
├── ca_lattice
├── notes
├── tests
├── pyproject.toml
├── uv.lock
└── README.md
```

### Package View

```text
CA
└── ca_lattice
    ├── __init__.py
    ├── specs.py
    ├── loci.py
    ├── alphabets.py
    ├── neighborhoods.py
    ├── frontiers.py
    ├── seeds.py
    ├── rules.py
    ├── boundary.py
    ├── rng.py
    └── rollout.py
```

### Notes And Book View

```text
CA
├── notes
│   ├── ca-types.csv
│   ├── ca-types.md
│   ├── generator.md
│   ├── v2.md
│   └── repo-plan.md
└── A-New-Kind-of-Science
    ├── FRONT-MATTER
    ├── CHAPTERS
    ├── BACK-MATTER
    └── A New Kind of Science.md
```

### Test View

```text
CA
└── tests
    ├── test_loci.py
    ├── test_rng.py
    ├── test_rules.py
    ├── test_seeds.py
    └── test_rollout.py
```

### Expanded View

```text
CA
├── A-New-Kind-of-Science
│   ├── FRONT-MATTER
│   │   ├── Contents
│   │   │   └── Contents.md
│   │   └── Preface
│   │       └── Preface.md
│   ├── CHAPTERS
│   │   ├── 1-The-Foundations-for-a-New-Kind-of-Science
│   │   │   └── 1-The-Foundations-for-a-New-Kind-of-Science.md
│   │   ├── 2-The-Crucial-Experiment
│   │   │   └── 2-The-Crucial-Experiment.md
│   │   ├── 3-The-World-of-Simple-Programs
│   │   │   └── 3-The-World-of-Simple-Programs.md
│   │   ├── 4-Systems-Based-on-Numbers
│   │   │   └── 4-Systems-Based-on-Numbers.md
│   │   ├── 5-Two-Dimensions-and-Beyond
│   │   │   └── 5-Two-Dimensions-and-Beyond.md
│   │   ├── 6-Starting-from-Randomness
│   │   │   └── 6-Starting-from-Randomness.md
│   │   ├── 7-Mechanisms-in-Programs-and-Nature
│   │   │   └── 7-Mechanisms-in-Programs-and-Nature.md
│   │   ├── 8-Implications-for-Everyday-Systems
│   │   │   └── 8-Implications-for-Everyday-Systems.md
│   │   ├── 9-Fundamental-Physics
│   │   │   └── 9-Fundamental-Physics.md
│   │   ├── 10-Processes-of-Perception-and-Analysis
│   │   │   └── 10-Processes-of-Perception-and-Analysis.md
│   │   ├── 11-The-Notion-of-Computation
│   │   │   └── 11-The-Notion-of-Computation.md
│   │   └── 12-The-Principle-of-Computational-Equivalence
│   │       └── 12-The-Principle-of-Computational-Equivalence.md
│   ├── BACK-MATTER
│   │   ├── Colophon
│   │   │   └── Colophon.md
│   │   ├── Index
│   │   │   └── Index.md
│   │   └── Notes
│   │       └── Notes.md
│   └── A New Kind of Science.md
├── notes
│   ├── ca-types.csv
│   ├── ca-types.md
│   ├── generator.md
│   ├── v2.md
│   └── repo-plan.md
├── ca_lattice
│   ├── __init__.py
│   ├── specs.py
│   ├── loci.py
│   ├── alphabets.py
│   ├── neighborhoods.py
│   ├── frontiers.py
│   ├── seeds.py
│   ├── rules.py
│   ├── boundary.py
│   ├── rng.py
│   └── rollout.py
├── tests
│   ├── test_loci.py
│   ├── test_rng.py
│   ├── test_rules.py
│   ├── test_seeds.py
│   └── test_rollout.py
├── pyproject.toml
├── uv.lock
└── README.md
```
