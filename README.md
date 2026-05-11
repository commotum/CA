# ankos

ANKoS ("A New Kind of Science") is a Python project for running
cellular-automaton experiments inspired by Wolfram's book. Import it as `ca`.

The aim is one construction API for many CA families: elementary, multi-color,
totalistic, two-dimensional, three-dimensional, and continuous. These systems
vary by dimension, geometry, alphabet, neighborhood, rule form, update schedule,
boundary, and seed, but share a common spine:

```text
domain:        the spacetime dimension of the automaton
shape:         the finite extent of the run
alphabet:      the possible cell states
seed:          the initial state
boundary:      the edge convention for neighborhood reads
frontier:      the cells updated at the next step
neighborhood:  what each active cell reads
rule:          how reads become the next state
```

The package implements fixed-grid trajectory generation.

## Model

An episode is a full-state trajectory over canonical coordinates:

```text
[t, x, y, z]
```

The same address covers scalar through three-dimensional systems:

```text
t+0D: [t, 0, 0, 0]
t+1D: [t, x, 0, 0]
t+2D: [t, x, y, 0]
t+3D: [t, x, y, z]
```

ANKoS follows Wolfram's next-state convention: state `t` is present in the
trajectory; the rule reads it and writes `t + 1`.

```text
state t -> state t + 1
```

At each update time, a frontier selects current-state sites, neighborhoods read
relative offsets around those sites, and a rule writes next-state values.
Temporal recurrences may also read earlier source times such as `t - 1`.

## API

```text
ca.Dynamics + rule_id + seed_state + steps
    -> ca.rollout(...)
    -> ca.RawEpisode
```

`ca.Dynamics` describes the system:

- `domain`: `t+0d`, `t+1d`, `t+2d`, or `t+3d`
- `shape`: native spatial shape
- `rule`: rule family
- `neighborhoods`: read stencils
- `frontier`: update-site selector
- `boundary`: spatial read behavior
- `metadata`: optional result metadata

`ca.RawEpisode` returns `states`, coordinates, and episode metadata.

Package modules:

```text
src/ca
|-- loci.py            coordinates, selectors, masks, gathering
|-- alphabets.py       finite value spaces
|-- seeds.py           seed specs and rendering
|-- neighborhoods.py   read stencils
|-- frontiers.py       update-site selectors
|-- rules.py           rule channels and families
|-- rollout.py         NumPy rollout
|-- specs.py           manifests and result types
|-- rng.py             reproducible RNG helpers
`-- __init__.py        public exports
```

## Quick Start

Install dependencies:

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

## Coordinates

Spatial axes are centered:

```text
shape (3,) -> x = -1, 0, 1
shape (4,) -> x = -1, 0, 1, 2
```

State arrays keep native rank:

```text
t+0d: (steps,)
t+1d: (steps, x)
t+2d: (steps, x, y)
t+3d: (steps, x, y, z)
```

Use `ca.canonical_coords(domain, shape, steps)` for the flattened
`[t, x, y, z]` table.

## Built-Ins

Rules:

- `ar2_modular_0d`
- `dyadrads_1d`
- `dyadaxes_2d`
- `dyadaxes_3d`

Neighborhoods:

- `self_at`, `literal_offsets`, `metric_radius`, `shell`, `axis_shell`
- `l1_shell`, `change_count_shell`, `directional_line`, `directional_fov`
- `eca`, `moore`, `von_neumann`, `history`
- `ar2_0d`, `dyadrads_1d`, `dyadaxes_2d`, `dyadaxes_3d`

Seeds:

- `pair`, `uniform_pair`, `constant`, `point`, `bernoulli`, `selector_seed`
- `subspace`, `finite_segment`, `body`, `compound`, `region`, `periodic`
- `path`, `transform`, `structured`

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

## References

```text
ref/A-New-Kind-of-Science/ANKoS-Atlas.md  book atlas and chapter map
ref/notes/CA-Types.md                     construction taxonomy
ref/notes/generator.md                    trajectory generator schema
```

## Development

```bash
uv run pytest
```
