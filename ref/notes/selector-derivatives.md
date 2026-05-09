# Selector Derivations

The core `locate.py` DSL should stay small. The following selector families are
useful, but they are derived catalog/helper factories rather than primitive DSL
operations.

## Coordinate Predicates

- `temporal_lag(h)`
  - Derived from `coord_eq("t", h)` when the selector frame is relative.
  - For absolute coordinates, use the same coordinate equality only when a fixed
    time coordinate is intended.

- `zero_axes(axes)`
  - Derived from `AND(coord_eq(axis, 0) for axis in axes)`.

- `nonzero_axes(axes)`
  - Derived from `NOT(zero_axes(axes))`.
  - Equivalently, derived from `count_where(axis != 0 for axis in axes) >= 1`.

- `change_count(axes, values)`
  - Derived from `count_where(project(coords, axes) != 0) in values`.
  - The axis set must stay explicit so temporal lag is not counted accidentally.

## Periodic Predicates

- `parity(axes, phase=0, modulus=2)`
  - Derived from `sum(project(coords, axes)) % modulus == phase`.
  - This is enough to express alternating cells, bands, extruded checkerboards,
    and full-dimensional checker lattices by changing only the axis set.

- `congruence(axis, step, phase=0)`
  - Derived from `coord(axis) % step == phase`.

- `product_lattice(axes, step, phase=0)`
  - Derived from `AND(congruence(axis, step, phase) for axis in axes)`.
  - This renders sparse cells, dot grids, or voxel lattices depending on active
    dimension.

- `grid_lattice(axes, step, phase=0)`
  - Derived from `OR(congruence(axis, step, phase) for axis in axes)`.
  - This renders alternating cells in 1D, grid lines in 2D, and grid planes in
    3D.

## Affine Predicates

- `subspace(free_axes, fixed=None)`
  - Derived from `AND(coord_eq(axis, value) for axis, value in fixed.items())`.
  - Rows, columns, planes, points, and lower-rank flats are aliases of this
    fixed-coordinate conjunction.

- `diagonal(axes, signs, fixed=None, center=None)`
  - Derived from linear equality over projected coordinates:
    `sign_i * (coord_i - center_i)` must be equal for all participating axes.
  - Non-participating active axes are fixed with ordinary `coord_eq`.

- `finite_segment(direction, center=None, start=None, length=None, half_length=None)`
  - Derived from affine-line membership plus a bounded interval along the line.
  - Axis-aligned bars and diagonal segments differ only in the direction vector.

## Metric Predicates

- `metric_radius(axes, metric, region, radius, center=None, thickness=None)`
  - Derived from `project`, coordinate subtraction, `norm`, and comparison.
  - Filled regions use `norm <= radius`.
  - Exact shells use `norm == radius` where appropriate.
  - Voxel shells use `radius - thickness < norm <= radius`.

- `boundary_axis_count(axes, extents, values)`
  - Derived from equality-to-boundary masks:
    `coord == lower_extent OR coord == upper_extent` per axis, then
    `count_where(boundary_axis_mask) in values`.

## Body Strata

- `cuboid_stratum(axes, extents, stratum, center=None)`
  - Derived from inside-extent coordinate comparisons and
    `boundary_axis_count`.
  - `volume`: inside all extents.
  - `shell`: inside all extents and at least one boundary axis.
  - `outline`: inside all extents and boundary-axis count at least `rank - 1`.
  - `vertices`: inside all extents and boundary-axis count equals `rank`.

- `l1_stratum(axes, radius, stratum, center=None)`
  - Derived from L1 `metric_radius`, zero/nonzero axis counts, and comparison.
  - `volume`: L1 distance `<= radius`.
  - `shell`: L1 distance `== radius`.
  - `vertices`: L1 distance `== radius` and exactly one nonzero projected axis.
  - `outline`: a catalog-level convention over the L1 shell, mainly meaningful
    in 3D.

- `l2_stratum(axes, radius, stratum, center=None, thickness=1)`
  - Derived from L2 `metric_radius`.
  - Keep only `volume` and `shell` as canonical L2 strata; outlines and vertices
    are not intrinsic for spherical bodies.

## Path, Spiral, and Fractal Families

- `fractal(...)`
  - Derived from a generic tensor predicate over coordinates.
  - Examples include bitwise tests such as `(x & y) == 0` and digit tests over
    base-3 expansions for Sierpinski-style masks.

- `spiral(...)`
  - Derived from a generic tensor predicate over coordinates or from a generated
    path mask.
  - Polar spirals use coordinate transforms and distance-to-curve predicates.
  - Square/lattice spirals can be expressed with ring/layer arithmetic or by
    scattering generated path coordinates into a mask.

- `path_mask(points, thickness=0)`
  - Derived from literal point coordinates plus optional metric dilation.
  - Useful as a catalog helper, not as a core selector primitive.

## Minimal Core

- `CoordinateSpace`
- `Selector`
- `Selection`
- `coordinate_space`
- `active_axes`
- `axis_values`
- `coord_vectors`
- `coord_grid`
- `absolute_universe`
- `offset_universe`
- `selector`
- `select`
- `mask`
- `combine_masks`
- `not_mask`
- `order_lex`
- `axis_project`
- `predicate`
- `coord_eq`
- `coord_between`
- `sum_axes`
- `count_where`
- `norm`
- `mod_eq`
- `gather`
- `native_indices`
