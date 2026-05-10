"""Composable selectors over canonical spacetime coordinates.

This module is the shared NumPy foundation for constructing finite coordinate
sets and support masks. All coordinates use canonical four-coordinate form
`[t, x, y, z]`; inactive spatial axes are fixed to zero, and active spatial
axes are centered by default.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np


Tensor = np.ndarray
Axis = Literal["t", "x", "y", "z"]
Frame = Literal["absolute", "relative"]
MaskOp = Literal["identity", "and", "or", "xor"]
Order = Literal["none", "lex"]
PredicateFn = Callable[[Tensor, Mapping[str, Any]], Tensor]

_CANONICAL_AXES = ("t", "x", "y", "z")
_SPATIAL_AXES = ("x", "y", "z")
_AXIS_COLUMNS = {"t": 0, "x": 1, "y": 2, "z": 3}
_BOUNDARY_POLICIES = ("none", "fixed", "periodic", "reflective")


@dataclass(frozen=True)
class CoordinateSpace:
    """Canonical finite coordinate space."""

    shape: tuple[int, ...]
    steps: int | None = None
    centered: bool = True
    intervals: Mapping[str, tuple[int, ...]] = field(default_factory=dict)


@dataclass(frozen=True)
class Selector:
    """Reusable finite-coordinate selector specification."""

    universe: Any
    predicates: tuple[PredicateFn, ...] = ()
    combine: MaskOp = "and"
    order: Order = "lex"
    frame: Frame = "absolute"
    read_mode: str | None = None


@dataclass(frozen=True)
class Selection:
    """Concrete selector result."""

    coords: Tensor | None
    mask: Tensor
    universe: Tensor


def _not_implemented() -> None:
    raise NotImplementedError("loci.py currently contains NumPy selector primitives only")


def coordinate_space(
    shape: Sequence[int],
    steps: int | None = None,
    centered: bool = True,
) -> CoordinateSpace:
    """Build a canonical finite coordinate space from native spatial extents."""

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
    intervals["t"] = (0,) if steps is None else tuple(axis_values("t", steps, centered=False).tolist())

    for axis_index, axis in enumerate(_SPATIAL_AXES):
        if axis_index >= len(spatial_shape):
            intervals[axis] = (0,)
            continue
        intervals[axis] = tuple(axis_values(axis, spatial_shape[axis_index], centered=centered).tolist())

    return CoordinateSpace(
        shape=spatial_shape,
        steps=steps,
        centered=centered,
        intervals=intervals,
    )


def active_axes(space_or_shape: CoordinateSpace | Sequence[int]) -> tuple[str, ...]:
    """Return active spatial axes for a coordinate space or native shape."""

    shape = space_or_shape.shape if isinstance(space_or_shape, CoordinateSpace) else tuple(space_or_shape)
    if len(shape) > 3:
        raise ValueError(f"shape rank must be 0..3, got {len(shape)}")
    return _SPATIAL_AXES[: len(shape)]


def axis_values(axis: str, size: int, centered: bool = True) -> Tensor:
    """Return coordinate values for one canonical axis."""

    if axis not in _CANONICAL_AXES:
        raise ValueError(f"unknown axis {axis!r}")

    size = int(size)
    if size <= 0:
        raise ValueError(f"axis size must be positive, got {size}")

    if axis == "t" or not centered:
        return np.arange(size, dtype=np.int64)

    if size % 2:
        half = size // 2
        return np.arange(-half, half + 1, dtype=np.int64)

    half = size // 2
    return np.arange(-half + 1, half + 1, dtype=np.int64)


def coord_vectors(space_or_shape: CoordinateSpace | Sequence[int]) -> dict[str, Tensor]:
    """Return coordinate vectors keyed by canonical axis name."""

    if isinstance(space_or_shape, CoordinateSpace):
        if space_or_shape.intervals:
            return {
                axis: np.asarray(tuple(space_or_shape.intervals[axis]), dtype=np.int64)
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
    """Build a coordinate grid with final dimension `[t, x, y, z]`."""

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
        return np.zeros((1, 4), dtype=np.int64)

    meshes = np.meshgrid(*(vecs[axis] for axis in axes), indexing="ij")
    out = np.zeros((*meshes[0].shape, 4), dtype=np.int64)
    for axis, mesh in zip(axes, meshes):
        out[..., _AXIS_COLUMNS[axis]] = mesh
    return out


def absolute_universe(
    space: CoordinateSpace,
    t: int | Sequence[int] | None = None,
    axes: Sequence[str] | None = None,
) -> Tensor:
    """Create a finite universe of absolute canonical coordinates."""

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
            time_values = np.asarray([t], dtype=np.int64)
        else:
            time_values = np.asarray(tuple(int(value) for value in t), dtype=np.int64)
        if time_values.size == 0:
            raise ValueError("t restriction cannot be empty")
        if space.steps is not None:
            valid_t = set(vecs["t"].tolist())
            missing = [int(value) for value in time_values.tolist() if int(value) not in valid_t]
            if missing:
                raise ValueError(f"time coordinates outside coordinate space: {missing}")
    elif selected_axes is None or "t" in selected_axes:
        time_values = vecs["t"] if space.steps is not None else np.asarray([0], dtype=np.int64)
    else:
        time_values = np.asarray([0], dtype=np.int64)

    values: dict[str, Tensor] = {"t": time_values}
    active = set(active_axes(space))
    for axis in _SPATIAL_AXES:
        should_expand_axis = axis in active and (selected_axes is None or axis in selected_axes)
        values[axis] = vecs[axis] if should_expand_axis else np.asarray([0], dtype=np.int64)

    meshes = np.meshgrid(*(values[axis] for axis in _CANONICAL_AXES), indexing="ij")
    return np.stack(meshes, axis=-1).reshape(-1, 4)


def offset_universe(
    time_offsets: Sequence[int],
    ranges: Mapping[str, Sequence[int]],
    active_axes: Sequence[str],
    inactive_zero: bool = True,
) -> Tensor:
    """Create a finite universe of source-relative offset coordinates."""

    active = tuple(active_axes)
    unknown = set(active).difference(_SPATIAL_AXES)
    if unknown:
        raise ValueError(f"unknown active axes: {sorted(unknown)}")

    time_values = np.asarray(tuple(int(value) for value in time_offsets), dtype=np.int64)
    if time_values.size == 0:
        raise ValueError("time_offsets cannot be empty")

    values: dict[str, Tensor] = {"t": time_values}
    for axis in _SPATIAL_AXES:
        if axis not in active and (inactive_zero or axis not in ranges):
            values[axis] = np.asarray([0], dtype=np.int64)
            continue
        if axis in active and axis not in ranges:
            raise ValueError(f"missing offset range for active axis {axis!r}")
        axis_values_t = np.asarray(tuple(int(value) for value in ranges[axis]), dtype=np.int64)
        if axis_values_t.size == 0:
            raise ValueError(f"offset range for axis {axis!r} cannot be empty")
        values[axis] = axis_values_t

    meshes = np.meshgrid(*(values[axis] for axis in _CANONICAL_AXES), indexing="ij")
    return np.stack(meshes, axis=-1).reshape(-1, 4)


def selector(
    universe: Any,
    predicates: Sequence[PredicateFn] = (),
    combine: MaskOp = "and",
    order: Order = "lex",
    frame: Frame = "absolute",
    read_mode: str | None = None,
) -> Selector:
    """Package a universe, predicates, combiner, order, and frame."""

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
    """Evaluate a selector in context."""

    context = {} if context is None else context
    universe = spec.universe(context) if callable(spec.universe) else spec.universe
    universe = np.asarray(universe)
    if universe.shape[-1:] != (4,):
        raise ValueError(f"selector universe must have final dimension 4, got {tuple(universe.shape)}")

    candidates = universe.reshape(-1, 4)
    if not spec.predicates:
        selected_mask = np.ones(candidates.shape[0], dtype=bool)
    else:
        predicate_masks = []
        for predicate_fn in spec.predicates:
            predicate_mask = np.asarray(predicate_fn(candidates, context), dtype=bool)
            if predicate_mask.size == 1:
                predicate_mask = np.broadcast_to(predicate_mask, (candidates.shape[0],))
            else:
                predicate_mask = predicate_mask.reshape(-1)
            if predicate_mask.size != candidates.shape[0]:
                raise ValueError(
                    f"predicate returned {predicate_mask.size} values for {candidates.shape[0]} candidates"
                )
            predicate_masks.append(predicate_mask)
        selected_mask = combine_masks(predicate_masks, spec.combine)

    coords = candidates[selected_mask]
    if spec.order == "lex" and coords.size:
        coords = order_lex(coords)

    return Selection(
        coords=coords,
        mask=selected_mask.reshape(universe.shape[:-1]),
        universe=universe,
    )


def mask(spec: Selector, context: Mapping[str, Any] | None = None) -> Tensor:
    """Return the unordered support mask for a selector."""

    return select(spec, context).mask


def combine_masks(masks: Sequence[Tensor], op: MaskOp = "and") -> Tensor:
    """Combine Boolean masks with selector Boolean algebra."""

    masks = [np.asarray(mask, dtype=bool) for mask in masks]
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
        elif op == "or":
            result = result | next_mask
        else:
            result = result ^ next_mask
    return result


def not_mask(mask: Tensor) -> Tensor:
    """Return the Boolean complement of a support mask."""

    return ~np.asarray(mask, dtype=bool)


def order_lex(coords: Tensor, axes: Sequence[str] = ("t", "x", "y", "z")) -> Tensor:
    """Return coordinates in deterministic lexicographic order."""

    coords_t = np.asarray(coords)
    if coords_t.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords_t.shape)}")

    columns = []
    for axis in axes:
        if axis not in _AXIS_COLUMNS:
            raise ValueError(f"unknown axis {axis!r}")
        columns.append(_AXIS_COLUMNS[axis])

    flat = coords_t.reshape(-1, 4)
    if flat.shape[0] == 0:
        return flat
    order = np.lexsort(tuple(flat[:, column] for column in reversed(columns)))
    return flat[order]


def axis_project(coords: Tensor, axes: Sequence[str]) -> Tensor:
    """Project canonical coordinate arrays onto a named axis set."""

    coords_t = np.asarray(coords)
    if coords_t.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords_t.shape)}")

    columns = []
    for axis in axes:
        if axis not in _AXIS_COLUMNS:
            raise ValueError(f"unknown axis {axis!r}")
        columns.append(_AXIS_COLUMNS[axis])
    return coords_t[..., columns]


def predicate(
    fn: PredicateFn,
    params: Mapping[str, Any] | None = None,
    name: str | None = None,
) -> PredicateFn:
    """Wrap a coordinate predicate with fixed parameters."""

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
        return np.asarray(coords)[..., column] == value

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
        coords_t = np.asarray(coords)
        return (coords_t[..., column] >= low) & (coords_t[..., column] <= high)

    return pred


def sum_axes(coords: Tensor, axes: Sequence[str]) -> Tensor:
    """Sum projected coordinate values over an explicit axis set."""

    return axis_project(coords, axes).sum(axis=-1)


def count_where(mask: Tensor, values: Sequence[int] | None = None) -> Tensor:
    """Count true values along the last axis, optionally testing membership."""

    counts = np.asarray(mask, dtype=bool).sum(axis=-1)
    if values is None:
        return counts

    values_t = np.asarray(tuple(int(value) for value in values), dtype=counts.dtype)
    if values_t.size == 0:
        return np.zeros_like(counts, dtype=bool)
    return np.isin(counts, values_t)


def norm(
    coords: Tensor,
    axes: Sequence[str],
    metric: Literal["l1", "l2", "linf"],
    center: Mapping[str, int] | None = None,
) -> Tensor:
    """Compute an axis-scoped metric norm over projected coordinates."""

    if metric not in ("l1", "l2", "linf"):
        raise ValueError(f"unknown metric {metric!r}")

    projected = axis_project(coords, axes)
    if projected.shape[-1] == 0:
        return np.zeros(projected.shape[:-1], dtype=np.float32)

    if center is not None:
        center_values = np.asarray([int(center.get(axis, 0)) for axis in axes], dtype=projected.dtype)
        projected = projected - center_values

    projected_abs = np.abs(projected)
    if metric == "l1":
        return projected_abs.sum(axis=-1)
    if metric == "l2":
        return np.sqrt(np.square(projected_abs.astype(np.float32)).sum(axis=-1))
    return projected_abs.max(axis=-1)


def mod_eq(values: Tensor, modulus: int, phase: int = 0) -> Tensor:
    """Return `values % modulus == phase` as a Boolean mask."""

    modulus = int(modulus)
    if modulus <= 0:
        raise ValueError(f"modulus must be positive, got {modulus}")
    return np.remainder(values, modulus) == (int(phase) % modulus)


def state_exists(offset_selector: Selector, value: int) -> PredicateFn:
    """Predicate factory for state-dependent existence tests."""

    value = int(value)

    def pred(coords: Tensor, context: Mapping[str, Any]) -> Tensor:
        if "values" not in context:
            raise KeyError("state_exists requires context['values']")

        selection = select(offset_selector, context)
        offsets = selection.coords
        if offsets is None:
            flat_universe = selection.universe.reshape(-1, 4)
            offsets = flat_universe[selection.mask.reshape(-1)]

        coords_arr = np.asarray(coords, dtype=np.int64)
        coords_flat = coords_arr.reshape(-1, 4)
        output_shape = coords_arr.shape[:-1]
        if offsets.size == 0:
            return np.zeros(output_shape, dtype=bool)

        query_coords = coords_flat[:, None, :] + offsets[None, :, :]
        gathered = gather(
            query_coords.reshape(-1, 4),
            np.asarray(context["values"]),
            context.get("boundary"),
        )
        gathered = gathered.reshape(coords_flat.shape[0], offsets.shape[0])
        return (gathered == value).any(axis=-1).reshape(output_shape)

    return pred


def gather(coords: Tensor, values: Tensor, boundary: Mapping[str, Any] | None = None) -> Tensor:
    """Gather native array values at canonical coordinates."""

    values_arr = np.asarray(values)
    coords_arr = np.asarray(coords, dtype=np.int64)
    if coords_arr.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords_arr.shape)}")

    boundary = {} if boundary is None else dict(boundary)
    allowed_boundary_fields = {"policy", "value", "coordinate_space"}
    extra_boundary_fields = set(boundary).difference(allowed_boundary_fields)
    if extra_boundary_fields:
        raise ValueError(f"unsupported boundary fields: {sorted(extra_boundary_fields)}")

    space = boundary.get("coordinate_space")
    if space is None and values_arr.ndim == 0:
        space = coordinate_space(())
    if space is None:
        space = coordinate_space(tuple(values_arr.shape[1:]), steps=int(values_arr.shape[0]))
    if not isinstance(space, CoordinateSpace):
        raise TypeError("boundary['coordinate_space'] must be a CoordinateSpace")

    policy = boundary.get("policy", "none")
    if not isinstance(policy, str):
        raise TypeError(f"boundary policy must be a string, got {type(policy).__name__}")
    policy = policy.lower()
    if policy not in _BOUNDARY_POLICIES:
        raise ValueError(f"unknown boundary policy {policy!r}")
    if policy != "fixed" and "value" in boundary:
        raise ValueError("boundary field 'value' is only valid for fixed policy")
    fill_value = boundary.get("value", 0)

    mapped = coords_arr.copy()
    valid = np.ones(coords_arr.shape[:-1], dtype=bool)

    if space.steps is not None:
        t_low, t_high = int(space.intervals["t"][0]), int(space.intervals["t"][-1])
        t_coord = mapped[..., 0]
        valid &= (t_coord >= t_low) & (t_coord <= t_high)
        mapped[..., 0] = np.clip(t_coord, t_low, t_high)

    active = set(active_axes(space))
    for axis in _SPATIAL_AXES:
        col = _AXIS_COLUMNS[axis]
        coord = mapped[..., col]
        if axis not in active:
            valid &= coord == 0
            mapped[..., col] = 0
            continue

        interval = space.intervals[axis]
        low, high = int(interval[0]), int(interval[-1])
        size = len(interval)
        in_bounds = (coord >= low) & (coord <= high)

        if policy == "periodic":
            mapped[..., col] = np.remainder(coord - low, size) + low
            continue
        if policy == "reflective":
            if size == 1:
                mapped[..., col] = low
                continue
            period = 2 * size - 2
            reflected = np.remainder(coord - low, period)
            reflected = np.where(reflected < size, reflected, period - reflected)
            mapped[..., col] = reflected + low
            continue
        valid &= in_bounds
        mapped[..., col] = np.clip(coord, low, high)

    if not bool(valid.all()) and policy != "fixed":
        raise IndexError("coordinates outside coordinate space and no fixed boundary policy was provided")

    indices = native_indices(mapped, space)
    if indices:
        result = values_arr[indices]
    else:
        result = np.broadcast_to(values_arr, coords_arr.shape[:-1])

    if bool(valid.all()):
        return np.asarray(result)

    fill = np.asarray(fill_value, dtype=np.asarray(result).dtype)
    return np.where(valid, result, fill)


def native_indices(coords: Tensor, space: CoordinateSpace) -> tuple[Tensor, ...]:
    """Convert canonical coordinates to native array index arrays."""

    coords_arr = np.asarray(coords, dtype=np.int64)
    if coords_arr.shape[-1:] != (4,):
        raise ValueError(f"coords must have final dimension 4, got {tuple(coords_arr.shape)}")
    if not isinstance(space, CoordinateSpace):
        raise TypeError("native_indices requires a CoordinateSpace")

    intervals = space.intervals
    if not intervals:
        intervals = coordinate_space(space.shape, space.steps, space.centered).intervals

    indices: list[Tensor] = []
    if space.steps is not None:
        indices.append(coords_arr[..., _AXIS_COLUMNS["t"]] - int(intervals["t"][0]))
    for axis in active_axes(space):
        column = _AXIS_COLUMNS[axis]
        indices.append(coords_arr[..., column] - int(intervals[axis][0]))
    return tuple(np.asarray(index, dtype=np.intp) for index in indices)
