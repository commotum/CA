# Neighborhoods Phase 2 Plan

Goal: implement the `# Phase 2 General Families` in `src/ca/neighborhoods.py`
using `src/ca/loci.py` as the only coordinate/selector foundation.

The design follows `ref/notes/index.md` and `ref/notes/generator.md`:

- Neighborhoods are source-relative read interfaces.
- Ordinary spatial reads use the current source state, `time_offset=0`.
- Negative `time_offset` values represent explicit temporal memory.
- Neighborhoods do not encode alphabet, rule id, seed policy, or frontier.
- For Wolfram-style updates, reads come from `s_t`; rollout writes `s_{t+1}`.

## Current Phase 2 Surface

Implement these functions:

```text
literal_offsets(offsets, read_mode="compact", order="lex")
history(time_offsets, read_mode="compact")
radius(axes, metric, region, radius, time_offset=0, include_center=True, read_mode="compact")
shell(axes, metric, radius, time_offset=0, read_mode="compact")
directional_line(axis, values, time_offset=0, fixed=None)
directional_fov(axes, reference, direction, aperture, radius, time_offset=0)
```

`eca(...)`, `moore(...)`, and `von_neumann(...)` are Phase 3 aliases over the
Phase 2 metric radius primitive.

## Shared Implementation Rules

- Validate axes as unique members of `("x", "y", "z")`.
- Validate `time_offset` as an integer source-relative time.
- Validate `read_mode`; for now support `"compact"` and pass it through to
  `loci.selector(read_mode=...)`.
- Validate `order`; for now support `"lex"` and `"none"` because those are the
  `loci.selector` order values.
- Return a singular `Neighborhood` unless the function is explicitly a
  composition helper.
- Always return selectors with `frame="relative"`.
- Do not hand-roll coordinate sorting or mask logic; use `loci.selector`,
  `loci.select`, `loci.offset_universe`, `loci.axis_project`, `loci.norm`,
  `loci.coord_eq`, `loci.coord_between`, and ordinary predicate functions.

## Helper Functions To Add First

Add private helpers near the Phase 2 section:

```text
_validate_axes(axes) -> tuple[str, ...]
_validate_read_mode(read_mode) -> str
_validate_order(order) -> str
_axis_ranges(axes, low, high) -> dict[str, tuple[int, ...]]
_singular_neighborhood(universe, predicates, name, params, read_mode, order="lex")
```

Keep helpers narrow. If a helper obscures the family behavior, inline the logic
instead.

## Function Plan

### `literal_offsets`

Purpose: escape hatch for hand-authored fixed stencils.

Implementation:

- Convert `offsets` to `np.ndarray(dtype=np.int64)`.
- Require shape `(n, 4)` and `n > 0`.
- Reject duplicate rows unless there is a clear reason not to.
- Build a selector directly over the literal offset array.
- No predicates needed; the literal universe is already the selected support.
- Preserve `read_mode` and `order`.

Tests:

- Returns exactly the requested offsets in lex order.
- Rejects non-4D offsets.
- Rejects empty offsets.

### `history`

Purpose: general temporal memory at the same spatial site.

Implementation:

- Validate `time_offsets` as a non-empty sequence of integers.
- Compose `self_at(time_offset=h)` for each offset.
- Preserve component boundaries with `compose(..., combine="tuple")`.
- Name should be `"history"` and params should store normalized offsets.

Tests:

- `history((0, -1, -2))` yields three components.
- Component selected coords are `[0,0,0,0]`, `[-1,0,0,0]`,
  `[-2,0,0,0]`.

### `radius`

Purpose: general metric filled/shell stencil over active spatial axes.

Implementation:

- Validate `metric in {"l1", "l2", "linf"}`.
- Validate `region in {"filled", "shell"}`.
- Validate `radius >= 0`.
- Build universe with all selected axes ranging from `-radius..+radius`.
- Predicate:
  - `filled`: `loci.norm(coords, axes, metric) <= radius`
  - `shell`: `loci.norm(coords, axes, metric) == radius`
