"""Neighborhood catalog factories built from loci.

This module defines named neighborhood families for cellular-automata style
next-state generation. A neighborhood is a read interface: it defines the
source-relative offsets read around each current update site before the rule
writes the corresponding next-state value.

The construction hierarchy is intentional:

- `loci.py` owns the minimal tensor selector machinery: offset universes,
  predicates, mask algebra, ordering, and coordinate/index conversion.
- Singular neighborhoods are built directly from `loci.py` primitives. Each
  singular neighborhood should describe one coherent read locus, such as the
  current cell, a shell along one axis, or an L1 shell across several axes.
- Compound or multi-component neighborhoods are built by composing singular
  neighborhoods. They should preserve component boundaries when the rule needs
  to treat groups differently.

This keeps low-level selector logic centralized in `loci.py`, keeps simple
neighborhoods reusable, and prevents composite families from duplicating
primitive coordinate/predicate construction.

The default convention follows Wolfram-style next-state updates: ordinary
spatial neighborhoods read the current source state with `time_offset=0`, and
the generator writes the computed value to time `t+1`. Negative `time_offset`
values are reserved for explicit temporal-memory neighborhoods such as scalar
recurrences.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal

import numpy as np

from . import loci


CombineMode = Literal["tuple"]
Metric = Literal["l1", "l2", "linf"]
Region = Literal["filled", "shell"]


@dataclass(frozen=True)
class Neighborhood:
    """Structured neighborhood definition.

    `components` stores one or more loci selectors. Singular neighborhoods use
    one component. Compound neighborhoods use multiple components and normally
    keep `combine="tuple"` so downstream rules can distinguish self, primary,
    secondary, history, or other read groups.
    """

    components: tuple[loci.Selector, ...]
    combine: CombineMode = "tuple"
    name: str | None = None
    params: Mapping[str, Any] | None = None


# ---------------------------------------------------------------------------
# Internal Construction Helpers
# ---------------------------------------------------------------------------


def _validate_axis(axis: str) -> str:
    axis = str(axis)
    if axis not in ("x", "y", "z"):
        raise ValueError(f"axis must be one of x, y, z; got {axis!r}")
    return axis


def _validate_axes(axes: Sequence[str]) -> tuple[str, ...]:
    out = tuple(_validate_axis(axis) for axis in axes)
    if not out:
        raise ValueError("axes cannot be empty")
    if len(set(out)) != len(out):
        raise ValueError(f"axes must be unique, got {out}")
    return out


def _validate_read_mode(read_mode: str) -> str:
    read_mode = str(read_mode)
    if read_mode != "compact":
        raise ValueError(f"read_mode must be 'compact', got {read_mode!r}")
    return read_mode


def _validate_order(order: str) -> str:
    order = str(order)
    if order not in ("lex", "none"):
        raise ValueError(f"order must be 'lex' or 'none', got {order!r}")
    return order


def _axis_ranges(axes: Sequence[str], low: int, high: int) -> dict[str, tuple[int, ...]]:
    low = int(low)
    high = int(high)
    if low > high:
        raise ValueError(f"low must be <= high, got {low} > {high}")
    return {axis: tuple(range(low, high + 1)) for axis in axes}


# ---------------------------------------------------------------------------
# Core Neighborhood Constructors
# ---------------------------------------------------------------------------


def self_at(time_offset: int = 0, read_mode: str | None = None) -> Neighborhood:
    """Read the current cell itself at a source-relative time."""

    time_offset = int(time_offset)
    if read_mode is not None:
        read_mode = _validate_read_mode(read_mode)

    universe = loci.offset_universe(
        time_offsets=(time_offset,),
        ranges={},
        active_axes=(),
    )
    component = loci.selector(
        universe,
        order="lex",
        frame="relative",
        read_mode=read_mode,
    )

    params: dict[str, Any] = {"time_offset": time_offset}
    if read_mode is not None:
        params["read_mode"] = read_mode

    return Neighborhood(
        components=(component,),
        name="self_at",
        params=params,
    )


def literal_offsets(
    offsets: Sequence[Sequence[int]],
    read_mode: str = "compact",
    order: str = "lex",
) -> Neighborhood:
    """Build a singular neighborhood from explicitly listed offsets.

    This is the escape hatch for small hand-authored stencils. It should still
    compile into an ordinary loci selector rather than bypassing the selector
    machinery.
    """

    read_mode = _validate_read_mode(read_mode)
    order = _validate_order(order)
    offset_array = np.asarray(offsets, dtype=np.int64)

    if offset_array.ndim != 2 or offset_array.shape[1:] != (4,):
        raise ValueError(f"offsets must have shape (n, 4), got {tuple(offset_array.shape)}")
    if offset_array.shape[0] == 0:
        raise ValueError("offsets cannot be empty")
    if np.unique(offset_array, axis=0).shape[0] != offset_array.shape[0]:
        raise ValueError("offsets must be unique")

    component = loci.selector(
        offset_array,
        order=order,
        frame="relative",
        read_mode=read_mode,
    )

    return Neighborhood(
        components=(component,),
        name="literal_offsets",
        params={"offsets": tuple(tuple(int(value) for value in row) for row in offset_array.tolist())},
    )


def radius(
    axes: Sequence[str],
    metric: Metric,
    region: Region,
    radius: int,
    time_offset: int = 0,
    include_center: bool = True,
    read_mode: str = "compact",
) -> Neighborhood:
    """Build a metric radius neighborhood over selected axes."""

    axes = _validate_axes(axes)
    metric = str(metric)
    region = str(region)
    radius = int(radius)
    time_offset = int(time_offset)
    include_center = bool(include_center)
    read_mode = _validate_read_mode(read_mode)

    if metric not in ("l1", "l2", "linf"):
        raise ValueError(f"metric must be l1, l2, or linf; got {metric!r}")
    if region not in ("filled", "shell"):
        raise ValueError(f"region must be filled or shell; got {region!r}")
    if radius < 0:
        raise ValueError(f"radius must be non-negative, got {radius}")
    if radius == 0 and not include_center:
        raise ValueError("radius=0 with include_center=False selects no offsets")

    def in_metric_region(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        distances = loci.norm(coords, axes, metric=metric)  # type: ignore[arg-type]
        if region == "filled":
            return distances <= radius
        if metric == "l2":
            return np.isclose(distances, radius)
        return distances == radius

    predicates: list[loci.PredicateFn] = [in_metric_region]

    if not include_center:
        def is_not_center(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
            projected = loci.axis_project(coords, axes)
            return np.any(projected != 0, axis=-1)

        predicates.append(is_not_center)

    universe = loci.offset_universe(
        time_offsets=(time_offset,),
        ranges=_axis_ranges(axes, -radius, radius),
        active_axes=axes,
    )
    component = loci.selector(
        universe,
        predicates=tuple(predicates),
        order="lex",
        frame="relative",
        read_mode=read_mode,
    )

    return Neighborhood(
        components=(component,),
        name="radius",
        params={
            "axes": axes,
            "metric": metric,
            "region": region,
            "radius": radius,
            "time_offset": time_offset,
            "include_center": include_center,
            "read_mode": read_mode,
        },
    )


def shell(
    axes: Sequence[str],
    metric: Metric,
    r: int = 1,
    time_offset: int = 0,
    read_mode: str = "compact",
) -> Neighborhood:
    """Build an exact metric shell, excluding the center."""

    neighborhood = radius(
        axes=axes,
        metric=metric,
        region="shell",
        radius=r,
        time_offset=time_offset,
        include_center=False,
        read_mode=read_mode,
    )
    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="shell",
        params=neighborhood.params,
    )


def axis_shell(axis: str, radius: int, time_offset: int = 0) -> Neighborhood:
    """Read the two offsets exactly `radius` steps away along one axis."""

    axis = _validate_axis(axis)
    radius = int(radius)
    if radius <= 0:
        raise ValueError(f"radius must be positive, got {radius}")

    neighborhood = shell((axis,), metric="linf", r=radius, time_offset=time_offset)
    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="axis_shell",
        params={"axis": axis, "radius": radius, "time_offset": int(time_offset)},
    )


def l1_shell(
    axes: Sequence[str],
    radius: int = 1,
    time_offset: int = 0,
) -> Neighborhood:
    """Read all offsets at exact Manhattan/L1 distance `radius`."""

    axes = _validate_axes(axes)
    neighborhood = shell(axes, metric="l1", r=radius, time_offset=time_offset)
    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="l1_shell",
        params={"axes": axes, "radius": int(radius), "time_offset": int(time_offset)},
    )


# ---------------------------------------------------------------------------
# Derived Neighborhood Constructors
# ---------------------------------------------------------------------------


def change_count_shell(
    axes: Sequence[str],
    counts: Sequence[int],
    radius: int = 1,
    time_offset: int = 0,
) -> Neighborhood:
    """Read offsets where a selected number of axes changed from zero."""

    axes = _validate_axes(axes)
    counts = tuple(int(count) for count in counts)
    radius = int(radius)
    time_offset = int(time_offset)

    if not counts:
        raise ValueError("counts cannot be empty")

    for count in counts:
        if count < 0 or count > len(axes):
            raise ValueError(f"counts must be between 0 and {len(axes)}, got {count}")

    if radius < 0:
        raise ValueError(f"radius must be non-negative, got {radius}")

    def has_change_count(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        projected = loci.axis_project(coords, axes)
        changed_axes = projected != 0
        return loci.count_where(changed_axes, counts)

    universe = loci.offset_universe(
        time_offsets=(time_offset,),
        ranges=_axis_ranges(axes, -radius, radius),
        active_axes=axes,
    )
    component = loci.selector(
        universe,
        predicates=(has_change_count,),
        order="lex",
        frame="relative",
        read_mode="compact",
    )

    return Neighborhood(
        components=(component,),
        name="change_count_shell",
        params={
            "axes": axes,
            "counts": counts,
            "radius": radius,
            "time_offset": time_offset,
        },
    )


def directional_line(
    axis: str,
    values: Sequence[int],
    time_offset: int = 0,
    fixed: Mapping[str, int] | None = None,
) -> Neighborhood:
    """Read offsets along one directed axis with optional fixed coordinates.

    This covers one-sided rays, finite directional probes, and axis-aligned
    line stencils. It should be built from an offset universe plus equality or
    interval predicates rather than becoming a loci primitive.
    """

    axis = _validate_axis(axis)
    value_tuple = tuple(int(value) for value in values)
    if not value_tuple:
        raise ValueError("values cannot be empty")

    fixed_values = {} if fixed is None else {str(key): int(value) for key, value in fixed.items()}
    for fixed_axis in fixed_values:
        _validate_axis(fixed_axis)
    if axis in fixed_values:
        raise ValueError("fixed cannot constrain the moving axis")

    active_axes = tuple(axis_name for axis_name in ("x", "y", "z") if axis_name == axis or axis_name in fixed_values)
    ranges: dict[str, tuple[int, ...]] = {axis: value_tuple}
    ranges.update({fixed_axis: (fixed_value,) for fixed_axis, fixed_value in fixed_values.items()})

    universe = loci.offset_universe(
        time_offsets=(int(time_offset),),
        ranges=ranges,
        active_axes=active_axes,
    )
    component = loci.selector(
        universe,
        order="lex",
        frame="relative",
        read_mode="compact",
    )

    return Neighborhood(
        components=(component,),
        name="directional_line",
        params={
            "axis": axis,
            "values": value_tuple,
            "time_offset": int(time_offset),
            "fixed": fixed_values,
        },
    )


def directional_fov(
    axes: Sequence[str],
    reference: Sequence[int],
    direction: Sequence[float],
    aperture: float,
    radius: int,
    time_offset: int = 0,
) -> Neighborhood:
    """Read offsets inside a directional field of view.

    This is a derived predicate family over coordinates. It should compile to a
    generic `loci.predicate` that tests angular inclusion relative to
    `reference`, `direction`, and `aperture`.
    """

    axes = _validate_axes(axes)
    reference_values = np.asarray(tuple(int(value) for value in reference), dtype=np.float64)
    direction_values = np.asarray(tuple(float(value) for value in direction), dtype=np.float64)
    aperture = float(aperture)
    radius = int(radius)
    time_offset = int(time_offset)

    if reference_values.shape != (len(axes),):
        raise ValueError(f"reference must contain {len(axes)} values")
    if direction_values.shape != (len(axes),):
        raise ValueError(f"direction must contain {len(axes)} values")
    if radius < 0:
        raise ValueError(f"radius must be non-negative, got {radius}")
    if np.any(np.abs(reference_values) > radius):
        raise ValueError("reference must lie inside the finite radius support")
    if not 0 < aperture <= np.pi:
        raise ValueError("aperture must be in radians with 0 < aperture <= pi")

    direction_norm = np.linalg.norm(direction_values)
    if direction_norm == 0:
        raise ValueError("direction cannot be the zero vector")
    direction_unit = direction_values / direction_norm
    threshold = float(np.cos(aperture / 2.0))

    def in_field_of_view(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        projected = loci.axis_project(coords, axes).astype(np.float64)
        relative = projected - reference_values
        at_reference = np.all(projected == reference_values, axis=-1)
        lengths = np.linalg.norm(relative, axis=-1)
        dots = relative @ direction_unit
        with np.errstate(divide="ignore", invalid="ignore"):
            cosines = dots / lengths
        return at_reference | ((lengths > 0) & (cosines >= threshold))

    universe = loci.offset_universe(
        time_offsets=(time_offset,),
        ranges=_axis_ranges(axes, -radius, radius),
        active_axes=axes,
    )
    component = loci.selector(
        universe,
        predicates=(in_field_of_view,),
        order="lex",
        frame="relative",
        read_mode="compact",
    )

    return Neighborhood(
        components=(component,),
        name="directional_fov",
        params={
            "axes": axes,
            "reference": tuple(int(value) for value in reference_values.astype(np.int64).tolist()),
            "direction": tuple(float(value) for value in direction_values.tolist()),
            "aperture": aperture,
            "radius": radius,
            "time_offset": time_offset,
        },
    )


# ---------------------------------------------------------------------------
# Composition
# ---------------------------------------------------------------------------


def compose(components: Sequence[Neighborhood]) -> Neighborhood:
    """Compose singular or already-structured neighborhoods.

    Component boundaries are preserved. This matters for Dyadrads, Dyadaxes,
    and temporal-memory neighborhoods because downstream rules need to know
    which values came from which read group.
    """

    if not components:
        raise ValueError("components cannot be empty")

    selectors = []
    for component in components:
        selectors.extend(component.components)

    return Neighborhood(
        components=tuple(selectors),
        combine="tuple",
        name="compose",
        params={"component_count": len(components)},
    )


def history(time_offsets: Sequence[int], read_mode: str = "compact") -> Neighborhood:
    """Read the same spatial site at multiple source-relative times."""

    read_mode = _validate_read_mode(read_mode)
    normalized_offsets = tuple(int(time_offset) for time_offset in time_offsets)
    if not normalized_offsets:
        raise ValueError("time_offsets cannot be empty")

    components = tuple(
        self_at(time_offset=time_offset, read_mode=read_mode)
        for time_offset in normalized_offsets
    )
    neighborhood = compose(components)

    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="history",
        params={"time_offsets": normalized_offsets, "read_mode": read_mode},
    )


# ---------------------------------------------------------------------------
# Named Neighborhood Families
# ---------------------------------------------------------------------------


def eca(
    r: int = 1,
    time_offset: int = 0,
    include_center: bool = True,
) -> Neighborhood:
    """Alias for the standard Wolfram elementary-CA read neighborhood.

    With defaults, this is the one-dimensional nearest-neighbor stencil
    `[left, self, right]`. Larger `r` values extend that filled 1D stencil.
    """

    return radius(
        axes=("x",),
        metric="linf",
        region="filled",
        radius=r,
        time_offset=int(time_offset),
        include_center=include_center,
    )


def moore(
    axes: Sequence[str] = ("x", "y"),
    r: int = 1,
    time_offset: int = 0,
    include_center: bool = False,
) -> Neighborhood:
    """Alias for the L-infinity filled neighborhood.

    In 2D with radius 1 and `include_center=False`, this is the eight-cell
    Moore neighborhood. In 3D, it is the 26-cell surrounding cube shell.
    """

    return radius(
        axes=axes,
        metric="linf",
        region="filled",
        radius=r,
        time_offset=time_offset,
        include_center=include_center,
    )


def von_neumann(
    axes: Sequence[str] = ("x", "y"),
    r: int = 1,
    time_offset: int = 0,
    include_center: bool = False,
) -> Neighborhood:
    """Alias for the filled L1/Von Neumann neighborhood.

    With radius 1 and `include_center=False`, this is the usual cardinal shell:
    two cells in 1D, four in 2D, and six in 3D. With larger radii, it is the
    filled L1 metric region, optionally excluding the center.
    """

    return radius(
        axes=axes,
        metric="l1",
        region="filled",
        radius=r,
        time_offset=time_offset,
        include_center=include_center,
    )


def ar2_0d(time_offsets: Sequence[int] = (0, -1)) -> Neighborhood:
    """Build the 0D second-order scalar recurrence read interface.

    This compound neighborhood reads the scalar at the current source time and
    the same scalar one step back by default:
    `[0, 0, 0, 0]` and `[-1, 0, 0, 0]`.

    It should be built by composing `self_at(time_offset=0)` and
    `self_at(time_offset=-1)` rather than rebuilding the offsets directly.
    """

    components = [self_at(time_offset=time_offset) for time_offset in time_offsets]
    neighborhood = compose(components)

    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="ar2_0d",
        params={"time_offsets": tuple(int(time_offset) for time_offset in time_offsets)},
    )


def dyadrads_1d(time_offset: int = 0) -> Neighborhood:
    """Build the 1D Dyadrads three-component neighborhood.

    The components are current self, radius-1 shell on `x`, and radius-2 shell
    on `x`. The grouping is semantically important: this is not merely a flat
    radius-2 stencil, because the rule may treat self, primary radius, and
    secondary radius as different inputs.

    It should be built from `self_at`, `axis_shell(axis="x", radius=1)`, and
    `axis_shell(axis="x", radius=2)`, then combined with `compose`.
    """

    time_offset = int(time_offset)
    neighborhood = compose((
        self_at(time_offset=time_offset),
        axis_shell(axis="x", radius=1, time_offset=time_offset),
        axis_shell(axis="x", radius=2, time_offset=time_offset),
    ))

    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="dyadrads_1d",
        params={"time_offset": time_offset},
    )


def dyadaxes_2d(time_offset: int = 0) -> Neighborhood:
    """Build the 2D Dyadaxes three-component neighborhood.

    The components are current self, the four L1/cardinal neighbors, and the
    four diagonal neighbors in the current `3x3` spatial window.

    It should be built from `self_at`, `l1_shell(axes=("x", "y"), radius=1)`,
    and `change_count_shell(axes=("x", "y"), counts=(2,), radius=1)`, then
    combined with `compose`.
    """

    time_offset = int(time_offset)
    neighborhood = compose((
        self_at(time_offset=time_offset),
        l1_shell(axes=("x", "y"), radius=1, time_offset=time_offset),
        change_count_shell(axes=("x", "y"), counts=(2,), radius=1, time_offset=time_offset),
    ))

    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="dyadaxes_2d",
        params={"time_offset": time_offset},
    )


def dyadaxes_3d(time_offset: int = 0) -> Neighborhood:
    """Build the 3D Dyadaxes three-component neighborhood.

    The components are current self, the six face-adjacent voxels, and the
    twenty edge/corner voxels in the surrounding `3x3x3` spatial window.

    It should be built from `self_at`, `l1_shell(axes=("x", "y", "z"),
    radius=1)`, and `change_count_shell(axes=("x", "y", "z"), counts=(2, 3),
    radius=1)`, then combined with `compose`.
    """

    time_offset = int(time_offset)
    neighborhood = compose((
        self_at(time_offset=time_offset),
        l1_shell(axes=("x", "y", "z"), radius=1, time_offset=time_offset),
        change_count_shell(axes=("x", "y", "z"), counts=(2, 3), radius=1, time_offset=time_offset),
    ))

    return Neighborhood(
        components=neighborhood.components,
        combine=neighborhood.combine,
        name="dyadaxes_3d",
        params={"time_offset": time_offset},
    )
