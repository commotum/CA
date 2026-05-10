# Refactor Target

This document is the normalized target layout for the ankos repo:

- `ankos`: standalone cellular-automata library and research references.

## Naming Rules

- Use `ankos` as the repo-root name in tree views.
- Use `ca` only for the Python import package.
- Use `README.md` for the repo root.
- Keep reference material under the top-level `ref` directory.
- Keep research notes under `ref/notes`.
- Keep archived planning docs under `ref/notes/archived`.
- Keep uv reference docs under `ref/uv-docs`.
- Keep the NKS source as `ref/A-New-Kind-of-Science`.
  Preserve its `FRONT-MATTER`, `CHAPTERS`, and `BACK-MATTER` layout.

## ankos

### High-Level View

```text
ankos
├── src
│   └── ca
├── ref
├── tests
├── pyproject.toml
├── uv.lock
└── README.md
```

### Package View

```text
ankos
└── src
    └── ca
        ├── __init__.py
        ├── py.typed
        ├── specs.py
        ├── loci.py
        ├── alphabets.py
        ├── neighborhoods.py
        ├── frontiers.py
        ├── seeds.py
        ├── rules.py
        ├── rng.py
        └── rollout.py
```

### Ref View

```text
ankos
└── ref
    ├── roadmap
    ├── notes
    │   ├── CA-Types.csv
    │   ├── CA-Types.md
    │   ├── generator.md
    │   └── archived
    │       ├── V2.md
    │       ├── generator.md
    │       └── repo-plan.md
    ├── uv-docs
    └── A-New-Kind-of-Science
        ├── FRONT-MATTER
        ├── CHAPTERS
        ├── BACK-MATTER
        └── A New Kind of Science.md
```

### Test View

```text
ankos
└── tests
    ├── test_loci.py
    ├── test_rng.py
    ├── test_rules.py
    ├── test_seeds.py
    └── test_rollout.py
```

### Expanded View

```text
ankos
├── ref
│   ├── notes
│   │   ├── CA-Types.csv
│   │   ├── CA-Types.md
│   │   ├── generator.md
│   │   └── archived
│   │       ├── V2.md
│   │       ├── generator.md
│   │       └── repo-plan.md
│   ├── uv-docs
│   └── A-New-Kind-of-Science
│       ├── FRONT-MATTER
│       │   ├── Contents
│       │   │   └── Contents.md
│       │   └── Preface
│       │       └── Preface.md
│       ├── CHAPTERS
│       │   ├── 1-The-Foundations-for-a-New-Kind-of-Science
│       │   │   └── 1-The-Foundations-for-a-New-Kind-of-Science.md
│       │   ├── 2-The-Crucial-Experiment
│       │   │   └── 2-The-Crucial-Experiment.md
│       │   ├── 3-The-World-of-Simple-Programs
│       │   │   └── 3-The-World-of-Simple-Programs.md
│       │   ├── 4-Systems-Based-on-Numbers
│       │   │   └── 4-Systems-Based-on-Numbers.md
│       │   ├── 5-Two-Dimensions-and-Beyond
│       │   │   └── 5-Two-Dimensions-and-Beyond.md
│       │   ├── 6-Starting-from-Randomness
│       │   │   └── 6-Starting-from-Randomness.md
│       │   ├── 7-Mechanisms-in-Programs-and-Nature
│       │   │   └── 7-Mechanisms-in-Programs-and-Nature.md
│       │   ├── 8-Implications-for-Everyday-Systems
│       │   │   └── 8-Implications-for-Everyday-Systems.md
│       │   ├── 9-Fundamental-Physics
│       │   │   └── 9-Fundamental-Physics.md
│       │   ├── 10-Processes-of-Perception-and-Analysis
│       │   │   └── 10-Processes-of-Perception-and-Analysis.md
│       │   ├── 11-The-Notion-of-Computation
│       │   │   └── 11-The-Notion-of-Computation.md
│       │   └── 12-The-Principle-of-Computational-Equivalence
│       │       └── 12-The-Principle-of-Computational-Equivalence.md
│       ├── BACK-MATTER
│       │   ├── Colophon
│       │   │   └── Colophon.md
│       │   ├── Index
│       │   │   └── Index.md
│       │   └── Notes
│       │       └── Notes.md
│       └── A New Kind of Science.md
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
│       ├── rng.py
│       └── rollout.py
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
