# CA Repository Plan

CA should be a standalone simple-programs and cellular-automata research library. It should generate semantic trajectories from explicit system specifications, while downstream libraries such as `pe` decide how to serialize those trajectories for transformers, GPU batches, positional encoders, and loss masks.

The clean architecture split is:

```text
1. Primitives
2. Catalog / Registry
3. Builders / Presets
4. Generators
```

## 1. Primitives

Primitives are the programmable pieces from which systems are constructed.

Examples:

```text
Rule
Neighborhood
Frontier
Boundary
Seed
Schedule
Domain
Alphabet
```

Users should be able to use built-in primitives or write their own Python implementations.

The generator should not care whether a primitive came from the built-in catalog, a saved preset, or a custom user module. It should only consume a resolved specification.

## 2. Catalog / Registry

The catalog is the built-in library of widely used defaults.

Examples:

```text
ca.catalog.neighborhoods.moore_2d
ca.catalog.neighborhoods.von_neumann_3d
ca.catalog.neighborhoods.previous_self
ca.catalog.frontiers.full_next_slice
ca.catalog.rules.elementary_1d
ca.catalog.rules.totalistic
ca.catalog.rules.semi_totalistic_shell
ca.catalog.boundaries.fixed
ca.catalog.seeds.bernoulli
```

The index should be searchable metadata over the catalog:

```text
name
kind
compatible domains
active dimensions
rule type
alphabet
construction notes
parameters
source/reference
```

The catalog is not just documentation. It should provide actual reusable components.

## 3. Builders / Presets

Builders compose primitives into a reusable system specification.

Example:

```python
spec = (
    CABuilder()
    .domain("t+2d")
    .shape(t=8, x=11, y=11)
    .alphabet("binary")
    .seed("bernoulli", p=[0.35, 0.5, 0.65])
    .boundary("fixed", value=0)
    .neighborhood("previous_self")
    .neighborhood("axis_shell_2d")
    .neighborhood("off_axis_shell_2d")
    .rule("semi_totalistic_shell", rule_id=110)
    .frontier("full_next_slice")
    .build()
)
```

The same specification should be saveable as a preset:

```bash
ca preset save my-shell-ca specs/my-shell-ca.toml
ca generate --preset my-shell-ca --count 100
```

Most presets should be declarative and portable, using TOML, YAML, or JSON. Advanced users should also be able to reference custom Python by dotted path:

```toml
[rule]
type = "python"
path = "my_lab.rules:weird_rule"
```

Presets that reference arbitrary Python are useful locally, but less shareable than presets composed only from catalog primitives.

## 4. Generators

Generators consume resolved specs or presets and produce episodes / trajectories.

Example:

```python
gen = Generator.from_preset("my-shell-ca")
episode = gen.sample()
```

The generator output should be semantic, not transformer-shaped.

Examples:

```python
episode.values      # ndarray shaped [T], [T, X], [T, Y, X], or [T, Z, Y, X]
episode.domain
episode.rule_id
episode.rule_type
episode.seed
episode.boundary
episode.coords()
episode.metadata
```

CA may provide neutral helpers like:

```python
episode.state(t)
episode.coords(order="time-major")
episode.iter_sites(order="time-major")
```

But CA should not own transformer-specific serialization.

## Boundary With PE

CA produces trajectories.

PE turns those trajectories into model inputs.

CA should own:

```text
specs
rules
neighborhoods
frontiers / schedules
trajectory generation
rule audits
splits
generic episode objects
generic save/load
```

PE should own:

```text
token vocabulary
BOS / DOMAIN_ID tokens
flattening policy
next-state target construction
loss masks
attention masks
torch Dataset / collate
GPU dtypes and devices
MonSTER / RoPE coordinate preparation
```

So a PE-side serializer is the right place to turn CA episodes into transformer-friendly batches:

```python
example = pe.serialize_for_next_state_prediction(
    episode,
    vocab=vocab,
    order="time-major",
    prompt_states=4,
    target_states=4,
    coord_mode="txyz",
)
```

The principle:

```text
Catalog = named reusable components
Preset = saved assembled system
Generator = executable sampler
Episode = generated trajectory
```

CA should produce worlds as trajectories. PE should turn those trajectories into model food.