- If `include_center=False`, add a predicate excluding all-zero projected
  spatial offsets.
- Use `loci.selector(..., combine="and", order="lex", frame="relative")`.
- For `metric="l2"`, compare exact lattice distances. Because `loci.norm`
  returns floats for L2, use `np.isclose(distance, radius)` for shell and
  `distance <= radius` for filled.

Tests:

- 1D `linf` filled radius 1 with center gives left/self/right, suitable for
  elementary CA.
- 2D `linf` filled radius 1 without center gives 8 Moore offsets.
- 2D `l1` shell radius 1 gives 4 Von Neumann offsets.
- 3D `l1` shell radius 1 gives 6 face offsets.
- `include_center=False` removes `[0,0,0,0]`.

### `shell`

Purpose: convenience wrapper for metric shell neighborhoods.

Implementation:

- Delegate to `radius(..., region="shell", include_center=False)`.
- Preserve name `"shell"` and params if useful, or return the `radius` result
  with a wrapper name. Prefer explicit name `"shell"` for inspectability.

Tests:

- `shell(("x", "y"), "l1", 1)` matches `radius(..., region="shell",
  include_center=False)`.

### `directional_line`

Purpose: axis-aligned probes such as one-sided rays or custom values.

Implementation:

- Validate `axis`.
- Validate `values` as non-empty integer sequence.
- `fixed` maps other spatial axes to fixed integer offsets. Reject `fixed`
  containing the moving axis or unknown axes.
- Active axes should include the moving axis plus fixed axes.
- Universe:
  - moving axis uses exactly `values`;
  - fixed axes use the single fixed value;
  - unspecified spatial axes stay zero.
- No predicate is required if the universe is already exact.
- Selector order should be lex by default.

Tests:

- `directional_line("x", [1, 2, 3])` yields positive x offsets.
- `directional_line("x", [-2, -1], fixed={"y": 1})` yields two offsets with
  `y=1`.
- Rejects empty `values`, bad axes, and fixed moving axis.

### `directional_fov`

Purpose: finite directional field-of-view predicate over a bounded local
support.

This family needs an explicit finite support because `loci.offset_universe`
must return a bounded candidate set. Use this signature:

```python
def directional_fov(
    axes,
    reference,
    direction,
    aperture,
    radius,
    time_offset=0,
)
```

Then:

- Validate `axes`.
- Validate `reference` and `direction` lengths match `axes`.
- Normalize `direction`; reject zero vector.
- Validate `0 < aperture <= pi` if radians, or document/choose degrees.
- Use support cube `[-radius, radius]` over `axes`.
- Predicate implements the formula from `ref/notes/generator.md`:
  include `reference`, otherwise include offsets whose normalized dot product
  with direction is at least `cos(aperture / 2)`.

Tests:

- Direction +x with small aperture includes positive x offsets and excludes
  negative x offsets.
- Reference point is included.
- Rejects zero direction and missing/invalid finite radius.

## Phase 3 Aliases

Implemented aliases:

- `eca(r=1, time_offset=0, include_center=True)` should call:
  `radius(("x",), metric="linf", region="filled", radius=r,
  time_offset=time_offset, include_center=include_center)`.
- `moore(axes=("x", "y"), r=1, ...)` should call
  `radius(..., metric="linf", region="filled",
  include_center=include_center)`.
- `von_neumann(axes=("x", "y"), r=1, ...)` should call
  `radius(..., metric="l1", region="filled",
  include_center=include_center)`.

Important: `eca` is only the read neighborhood. The standard Wolfram ECA
construction also needs binary alphabet, exhaustive 256-rule lookup,
`time_slice` frontier, and usually a single active seed on a blank background.
Those belong outside `neighborhoods.py`.

## Verification Checklist

- `uv run pytest -q`
- `uv run python -m compileall -q src tests`
- Add tests in `tests/test_neighborhoods.py` or extend existing rollout tests.
- Use `loci.select(neighborhood.components[0]).coords.tolist()` for exact
  offset assertions.
- Confirm no Phase 2 function bypasses `loci` selector primitives.
