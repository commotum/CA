Yes. `rollout.py` is basically the standalone CA-package version of the old `data/generate.py`.

The rename is meant to make the responsibility clearer:

```text
generate.py  old repo-local name
rollout.py   CA-library name for “evolve this world forward”
```

In the current repo, `data/generate.py` already does the raw next-state evolution: it takes a dataset spec, initial state, rule id, shape, boundary, and step count; rolls raw states; creates canonical coordinates; and returns an `Episode`. The atlas describes it as “deterministic raw next-state rollout from a chosen dataset spec, initial state, and rule id.” 

So in the external CA package:

```text
ca_lattice/rollout.py
```

would contain the cleaned-up version of:

```text
data/generate.py
```

## What `rollout.py` should do

It should answer:

```text
Given a CA world, seed state, rule id, and step count,
what raw trajectory does this world produce?
```

Concretely:

```python
episode = rollout(
    world=world_spec,
    rule_id=rule_id,
    seed_state=seed_state,
    steps=17,
)
```

And return something raw/model-agnostic:

```python
RawEpisode(
    domain="t+2d",
    shape=(11, 11),
    rule_id=42,
    steps=17,
    states=states,   # raw generated values
    coords=coords,   # canonical [t, x, y, z]
    metadata={...},
)
```

## What it should contain from old `generate.py`

Move these concepts over:

```text
Episode / RawEpisode dataclass
generate_episode / rollout
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

The current `data/generate.py` already has those responsibilities: dispatching by rule family, rolling AR2 scalar sequences, rolling spatial lookup rules synchronously, reading neighborhood components, reducing channels, applying gates, and packing lookup indices. 

## What should change during the move

The important cleanup is that old `generate.py` currently accepts a `frontier` argument but ignores it; all spatial rules update full states synchronously. 

In the new `rollout.py`, make that explicit:

```python
if world.frontier.family != "full_next_slice":
    raise NotImplementedError(
        "ca_lattice Phase 1 supports only full_next_slice rollout"
    )
```

So instead of silently pretending to support arbitrary frontiers, Phase 1 says:

```text
Only full-next-slice synchronous rollout is executable right now.
```

That matches your choice to keep `frontiers.py` but expose only `FullNextSlice`.

## What `rollout.py` should not do

It should not do anything model-facing:

```text
token ids
BOS/domain tokens
position ids
layout ids
attention masks
loss masks
batch padding
train/eval split selection
held-out-rule policies
PE cache building
```

Those belong in `pe/data/datasets.py`, dataset `prepare.py` files, `posenc/`, or the experiment runner.

So the boundary is:

```text
ca_lattice/rollout.py
  raw world evolution

pe/data/datasets.py
  serialize raw episodes into training examples

posenc/posenc.py
  turn explicit coords into q/k PE factors

posenc/flashmask.py
  build masks / run attention
```

In short: **yes, `rollout.py` is the cleaned-up external-library successor to `data/generate.py`.**
