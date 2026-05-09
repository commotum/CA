"""Composable tensor selectors over canonical spacetime coordinates.

This module is the shared DSL for constructing and defining loci: finite sets
of coordinates or offsets used by neighborhoods, frontiers, seeds, and related
catalogs. The core abstraction follows `data/context/generator.md`: construct a
finite universe, evaluate tensor predicates over every candidate, combine the
predicate masks, and return either an ordered coordinate list or an unordered
support mask.

All candidates are represented in canonical four-coordinate form `[t, x, y, z]`.
Unused spatial axes are fixed to zero. Spatial coordinates are centered by
default, while time coordinates are causal indices `0..T-1`. The same tensor
machinery should support absolute coordinate selectors, relative offset
selectors, structured geometric supports, periodic supports, and
state-dependent predicates.

Catalog/config layers should name Python function families and pass explicit
parameters. They should not define selector logic. The implementation below is
organized so each section can grow from its local spec into executable tensor
code without turning the module-level overview into a long design dump.

Catalog APIs use state-relative terms: neighborhoods default to the current
source state with `time_offset=0`, temporal-memory reads use negative
`time_offset` values, and frontiers select current update sites. The next-state
write coordinate is derived by the generator.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, Literal

import torch


Tensor = torch.Tensor
Axis = Literal["t", "x", "y", "z"]
Frame = Literal["absolute", "relative"]
MaskOp = Literal["identity", "and", "or", "xor"]
Order = Literal["none", "lex"]
PredicateFn = Callable[[Tensor, Mapping[str, Any]], Tensor]

_CANONICAL_AXES = ("t", "x", "y", "z")
_SPATIAL_AXES = ("x", "y", "z")
_AXIS_COLUMNS = {"t": 0, "x": 1, "y": 2, "z": 3}
_BOUNDARY_POLICIES = ("fixed", "periodic", "reflective", "clamp")


@dataclass(frozen=True)
class CoordinateSpace:
    """Canonical finite coordinate space.

    `shape` is the native spatial shape, `steps` is the time extent when a full
    trajectory coordinate space is needed, and `intervals` stores explicit coordinate
    values for `t`, `x`, `y`, and `z`. Unused spatial intervals should be the
    singleton `(0,)`. This object is the bridge between native tensor axes and
    canonical `[t, x, y, z]` coordinates.
    """

    shape: tuple[int, ...]
    steps: int | None = None
    centered: bool = True
    intervals: Mapping[str, tuple[int, ...]] = field(default_factory=dict)


@dataclass(frozen=True)
class Selector:
    """Reusable selector specification.

    A selector owns the finite universe generator or tensor, predicate
    functions, Boolean combiner, output ordering, coordinate frame, and optional
    read/support mode metadata. It deliberately does not encode whether a caller
    will use the selection as a support, an offset list, or a mask.
    """

    universe: Any
    predicates: tuple[PredicateFn, ...] = ()
    combine: MaskOp = "and"
    order: Order = "lex"
    frame: Frame = "absolute"
    read_mode: str | None = None


@dataclass(frozen=True)
class Selection:
    """Concrete selector result.

    `coords` contains selected candidates in canonical four-coordinate form
    when an ordered list is requested. `mask` contains the Boolean support
    aligned to the selector universe or native tensor shape. Static and
    fixed-support selectors may expose both.
    """

    coords: Tensor | None
    mask: Tensor
    universe: Tensor


def _not_implemented() -> None:
    raise NotImplementedError("locate.py currently contains DSL specs only")


# ---------------------------------------------------------------------------
# Shape and Coordinate-Space Construction
# ---------------------------------------------------------------------------


def coordinate_space(
    shape: Sequence[int],
    steps: int | None = None,
    centered: bool = True,
) -> CoordinateSpace:
    """Build a canonical finite coordinate space from native tensor extents.

    The implementation should validate rank `0..3`, normalize spatial shape to
    active axes `x`, `y`, `z`, create centered spatial coordinate intervals, and
    create `t = 0..steps-1` when `steps` is provided. Inactive spatial axes must
    be represented as zero-valued singleton intervals so every downstream tensor
    can be expressed in `[t, x, y, z]` form.
    """

    spatial_shape = tuple(int(size) for size in shape)

    if len(spatial_shape) > 3:
        raise ValueError(f"shape rank must be 0..3, got {len(spatial_shape)}")

    if any(size <= 0 for size in spatial_shape):
        raise ValueError(f"shape extents must be positive, got {spatial_shape}")

    if steps is not None:
        steps = int(steps)
        if steps <= 0:
            raise ValueError(f"steps must be positive when provided, got {steps}")

    intervals: dict[str, tuple[int, ...]] = {}
    if steps is None:
        intervals["t"] = (0,)
    else:
        intervals["t"] = tuple(axis_values("t", steps, centered=False).tolist())

    for axis_index, axis in enumerate(_SPATIAL_AXES):
        if axis_index >= len(spatial_shape):
            intervals[axis] = (0,)
            continue

        size = spatial_shape[axis_index]
        intervals[axis] = tuple(axis_values(axis, size, centered=centered).tolist())

    return CoordinateSpace(
        shape=spatial_shape,
        steps=steps,
        centered=centered,
        intervals=intervals,
    )


def active_axes(space_or_shape: CoordinateSpace | Sequence[int]) -> tuple[str, ...]:
    """Return the active spatial axes for a coordinate space or native shape.

    The result should always be a prefix of `("x", "y", "z")`. This is the
    central validation helper for axis-scoped predicates: callers may only use
    inactive axes when they are explicitly constraining those axes to zero.
    """

    shape = (
        space_or_shape.shape
        if isinstance(space_or_shape, CoordinateSpace)
        else tuple(space_or_shape)
    )

    if len(shape) > 3:
        raise ValueError(f"shape rank must be 0..3, got {len(shape)}")

    return _SPATIAL_AXES[:len(shape)]


def axis_values(axis: str, size: int, centered: bool = True) -> Tensor:
    """Return the coordinate vector for one axis.

    Spatial axes use centered coordinates by default: odd sizes map to
    `-floor(n/2)..floor(n/2)`, and even sizes map to `-(n/2)+1..n/2`. Time axes
    should use causal indices `0..T-1` regardless of `centered`.
    """

    if axis not in _CANONICAL_AXES:
        raise ValueError(f"unknown axis {axis!r}")

    size = int(size)
    if size <= 0:
        raise ValueError(f"axis size must be positive, got {size}")

    if axis == "t" or not centered:
        return torch.arange(size, dtype=torch.long)

    if size % 2:
        half = size // 2
        return torch.arange(-half, half + 1, dtype=torch.long)

    half = size // 2
    return torch.arange(-half + 1, half + 1, dtype=torch.long)


def coord_vectors(space_or_shape: CoordinateSpace | Sequence[int]) -> dict[str, Tensor]:
    """Return coordinate vectors keyed by canonical axis name.

    A full coordinate space should provide `t`, `x`, `y`, and `z` vectors, with
    inactive spatial axes as singleton zero vectors. A spatial shape may return
    only the active spatial vectors. This helper should be the source of truth
    for meshgrid construction and coordinate-index conversion.
    """

    if isinstance(space_or_shape, CoordinateSpace):
        if space_or_shape.intervals:
            return {
                axis: torch.tensor(tuple(space_or_shape.intervals[axis]), dtype=torch.long)
                for axis in _CANONICAL_AXES
            }

        return coord_vectors(
            coordinate_space(
                space_or_shape.shape,
                space_or_shape.steps,
                space_or_shape.centered,
            )
        )

    shape = tuple(int(s) for s in space_or_shape)

    if len(shape) > 3:
        raise ValueError(f"shape rank must be 0..3, got {len(shape)}")

    return {
        axis: axis_values(axis, size)
        for axis, size in zip(_SPATIAL_AXES, shape)
    }


def coord_grid(space_or_shape: CoordinateSpace | Sequence[int], frame: Frame = "absolute") -> Tensor:
    """Build a coordinate grid with final dimension `[t, x, y, z]`.

    The grid should preserve native tensor-axis order in its leading dimensions
    while storing canonical coordinates in the last dimension. For relative
    frames, callers should normally use `offset_universe`, but this function can
    still provide the common grid construction path.
    """

    if frame not in ("absolute", "relative"):
        raise ValueError(f"unknown frame {frame!r}")

    vecs = coord_vectors(space_or_shape)

    if isinstance(space_or_shape, CoordinateSpace):
        axes = active_axes(space_or_shape)
        if space_or_shape.steps is not None:
            axes = ("t",) + axes
    else:
        axes = active_axes(space_or_shape)

    if not axes:
        return torch.zeros(4, dtype=torch.long)

    meshes = torch.meshgrid(*(vecs[axis] for axis in axes), indexing="ij")
    out = torch.zeros((*meshes[0].shape, 4), dtype=torch.long, device=meshes[0].device)

    for axis, mesh in zip(axes, meshes):
        out[..., _AXIS_COLUMNS[axis]] = mesh

    return out


# ---------------------------------------------------------------------------
# Universe Builders
# ---------------------------------------------------------------------------


def absolute_universe(
    space: CoordinateSpace,
    t: int | Sequence[int] | None = None,
    axes: Sequence[str] | None = None,
) -> Tensor:
    """Create a finite candidate universe of absolute coordinates.

    This is the generic `Q = D` universe for selectors whose candidate variable
    is an absolute coordinate `c`. Optional restrictions such as a fixed time
    slice should narrow the candidate tensor before predicates run, as an
    efficiency choice that does not change selector semantics.
    """

    if not isinstance(space, CoordinateSpace):
        raise TypeError("absolute_universe requires a CoordinateSpace")

    selected_axes = None
    if axes is not None:
        selected_axes = set(axes)
        unknown = selected_axes.difference(_CANONICAL_AXES)
        if unknown:
            raise ValueError(f"unknown axes: {sorted(unknown)}")

    vecs = coord_vectors(space)

    if t is not None:
        if isinstance(t, int):
            time_values = torch.tensor([t], dtype=torch.long)
        else:
            time_values = torch.tensor(tuple(int(value) for value in t), dtype=torch.long)

        if time_values.numel() == 0:
            raise ValueError("t restriction cannot be empty")

        if space.steps is not None:
            valid_t = set(vecs["t"].tolist())
            missing = [int(value) for value in time_values.tolist() if int(value) not in valid_t]
            if missing:
                raise ValueError(f"time coordinates outside coordinate space: {missing}")

    elif selected_axes is None or "t" in selected_axes:
        time_values = vecs["t"] if space.steps is not None else torch.tensor([0], dtype=torch.long)
    else:
        time_values = torch.tensor([0], dtype=torch.long)

    values: dict[str, Tensor] = {"t": time_values}
    active = set(active_axes(space))

    for axis in _SPATIAL_AXES:
        should_expand_axis = axis in active and (selected_axes is None or axis in selected_axes)

        if not should_expand_axis:
            values[axis] = torch.tensor([0], dtype=torch.long)
            continue

        values[axis] = vecs[axis]

    meshes = torch.meshgrid(*(values[axis] for axis in _CANONICAL_AXES), indexing="ij")
    return torch.stack(meshes, dim=-1).reshape(-1, 4)


def offset_universe(
    time_offsets: Sequence[int],
    ranges: Mapping[str, Sequence[int]],
    active_axes: Sequence[str],
    inactive_zero: bool = True,
) -> Tensor:
    """Create a finite candidate universe of relative offsets.

    `time_offsets` are source-relative offsets anchored at the current update
    site. Use `0` for current-state spatial reads and negative values for
    temporal-memory reads. Inactive spatial axes should be forced to zero by
    construction when `inactive_zero=True`.
    """

    active = tuple(active_axes)
    unknown = set(active).difference(_SPATIAL_AXES)

    if unknown:
        raise ValueError(f"unknown active axes: {sorted(unknown)}")

    time_values = torch.tensor(tuple(int(value) for value in time_offsets), dtype=torch.long)
    if time_values.numel() == 0:
        raise ValueError("time_offsets cannot be empty")

    values: dict[str, Tensor] = {"t": time_values}

    for axis in _SPATIAL_AXES:
        if axis not in active and (inactive_zero or axis not in ranges):
            values[axis] = torch.tensor([0], dtype=torch.long)
            continue

        if axis in active and axis not in ranges:
            raise ValueError(f"missing offset range for active axis {axis!r}")

        axis_values_t = torch.tensor(tuple(int(value) for value in ranges[axis]), dtype=torch.long)
        if axis_values_t.numel() == 0:
            raise ValueError(f"offset range for axis {axis!r} cannot be empty")

        values[axis] = axis_values_t

    meshes = torch.meshgrid(*(values[axis] for axis in _CANONICAL_AXES), indexing="ij")
    return torch.stack(meshes, dim=-1).reshape(-1, 4)


# ---------------------------------------------------------------------------
# Selector Evaluation
# ---------------------------------------------------------------------------


def selector(
    universe: Any,
    predicates: Sequence[PredicateFn] = (),
    combine: MaskOp = "and",
    order: Order = "lex",
    frame: Frame = "absolute",
    read_mode: str | None = None,
) -> Selector:
    """Package a universe, predicates, combiner, order, and frame.

    The selector object should remain neutral: it describes a finite selection
    problem but not its later role. `combine` follows the generator schema:
    identity for a single predicate, AND by default for multiple predicates, OR
    or formula-style composition when explicitly requested.
    """

    if combine not in ("identity", "and", "or", "xor"):
        raise ValueError(f"unknown mask combiner {combine!r}")

    if order not in ("none", "lex"):
        raise ValueError(f"unknown order {order!r}")

    if frame not in ("absolute", "relative"):
        raise ValueError(f"unknown frame {frame!r}")

    return Selector(
        universe=universe,
        predicates=tuple(predicates),
        combine=combine,
        order=order,
        frame=frame,
        read_mode=read_mode,
    )


def select(spec: Selector, context: Mapping[str, Any] | None = None) -> Selection:
    """Evaluate a selector in context.

    Evaluation should materialize the finite universe, apply every predicate as
    a vectorized tensor operation over candidates, combine predicate masks,
    order selected candidates when requested, and return both selected
    coordinates and the support mask when available.
    """

    context = {} if context is None else context
    universe = spec.universe(context) if callable(spec.universe) else spec.universe
    universe = torch.as_tensor(universe)

    if universe.shape[-1:] != (4,):
        raise ValueError(f"selector universe must have final dimension 4, got {tuple(universe.shape)}")

    candidates = universe.reshape(-1, 4)

    if not spec.predicates:
        selected_mask = torch.ones(candidates.shape[0], dtype=torch.bool, device=candidates.device)
    else:
        predicate_masks = []

        for predicate_fn in spec.predicates:
            predicate_mask = predicate_fn(candidates, context)
            predicate_mask = torch.as_tensor(predicate_mask, device=candidates.device).bool()

            if predicate_mask.numel() == 1:
                predicate_mask = predicate_mask.expand(candidates.shape[0])
            else:
                predicate_mask = predicate_mask.reshape(-1)

            if predicate_mask.numel() != candidates.shape[0]:
                raise ValueError(
                    f"predicate returned {predicate_mask.numel()} values for {candidates.shape[0]} candidates"
                )

            predicate_masks.append(predicate_mask)

        selected_mask = combine_masks(predicate_masks, spec.combine)

    coords = candidates[selected_mask]
    if spec.order == "lex" and coords.numel():
        coords = order_lex(coords)

    return Selection(
        coords=coords,
        mask=selected_mask.reshape(universe.shape[:-1]),
        universe=universe,
    )


def mask(spec: Selector, context: Mapping[str, Any] | None = None) -> Tensor:
    """Return the unordered support mask for a selector.

    The mask should align either to the candidate universe or to the native
    tensor shape declared by the selector. This support view is what makes
    ordinary tensor indexing, assignment, visualization, and rendered-mask
    deduplication straightforward.
    """

    return select(spec, context).mask


def combine_masks(masks: Sequence[Tensor], op: MaskOp = "and") -> Tensor:
    """Combine Boolean masks with selector Boolean algebra.

    Core operations should include identity, AND, OR, and XOR. More complex
    formula combiners can be layered on top, but the primitive behavior should
    stay tensorized and shape-preserving.
    """

    masks = [torch.as_tensor(mask).bool() for mask in masks]

    if not masks:
        raise ValueError("at least one mask is required")

    if op == "identity":
        if len(masks) != 1:
            raise ValueError("identity combiner requires exactly one mask")
        return masks[0]

    if op not in ("and", "or", "xor"):
        raise ValueError(f"unknown mask combiner {op!r}")

    result = masks[0]

    for next_mask in masks[1:]:
        if op == "and":
            result = result & next_mask
            continue

        if op == "or":
            result = result | next_mask
            continue

        result = result ^ next_mask

    return result


def not_mask(mask: Tensor) -> Tensor:
    """Return the Boolean complement of a support mask.

    Complements should be implemented as mask algebra rather than as separate
    geometric families. This keeps inverted seeds, holes, and excluded regions
    compositional.
    """

    return ~torch.as_tensor(mask).bool()


def order_lex(coords: Tensor, axes: Sequence[str] = ("t", "x", "y", "z")) -> Tensor:
    """Return indices or coordinates in deterministic lexicographic order.

    Ordering is mathematically relevant for ordered selections and operationally
    useful for manifests, reproducible sampling, debug prints, and exact mask
    deduplication. The default order is canonical `[t, x, y, z]`.
    """

    coords_t = torch.as_tensor(coords)

    if coords_t.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords_t.shape)}")

    columns = []
    for axis in axes:
        if axis not in _AXIS_COLUMNS:
            raise ValueError(f"unknown axis {axis!r}")
        columns.append(_AXIS_COLUMNS[axis])

    flat = coords_t.reshape(-1, 4)
    sorted_indices = torch.arange(flat.shape[0], device=flat.device)

    for column in reversed(columns):
        column_values = flat[sorted_indices, column]
        sorted_indices = sorted_indices[torch.argsort(column_values, stable=True)]

    return flat[sorted_indices]


def axis_project(coords: Tensor, axes: Sequence[str]) -> Tensor:
    """Project canonical coordinate tensors onto a named axis set.

    Metric, parity, congruence, and count predicates should all use this
    helper. Keeping the axis set explicit prevents the temporal coordinate from
    leaking into spatial predicates and keeps extruded versus full-dimensional
    patterns distinct.
    """

    coords_t = torch.as_tensor(coords)

    if coords_t.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords_t.shape)}")

    columns = []
    for axis in axes:
        if axis not in _AXIS_COLUMNS:
            raise ValueError(f"unknown axis {axis!r}")
        columns.append(_AXIS_COLUMNS[axis])

    return coords_t[..., columns]


# ---------------------------------------------------------------------------
# Predicate and Reduction Primitives
# ---------------------------------------------------------------------------


def predicate(
    fn: PredicateFn,
    params: Mapping[str, Any] | None = None,
    name: str | None = None,
) -> PredicateFn:
    """Wrap an arbitrary tensor predicate as a first-class selector predicate.

    The wrapped function must accept candidate coordinates and context and
    return one Boolean value per candidate. Catalog factories for fractals,
    spirals, affine shapes, metric bodies, and periodic masks should compile
    down to this generic predicate form instead of becoming core DSL concepts.
    """

    fixed_params = dict(params or {})

    def wrapped(coords: Tensor, context: Mapping[str, Any]) -> Tensor:
        merged = dict(context)
        merged.update(fixed_params)
        return fn(coords, merged)

    if name is not None:
        wrapped.__name__ = name
    return wrapped


def coord_eq(axis: str, value: int) -> PredicateFn:
    """Predicate factory for equality on one canonical axis."""

    if axis not in _AXIS_COLUMNS:
        raise ValueError(f"unknown axis {axis!r}")

    column = _AXIS_COLUMNS[axis]
    value = int(value)

    def pred(coords: Tensor, context: Mapping[str, Any]) -> Tensor:
        return coords[..., column] == value

    return pred


def coord_between(axis: str, low: int, high: int) -> PredicateFn:
    """Predicate factory for inclusive interval selection on one axis."""

    if axis not in _AXIS_COLUMNS:
        raise ValueError(f"unknown axis {axis!r}")

    low, high = int(low), int(high)

    if low > high:
        raise ValueError(f"low must be <= high, got {low} > {high}")

    column = _AXIS_COLUMNS[axis]

    def pred(coords: Tensor, context: Mapping[str, Any]) -> Tensor:
        return (coords[..., column] >= low) & (coords[..., column] <= high)

    return pred


def sum_axes(coords: Tensor, axes: Sequence[str]) -> Tensor:
    """Sum projected coordinate values over an explicit axis set.

    Periodic parity and other modular families should be derived from this
    reduction plus `mod_eq`, keeping axis selection explicit and minimal.
    """

    return axis_project(coords, axes).sum(dim=-1)


def count_where(mask: Tensor, values: Sequence[int] | None = None) -> Tensor:
    """Count true values along the predicate's reduction dimension.

    Change counts, boundary-axis counts, zero/nonzero axis tests, and many
    stratum predicates are derived from this primitive count operation.
    """

    counts = torch.as_tensor(mask).bool().sum(dim=-1)

    if values is None:
        return counts

    values_t = torch.tensor(
        tuple(int(value) for value in values),
        dtype=counts.dtype,
        device=counts.device,
    )

    if values_t.numel() == 0:
        return torch.zeros_like(counts, dtype=torch.bool)

    return torch.isin(counts, values_t)


def norm(
    coords: Tensor,
    axes: Sequence[str],
    metric: Literal["l1", "l2", "linf"],
    center: Mapping[str, int] | None = None,
) -> Tensor:
    """Compute an axis-scoped metric norm over projected coordinates.

    Filled balls, shells, cuboids, diamonds, spheres, and distance-to-curve
    predicates should be derived from this primitive plus ordinary comparisons.
    """

    if metric not in ("l1", "l2", "linf"):
        raise ValueError(f"unknown metric {metric!r}")

    projected = axis_project(coords, axes)

    if projected.shape[-1] == 0:
        return torch.zeros(projected.shape[:-1], dtype=torch.float32, device=projected.device)

    if center is not None:
        center_values = torch.tensor(
            [int(center.get(axis, 0)) for axis in axes],
            dtype=projected.dtype,
            device=projected.device,
        )
        projected = projected - center_values

    projected_abs = projected.abs()

    if metric == "l1":
        return projected_abs.sum(dim=-1)

    if metric == "l2":
        return projected_abs.float().square().sum(dim=-1).sqrt()

    return projected_abs.max(dim=-1).values


def mod_eq(values: Tensor, modulus: int, phase: int = 0) -> Tensor:
    """Return `values % modulus == phase` as a Boolean mask.

    Congruence, parity, product lattices, and grid lattices should be expressed
    in catalog/helper code by combining this primitive with projection,
    reductions, and Boolean mask algebra.
    """

    modulus = int(modulus)

    if modulus <= 0:
        raise ValueError(f"modulus must be positive, got {modulus}")

    return torch.remainder(values, modulus) == (int(phase) % modulus)


# ---------------------------------------------------------------------------
# State-Dependent Predicates and Tensor Indexing
# ---------------------------------------------------------------------------


def state_exists(offset_selector: Selector, value: int) -> PredicateFn:
    """Predicate factory for state-dependent existence tests.

    The predicate should evaluate `offset_selector` relative to each candidate,
    gather the context state at those relative coordinates, and return true
    when any gathered value equals `value`. This is the generic hook for
    adaptive selectors without baking adaptive behavior into the selector core.
    """

    value = int(value)

    def pred(coords: Tensor, context: Mapping[str, Any]) -> Tensor:
        if "values" not in context:
            raise KeyError("state_exists requires context['values']")

        selection = select(offset_selector, context)
        offsets = selection.coords

        if offsets is None:
            flat_universe = selection.universe.reshape(-1, 4)
            offsets = flat_universe[selection.mask.reshape(-1)]

        coords = torch.as_tensor(coords, dtype=torch.long)
        coords_flat = coords.reshape(-1, 4)
        output_shape = coords.shape[:-1]

        if offsets.numel() == 0:
            return torch.zeros(output_shape, dtype=torch.bool, device=coords_flat.device)

        offsets = offsets.to(coords_flat.device)
        query_coords = coords_flat[:, None, :] + offsets[None, :, :]

        gathered = gather(
            query_coords.reshape(-1, 4),
            torch.as_tensor(context["values"]),
            context.get("boundary"),
        )

        gathered = gathered.reshape(coords_flat.shape[0], offsets.shape[0])
        return (gathered == value).any(dim=-1).reshape(output_shape)

    return pred


def gather(coords: Tensor, values: Tensor, boundary: Mapping[str, Any] | None = None) -> Tensor:
    """Gather native tensor values at canonical coordinates.

    This helper maps `[t, x, y, z]` coordinates back to native tensor indices,
    applies a boundary policy when provided, and returns values in the same
    order as `coords`. Higher-level code should use this rather than duplicating
    coordinate-to-index arithmetic.
    """

    values = torch.as_tensor(values)
    coords = torch.as_tensor(coords, dtype=torch.long, device=values.device)

    if coords.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords.shape)}")

    boundary = {} if boundary is None else boundary
    space = boundary.get("coordinate_space")

    if space is None and values.ndim == 0:
        space = coordinate_space(())

    if space is None:
        space = coordinate_space(tuple(values.shape[1:]), steps=int(values.shape[0]))

    if not isinstance(space, CoordinateSpace):
        raise TypeError("boundary['coordinate_space'] must be a CoordinateSpace")

    policy = boundary.get("policy", boundary.get("mode", boundary.get("type")))
    policy = policy.lower() if isinstance(policy, str) else policy

    if policy is not None and policy not in _BOUNDARY_POLICIES:
        raise ValueError(f"unknown boundary policy {policy!r}")

    fill_value = boundary.get("value", boundary.get("fill_value", 0))

    mapped = coords.clone()
    valid = torch.ones(coords.shape[:-1], dtype=torch.bool, device=coords.device)

    if space.steps is not None:
        t_low, t_high = space.intervals["t"][0], space.intervals["t"][-1]
        t_coord = mapped[..., 0]

        valid = valid & (t_coord >= t_low) & (t_coord <= t_high)
        mapped[..., 0] = t_coord.clamp(t_low, t_high)

    active = set(active_axes(space))

    for axis in _SPATIAL_AXES:
        col = _AXIS_COLUMNS[axis]
        coord = mapped[..., col]

        if axis not in active:
            valid = valid & (coord == 0)
            mapped[..., col] = 0
            continue

        interval = space.intervals[axis]
        low, high = int(interval[0]), int(interval[-1])
        size = len(interval)
        in_bounds = (coord >= low) & (coord <= high)

        if policy == "periodic":
            mapped[..., col] = torch.remainder(coord - low, size) + low
            continue

        if policy == "reflective":
            if size == 1:
                mapped[..., col] = low
                continue

            period = 2 * size - 2
            reflected = torch.remainder(coord - low, period)
            reflected = torch.where(reflected < size, reflected, period - reflected)
            mapped[..., col] = reflected + low
            continue

        if policy == "clamp":
            mapped[..., col] = coord.clamp(low, high)
            continue

        valid = valid & in_bounds
        mapped[..., col] = coord.clamp(low, high)

    has_invalid_coords = not bool(valid.all())

    if has_invalid_coords and policy != "fixed":
        raise IndexError("coordinates outside coordinate space and no fixed boundary policy was provided")

    indices = native_indices(mapped, space)

    if indices:
        result = values[indices]
    else:
        result = values.expand(coords.shape[:-1])

    if not has_invalid_coords:
        return result

    fill = torch.as_tensor(fill_value, dtype=result.dtype, device=result.device)
    return torch.where(valid, result, fill)


def native_indices(coords: Tensor, space: CoordinateSpace) -> tuple[Tensor, ...]:
    """Convert canonical coordinates to native tensor index tensors.

    The conversion should account for centered spatial coordinate offsets and
    omit inactive axes when indexing native tensors. It is the inverse of the
    coordinate-grid construction path.
    """

    coords = torch.as_tensor(coords, dtype=torch.long)

    if coords.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords.shape)}")

    if not isinstance(space, CoordinateSpace):
        raise TypeError("native_indices requires a CoordinateSpace")

    intervals = space.intervals

    if not intervals:
        intervals = {}
        if space.steps is None:
            intervals["t"] = (0,)
        else:
            intervals["t"] = tuple(axis_values("t", space.steps, centered=False).tolist())

        for axis_index, axis in enumerate(_SPATIAL_AXES):
            if axis_index >= len(space.shape):
                intervals[axis] = (0,)
                continue

            size = space.shape[axis_index]
            intervals[axis] = tuple(axis_values(axis, size, centered=space.centered).tolist())

    indices: list[Tensor] = []

    if space.steps is not None:
        indices.append(coords[..., _AXIS_COLUMNS["t"]] - int(intervals["t"][0]))

    for axis in active_axes(space):
        column = _AXIS_COLUMNS[axis]
        first_value = int(intervals[axis][0])
        indices.append(coords[..., column] - first_value)

    return tuple(index.long() for index in indices)
