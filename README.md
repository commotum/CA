# ankos

`ankos` is a Python project for exploring cellular automata and other simple
programs in the spirit of *A New Kind of Science*. The import package is `ca`.

The central idea is direct experimentation: choose a simple rule, choose an
initial condition, run the system, and study the trajectory that appears.
Simple programs can settle into repetition, form nested structure, generate
apparent randomness, or support localized interactions. `ankos` provides the
small trajectory generator needed to run those experiments reproducibly.

## Project Layout

```text
ankos
|-- src/ca                         Python package
|-- tests                          package tests
|-- ref/A-New-Kind-of-Science       book source and ANKoS atlas
|-- ref/notes/generator.md          trajectory generator schema
|-- pyproject.toml
`-- README.md
```

The atlas at `ref/A-New-Kind-of-Science/ANKoS-Atlas.md` summarizes the book's
arc: complexity from simple rules, behavior classes, randomness generation,
self-organization, universality, computational irreducibility, and simple
programs as explanatory models.

The generator schema at `ref/notes/generator.md` defines the coordinate and
update model used by the package.

## Trajectory Model

A generated episode is a full-state trajectory over canonical coordinates:

```text
[t, x, y, z]
```

The same coordinate form covers scalar, one-dimensional, two-dimensional, and
three-dimensional systems:

```text
t+0D: [t, 0, 0, 0]
t+1D: [t, x, 0, 0]
t+2D: [t, x, y, 0]
t+3D: [t, x, y, z]
```

At each update time, a frontier selects update sites in the current state.
Neighborhoods read relative offsets around each selected site. A rule maps
those reads to the value written at the corresponding next-time coordinate.

For ordinary cellular automata, neighborhoods read the current state and write
the next one:

```text
state at t -> state at t + 1
```

Temporal recurrences can also read earlier source times such as `t - 1`.

## The `ca` Package

```text
src/ca
|-- loci.py            canonical coordinates, selectors, masks, and gathering
|-- alphabets.py       finite value spaces
|-- seeds.py           initial-state seed families and rendering
|-- neighborhoods.py   read stencils built from selectors
|-- frontiers.py       update-site frontiers
|-- rules.py           rule channels and named rule families
|-- rollout.py         NumPy trajectory rollout
|-- specs.py           manifest loading and result dataclasses
|-- rng.py             reproducible NumPy RNG helpers
`-- __init__.py        public exports
```

The usual Python flow is:

```text
ca.Dynamics + rule_id + seed_state + steps
    -> ca.rollout(...)
    -> ca.RawEpisode
```

`ca.Dynamics` describes the reusable system:

- `domain`: `t+0d`, `t+1d`, `t+2d`, or `t+3d`
- `shape`: native spatial shape
- `rule`: a rule family
- `neighborhoods`: read stencils for the rule
- `frontier`: an update-site frontier
- `boundary`: spatial read behavior
- `metadata`: optional metadata copied into the result

`ca.RawEpisode` contains the raw NumPy `states`, optional flattened
coordinates, and the episode metadata.

## Quick Start

Install dependencies from the repository root:

```bash
uv sync
```

Roll a scalar second-order modular recurrence:

```python
import numpy as np

import ca

dynamics = ca.Dynamics(
    domain="t+0d",
    shape=(),
    rule=ca.ar2_modular_0d(modulus=97),
    neighborhoods=(),
    frontier=ca.time_slice(()),
)

episode = ca.rollout(
    dynamics=dynamics,
    rule_id=0,
    seed_state=np.array([1, 2]),
    steps=4,
)

print(episode.states.tolist())
# [2, 3, 4, 5]
```

Roll a two-dimensional Dyadaxes system:

```python
import numpy as np

import ca

dynamics = ca.Dynamics(
    domain="t+2d",
    shape=(3, 3),
    rule=ca.dyadaxes_2d_rule(),
    neighborhoods=(ca.dyadaxes_2d_neighborhood(),),
    frontier=ca.time_slice((3, 3)),
    boundary={"policy": "fixed", "value": 0},
)

seed_state = np.array(
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    dtype=np.int64,
)

episode = ca.rollout(dynamics, rule_id=0, seed_state=seed_state, steps=2)

print(episode.states.shape)
# (2, 3, 3)
```

Load dynamics from a manifest:

```python
import numpy as np

import ca

manifest = {
    "dataset_id": "2d-dyadaxes",
    "manifest_version": "v1",
    "domain": "t+2d",
    "shape": [3, 3],
    "dynamics": {
        "neighborhood": {"family": "dyadaxes_2d"},
        "frontier": {"family": "time_slice"},
        "rule": {"family": "dyadaxes_2d"},
        "boundary": {"policy": "fixed", "value": 0},
    },
}

dynamics = ca.dynamics_from_spec(manifest)
seed_state = np.ones((3, 3), dtype=np.int64)
episode = ca.rollout(dynamics, rule_id=0, seed_state=seed_state, steps=2)
```

## Coordinates And Shapes

Spatial axes are centered by default. For example:

```text
shape (3,) -> x = -1, 0, 1
shape (4,) -> x = -1, 0, 1, 2
```

Native state arrays keep their natural rank:

```text
t+0d: (steps,)
t+1d: (steps, x)
t+2d: (steps, x, y)
t+3d: (steps, x, y, z)
```

Use `ca.canonical_coords(domain, shape, steps)` to create the flattened
`[t, x, y, z]` table for an episode.

## Built-In Families

Rules:

- `ar2_modular_0d`: second-order modular scalar recurrence
- `dyadrads_1d`: binary lookup over self, radius-1 activity, and radius-2
  activity
- `dyadaxes_2d`: binary lookup over self, cardinal-neighbor majority, and
  diagonal-neighbor majority
- `dyadaxes_3d`: binary lookup over self, face-neighbor majority, and
  edge/corner activity

Neighborhoods:

- Basic stencils: `self_at`, `literal_offsets`, `metric_radius`, `shell`,
  `axis_shell`, `l1_shell`, `change_count_shell`, `directional_line`,
  `directional_fov`
- Common CA aliases: `eca`, `moore`, `von_neumann`, `history`
- Compounds: `ar2_0d`, `dyadrads_1d`, `dyadaxes_2d`, `dyadaxes_3d`

Seeds:

- Scalar and simple seeds: `pair`, `uniform_pair`, `constant`, `point`,
  `bernoulli`, `selector_seed`
- Structured supports: `subspace`, `finite_segment`, `body`, `compound`,
  `region`, `periodic`, `path`, `transform`, `structured`

Alphabets:

- `int_range_alphabet`
- `float_range_alphabet`
- `boolean`
- `symbolic`

Boundary policies:

```python
{"policy": "none"}
{"policy": "fixed", "value": 0}
{"policy": "periodic"}
{"policy": "reflective"}
```

## Reproducible Seeds

Use `ca.rng` to derive NumPy generators for stochastic seed rendering:

```python
import ca

rng = ca.numpy_rng({"policy": "splitmix64", "base_rng": 12345}, episode_index=7)
seed_state = ca.render(ca.bernoulli(p_low=0.5, p_high=0.5), shape=(16,), rng=rng)
```

Pass the rendered `seed_state` to `ca.rollout(...)`.

## Development

Run tests:

```bash
uv run pytest
```
