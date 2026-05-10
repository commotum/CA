"""Seed catalog factories built from loci.

This module defines seed families for next-state generation. A seed is the
initial assignment interface: it describes which current or history coordinates
are initialized, what value selected coordinates receive, and what background
value fills the rest.

The construction hierarchy mirrors `neighborhoods.py` and `frontiers.py`:

- `loci.py` owns selector machinery over canonical `[t, x, y, z]` coordinates.
- Core seed families package common initial assignments such as constants,
  scalar history pairs, random initial slices, and selector-backed supports.
- Structured seed families build meaningful geometric supports from loci
  predicates rather than duplicating selector logic.

This keeps seed support construction separate from alphabets, rules, rollout,
tokenization, and dataset assembly. `datasets.py` chooses which seed family is
paired with each named dataset.
"""

from __future__ import annotations

import itertools
import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal

import torch

from . import loci


Metric = Literal["l1", "l2", "linf"]
Stratum = Literal["volume", "shell", "outline", "vertices"]
DedupeMode = Literal["exact", "symmetry"]


@dataclass(frozen=True)
class Seed:
    """Structured seed definition.

    `support` is a selector over initialized coordinates. `support=None` means
    the seed applies to the whole initial support, as with constants. A seed may
    be deterministic through `selected_value`, stochastic through
    `distribution`, or a named family whose renderer handles its placement.
    """

    support: loci.Selector | None
    selected_value: int | None = None
    fill_value: int = 0
    distribution: Any | None = None
    family: str | None = None
    params: Mapping[str, Any] | None = None
    name: str | None = None


def _not_implemented() -> None:
    raise NotImplementedError("seeds.py currently contains catalog specs only")


def _initial_slice(context: Mapping[str, Any]) -> loci.Tensor:
    space = context.get("coordinate_space")
    if space is None:
        space = loci.coordinate_space(context["shape"])
    return loci.absolute_universe(space, t=0)


def _center(center: Mapping[str, int] | Sequence[int] | None) -> dict[str, int]:
    out = {"x": 0, "y": 0, "z": 0}

    if center is None:
        return out

    if isinstance(center, Mapping):
        for axis in out:
            out[axis] = int(center.get(axis, 0))
        return out

    for axis, value in zip(("x", "y", "z"), center):
        out[axis] = int(value)

    return out


def _axis_extents(shape: Sequence[int]) -> dict[str, int]:
    space = loci.coordinate_space(shape)
    extents = {}

    for axis in loci.active_axes(shape):
        values = space.intervals[axis]
        extents[axis] = max(abs(values[0]), abs(values[-1]))

    return extents


def _max_body_radius(metric: Metric, extents: Mapping[str, int]) -> int:
    if not extents:
        return 0

    if metric == "linf":
        return max(extents.values())

    if metric == "l1":
        return sum(extents.values())

    squared = sum(extent * extent for extent in extents.values())
    return math.ceil(math.sqrt(squared))


def _subspace_specs(shape: Sequence[int]) -> list[Seed]:
    space = loci.coordinate_space(shape)
    axes = loci.active_axes(shape)
    specs = []

    for free_count in range(0, len(axes) + 1):
        for free_axes in itertools.combinations(axes, free_count):
            fixed_axes = tuple(axis for axis in axes if axis not in free_axes)

            for fixed_values in itertools.product(*(space.intervals[axis] for axis in fixed_axes)):
                fixed = dict(zip(fixed_axes, fixed_values))
                specs.append(subspace(free_axes=free_axes, fixed=fixed))

    return specs


# ---------------------------------------------------------------------------
# Phase 1 Core Seeds
# ---------------------------------------------------------------------------


def pair(x0: int, x1: int, fill_value: int = 0) -> Seed:
    """Build a two-value scalar history seed.

    This is the deterministic seed family for second-order 0D recurrences.
    The renderer should place `x0` and `x1` according to the dataset's temporal
    history convention.
    """

    x0 = int(x0)
    x1 = int(x1)
    fill_value = int(fill_value)

    return Seed(
        support=None,
        fill_value=fill_value,
        family="pair",
        params={"x0": x0, "x1": x1, "fill_value": fill_value},
    )


def uniform_pair(value_count: int = 97, reject_zero_zero: bool = True) -> Seed:
    """Sample a two-value scalar history seed uniformly.

    `value_count` is the finite value count, usually the alphabet size for the
    scalar recurrence dataset.
    """

    value_count = int(value_count)
    reject_zero_zero = bool(reject_zero_zero)

    return Seed(
        support=None,
        family="uniform_pair",
        params={
            "value_count": value_count,
            "reject_zero_zero": reject_zero_zero,
        },
        distribution={
            "family": "uniform_pair",
            "value_count": value_count,
            "reject_zero_zero": reject_zero_zero,
        },
    )


def bernoulli(
    p_low: float = 0.0,
    p_high: float = 1.0,
    support: str | loci.Selector | Mapping[str, Any] = "initial_slice",
) -> Seed:
    """Sample binary values over a seed support.

    This is a stochastic seed family, separate from structured geometric seed
    enumeration.
    """

    if support == "initial_slice":
        def initial_slice(context: Mapping[str, Any]) -> loci.Tensor:
            space = context.get("coordinate_space")
            if space is None:
                space = loci.coordinate_space(context["shape"])
            return loci.absolute_universe(space, t=0)

        support_selector = loci.selector(
            initial_slice,
            order="none",
            frame="absolute",
        )
    elif isinstance(support, loci.Selector):
        support_selector = support
    else:
        support_selector = None

    return Seed(
        support=support_selector,
        fill_value=0,
        family="bernoulli",
        params={"p_low": p_low, "p_high": p_high, "support": support},
        distribution={
            "family": "bernoulli",
            "p_low": float(p_low),
            "p_high": float(p_high),
        },
    )


def selector_seed(
    selector: loci.Selector,
    selected_value: int = 1,
    fill_value: int = 0,
    distribution: Any | None = None,
) -> Seed:
    """Build a seed from an explicit selector-backed support."""

    return Seed(
        support=selector,
        selected_value=selected_value,
        fill_value=fill_value,
        distribution=distribution,
        family="selector_seed",
        params={
            "selected_value": selected_value,
            "fill_value": fill_value,
        },
    )


def point(
    center: Mapping[str, int] | Sequence[int] | None = None,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select one centered or explicitly positioned seed coordinate."""

    if center is None:
        target = {"t": 0, "x": 0, "y": 0, "z": 0}
    elif isinstance(center, Mapping):
        target = {
            "t": int(center.get("t", 0)),
            "x": int(center.get("x", 0)),
            "y": int(center.get("y", 0)),
            "z": int(center.get("z", 0)),
        }
    else:
        values = tuple(int(value) for value in center)
        target = {"t": 0, "x": 0, "y": 0, "z": 0}

        if len(values) == 4:
            target["t"] = values[0]
            values = values[1:]

        for axis, coord in zip(("x", "y", "z"), values):
            target[axis] = coord

    def initial_slice(context: Mapping[str, Any]) -> loci.Tensor:
        space = context.get("coordinate_space")
        if space is None:
            space = loci.coordinate_space(context["shape"])
        return loci.absolute_universe(space, t=target["t"])

    support = loci.selector(
        initial_slice,
        predicates=tuple(
            loci.coord_eq(axis, coord)
            for axis, coord in target.items()
        ),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="point",
        params={
            "center": target,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


# ---------------------------------------------------------------------------
# Phase 2 Structured Supports
# ---------------------------------------------------------------------------


def subspace(
    free_axes: Sequence[str],
    fixed: Mapping[str, int] | None = None,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select an affine subspace such as a row, column, line, or plane."""

    free_axes = tuple(str(axis) for axis in free_axes)
    fixed = {} if fixed is None else dict(fixed)

    support = loci.selector(
        _initial_slice,
        predicates=tuple(
            loci.coord_eq(axis, int(coord))
            for axis, coord in fixed.items()
            if axis not in free_axes
        ),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="subspace",
        params={
            "free_axes": free_axes,
            "fixed": fixed,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def finite_segment(
    direction: Sequence[int] | str,
    length: int,
    center: Mapping[str, int] | Sequence[int] | None = None,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select a finite segment along an axis or lattice direction."""

    length = int(length)
    center = _center(center)

    if isinstance(direction, str):
        direction_values = {"x": 0, "y": 0, "z": 0}
        direction_values[direction] = 1
    else:
        values = tuple(int(value) for value in direction)
        if len(values) == 4:
            values = values[1:]
        direction_values = {
            axis: value
            for axis, value in zip(("x", "y", "z"), values)
        }

    start = -(length // 2)
    offsets = range(start, start + length)
    points = []
    for offset in offsets:
        points.append([
            center["x"] + offset * direction_values.get("x", 0),
            center["y"] + offset * direction_values.get("y", 0),
            center["z"] + offset * direction_values.get("z", 0),
        ])

    allowed = torch.tensor(points, dtype=torch.long)

    def on_segment(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        projected = loci.axis_project(coords, ("x", "y", "z"))
        matches = projected[:, None, :] == allowed.to(projected.device)[None, :, :]
        return matches.all(dim=-1).any(dim=-1)

    support = loci.selector(
        _initial_slice,
        predicates=(on_segment,),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="finite_segment",
        params={
            "direction": direction,
            "length": length,
            "center": center,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def body(
    metric: Metric,
    stratum: Stratum,
    radius: int | None = None,
    extents: Mapping[str, int] | None = None,
    center: Mapping[str, int] | Sequence[int] | None = None,
    thickness: int = 1,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select a compact metric body such as a block, diamond, ring, or shell."""

    center = _center(center)
    radius = 1 if radius is None else int(radius)
    thickness = int(thickness)

    def body_predicate(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        space = context.get("coordinate_space")
        axes = loci.active_axes(space if space is not None else context["shape"])

        if metric == "linf":
            projected = loci.axis_project(coords, axes)
            center_values = torch.tensor(
                [center[axis] for axis in axes],
                dtype=projected.dtype,
                device=projected.device,
            )
            relative = projected - center_values
            extent_values = torch.tensor(
                [int(extents.get(axis, radius)) if extents else radius for axis in axes],
                dtype=projected.dtype,
                device=projected.device,
            )
            abs_relative = relative.abs()
            within = (abs_relative <= extent_values).all(dim=-1)
            boundary_axes = (abs_relative == extent_values).sum(dim=-1)

            if stratum == "volume":
                return within

            if stratum == "shell":
                return within & (boundary_axes >= 1)

            if stratum == "outline":
                return within & (boundary_axes >= max(1, len(axes) - 1))

            return within & (boundary_axes == len(axes))

        distances = loci.norm(coords, axes, metric=metric, center=center)

        if stratum == "volume":
            return distances <= radius

        if metric == "l2":
            shell = (distances > radius - thickness) & (distances <= radius)
        else:
            shell = distances == radius

        projected = loci.axis_project(coords, axes)
        center_values = torch.tensor(
            [center[axis] for axis in axes],
            dtype=projected.dtype,
            device=projected.device,
        )
        relative = projected - center_values
        nonzero_axes = (relative != 0).sum(dim=-1)
        zero_axes = len(axes) - nonzero_axes

        if stratum == "shell":
            return shell

        if stratum == "outline":
            if len(axes) <= 2:
                return shell
            return shell & (zero_axes >= 1)

        return shell & (nonzero_axes == 1)

    support = loci.selector(
        _initial_slice,
        predicates=(body_predicate,),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="body",
        params={
            "metric": metric,
            "stratum": stratum,
            "radius": radius,
            "extents": extents,
            "center": center,
            "thickness": thickness,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def compound(
    kind: str,
    components: Sequence[Seed | Mapping[str, Any]] | None = None,
    axes: Sequence[str] | None = None,
    signs: Sequence[int] | None = None,
    extent: int | None = None,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select a union-style compound support such as plus or X shapes."""

    kind = str(kind)
    axes = ("x", "y", "z") if axes is None else tuple(str(axis) for axis in axes)
    signs = tuple(int(sign) for sign in signs) if signs is not None else None
    extent = None if extent is None else int(extent)

    if components:
        selectors = tuple(component.support for component in components if isinstance(component, Seed))

        def has_any_component(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
            result = torch.zeros(coords.shape[0], dtype=torch.bool, device=coords.device)
            for selector in selectors:
                selection = loci.select(selector, context)
                selected = selection.coords
                matches = coords[:, None, :] == selected.to(coords.device)[None, :, :]
                result = result | matches.all(dim=-1).any(dim=-1)
            return result

        support = loci.selector(
            _initial_slice,
            predicates=(has_any_component,),
            order="none",
            frame="absolute",
        )
    else:
        def compound_predicate(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
            projected = loci.axis_project(coords, axes)
            abs_projected = projected.abs()

            if extent is not None:
                in_extent = (abs_projected <= extent).all(dim=-1)
            else:
                in_extent = torch.ones(projected.shape[0], dtype=torch.bool, device=projected.device)

            if kind in ("axial-star", "plus"):
                return in_extent & ((projected != 0).sum(dim=-1) <= 1)

            if kind in ("diagonal-star", "x"):
                if signs is None:
                    return in_extent & (abs_projected == abs_projected[:, :1]).all(dim=-1)

                sign_values = torch.tensor(signs, dtype=projected.dtype, device=projected.device)
                signed = projected * sign_values
                return in_extent & (signed == signed[:, :1]).all(dim=-1)

            return torch.zeros(projected.shape[0], dtype=torch.bool, device=projected.device)

        support = loci.selector(
            _initial_slice,
            predicates=(compound_predicate,),
            order="none",
            frame="absolute",
        )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="compound",
        params={
            "kind": kind,
            "axes": axes,
            "signs": signs,
            "extent": extent,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def region(
    kind: str,
    axis: str | None = None,
    sides: Mapping[str, str] | None = None,
    bounds: Mapping[str, tuple[int, int]] | None = None,
    coord: int = 0,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select a large region such as a half-space, orthant, slab, or interface."""

    kind = str(kind)
    sides = {} if sides is None else dict(sides)
    bounds = {} if bounds is None else dict(bounds)

    def compare(values: loci.Tensor, side: str, threshold: int) -> loci.Tensor:
        if side in ("le", "<="):
            return values <= threshold
        if side in ("lt", "<"):
            return values < threshold
        if side in ("ge", ">="):
            return values >= threshold
        if side in ("gt", ">"):
            return values > threshold
        return values == threshold

    def region_predicate(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        if kind == "half-space":
            values = loci.axis_project(coords, (axis,)).squeeze(-1)
            return compare(values, sides.get(axis, "ge"), int(coord))

        if kind == "orthant":
            masks = []
            for side_axis, side in sides.items():
                values = loci.axis_project(coords, (side_axis,)).squeeze(-1)
                masks.append(compare(values, side, int(coord)))
            return loci.combine_masks(masks, op="and")

        if kind == "slab":
            masks = []
            for bound_axis, (low, high) in bounds.items():
                values = loci.axis_project(coords, (bound_axis,)).squeeze(-1)
                masks.append((values >= int(low)) & (values <= int(high)))
            return loci.combine_masks(masks, op="and")

        if kind == "interface":
            values = loci.axis_project(coords, (axis,)).squeeze(-1)
            return values == int(coord)

        return torch.zeros(coords.shape[0], dtype=torch.bool, device=coords.device)

    support = loci.selector(
        _initial_slice,
        predicates=(region_predicate,),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="region",
        params={
            "kind": kind,
            "axis": axis,
            "sides": sides,
            "bounds": bounds,
            "coord": int(coord),
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def periodic(
    kind: str,
    axes: Sequence[str],
    step: int = 2,
    phase: int = 0,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select a periodic support such as parity, product lattice, or grid lattice."""

    kind = str(kind)
    axes = tuple(str(axis) for axis in axes)
    step = int(step)
    phase = int(phase)

    def periodic_predicate(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        if kind == "parity":
            return loci.mod_eq(loci.sum_axes(coords, axes), step, phase)

        projected = loci.axis_project(coords, axes)
        hits = torch.remainder(projected - phase, step) == 0

        if kind in ("product-lattice", "sparse-lattice"):
            return hits.all(dim=-1)

        if kind == "grid-lattice":
            return hits.any(dim=-1)

        return torch.zeros(coords.shape[0], dtype=torch.bool, device=coords.device)

    support = loci.selector(
        _initial_slice,
        predicates=(periodic_predicate,),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="periodic",
        params={
            "kind": kind,
            "axes": axes,
            "step": step,
            "phase": phase,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def fractal(kind: str, params: Mapping[str, Any], value: int = 1, fill_value: int = 0) -> Seed:
    """Select a future fractal-style support compiled to loci predicates."""

    predicate_fn = params["predicate"]
    support = loci.selector(
        _initial_slice,
        predicates=(loci.predicate(predicate_fn, params, name=str(kind)),),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="fractal",
        params={
            "kind": kind,
            "params": dict(params),
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def spiral(kind: str, params: Mapping[str, Any], value: int = 1, fill_value: int = 0) -> Seed:
    """Select a future spiral-style support compiled to loci predicates."""

    predicate_fn = params["predicate"]
    support = loci.selector(
        _initial_slice,
        predicates=(loci.predicate(predicate_fn, params, name=str(kind)),),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="spiral",
        params={
            "kind": kind,
            "params": dict(params),
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def path(
    points: Sequence[Sequence[int]],
    thickness: int = 0,
    value: int = 1,
    fill_value: int = 0,
) -> Seed:
    """Select a path through explicit lattice points."""

    canonical_points = []
    for point_values in points:
        values = tuple(int(value) for value in point_values)
        if len(values) == 4:
            canonical_points.append(values)
            continue

        coords = [0, 0, 0, 0]
        for index, value in enumerate(values, start=1):
            coords[index] = value
        canonical_points.append(tuple(coords))

    point_tensor = torch.tensor(canonical_points, dtype=torch.long)
    thickness = int(thickness)

    def path_predicate(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        deltas = coords[:, None, :] - point_tensor.to(coords.device)[None, :, :]
        distances = deltas[:, :, 1:].abs().max(dim=-1).values
        same_time = deltas[:, :, 0] == 0
        return (same_time & (distances <= thickness)).any(dim=-1)

    support = loci.selector(
        _initial_slice,
        predicates=(path_predicate,),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=int(value),
        fill_value=int(fill_value),
        family="path",
        params={
            "points": tuple(canonical_points),
            "thickness": thickness,
            "value": int(value),
            "fill_value": int(fill_value),
        },
    )


def transform(
    seed_spec: Seed,
    invert: bool = False,
    reflect: Sequence[str] = (),
    permute: Sequence[str] | None = None,
    rotate: Any | None = None,
) -> Seed:
    """Transform a seed support.

    Phase 2 supports complement/invert. Orientation transforms remain explicit
    stubs until the corresponding coordinate-transform helpers exist.
    """

    seed = seed_spec

    if reflect or permute is not None or rotate is not None:
        _not_implemented()

    if not invert:
        return seed

    def transformed_predicate(coords: loci.Tensor, context: Mapping[str, Any]) -> loci.Tensor:
        selection = loci.select(seed.support, context)
        selected = selection.coords
        matches = coords[:, None, :] == selected.to(coords.device)[None, :, :]
        mask = matches.all(dim=-1).any(dim=-1)

        return ~mask

    support = loci.selector(
        _initial_slice,
        predicates=(transformed_predicate,),
        order="none",
        frame="absolute",
    )

    return Seed(
        support=support,
        selected_value=seed.selected_value,
        fill_value=seed.fill_value,
        distribution=seed.distribution,
        family="transform",
        params={
            "seed_spec": seed_spec,
            "invert": invert,
            "reflect": tuple(reflect),
            "permute": permute,
            "rotate": rotate,
        },
    )


# ---------------------------------------------------------------------------
# Rendering and Dedupe
# ---------------------------------------------------------------------------


def render(seed: Seed, shape: Sequence[int], rng: Any | None = None) -> Any:
    """Render a seed spec into an initial raw state or mask.

    Rendering is where selector supports are materialized for a concrete shape.
    It should use `loci.select` or `loci.mask` rather than reimplementing
    coordinate logic.
    """

    shape = tuple(int(size) for size in shape)

    if seed.family == "pair":
        params = seed.params or {}
        return torch.tensor((params["x0"], params["x1"]), dtype=torch.long)

    if seed.family == "uniform_pair":
        params = seed.params or {}
        value_count = int(params["value_count"])

        while True:
            values = torch.randint(value_count, (2,), generator=rng, dtype=torch.long)
            if not params["reject_zero_zero"] or bool(values.any()):
                return values

    value = seed.fill_value if seed.selected_value is None else seed.selected_value
    output = torch.full(shape, int(value), dtype=torch.long)

    if seed.support is None:
        return output

    output = torch.full(shape, int(seed.fill_value), dtype=torch.long)
    space = loci.coordinate_space(shape)
    context = {"shape": shape, "coordinate_space": space}
    selection = loci.select(seed.support, context)
    selected = selection.coords

    if selected is None or selected.numel() == 0:
        return output

    indices = loci.native_indices(selected, space)

    if seed.distribution and seed.distribution.get("family") == "bernoulli":
        p_low = float(seed.distribution["p_low"])
        p_high = float(seed.distribution["p_high"])
        p = p_low + (p_high - p_low) * float(torch.rand((), generator=rng))
        samples = (torch.rand(shape, generator=rng) < p).long()
        output[indices] = samples[indices]
        return output

    output[indices] = int(seed.selected_value)
    return output


def dedupe(
    specs: Sequence[Seed],
    shape: Sequence[int],
    mode: DedupeMode = "exact",
) -> list[Seed]:
    """Remove duplicate rendered seed supports for a concrete shape."""

    if mode != "exact":
        _not_implemented()

    kept = []
    seen = set()

    for spec in specs:
        rendered = render(spec, shape)
        key = rendered.cpu().contiguous().numpy().tobytes()

        if key in seen:
            continue

        seen.add(key)
        kept.append(spec)

    return kept


# ---------------------------------------------------------------------------
# Phase 3 Structured Groups and Aliases
# ---------------------------------------------------------------------------


def structured(
    shape: Sequence[int],
    include_subspaces: bool = True,
    include_bodies: bool = True,
    include_compounds: bool = True,
    include_regions: bool = True,
    include_periodic: bool = True,
    dedupe: DedupeMode = "exact",
) -> list[Seed]:
    """Enumerate canonical structured seed specs.

    This generates dimension-polymorphic seed specs, expands centered metric
    bodies across every meaningful radius for the target shape, adds inverted
    versions of every selector-backed seed, and dedupes collapsed supports after
    rendering.
    """

    shape = tuple(int(size) for size in shape)
    axes = loci.active_axes(shape)
    extents = _axis_extents(shape)
    specs: list[Seed] = []

    if include_subspaces:
        specs.extend(_subspace_specs(shape))

    if include_bodies and axes:
        for metric in ("linf", "l1", "l2"):
            max_radius = _max_body_radius(metric, extents)

            for radius in range(1, max_radius + 1):
                for stratum in ("volume", "shell", "outline", "vertices"):
                    specs.append(body(metric=metric, stratum=stratum, radius=radius))

    if include_compounds and axes:
        for extent in range(1, _max_body_radius("linf", extents) + 1):
            specs.append(compound(kind="plus", axes=axes, extent=extent))

            if len(axes) >= 2:
                specs.append(compound(kind="x", axes=axes[:2], extent=extent))

    if include_regions and axes:
        first_axis = axes[0]
        specs.append(region(kind="half-space", axis=first_axis, sides={first_axis: "ge"}, coord=0))
        specs.append(region(kind="interface", axis=first_axis, coord=0))

        sides = {axis: "ge" for axis in axes}
        specs.append(region(kind="orthant", sides=sides, coord=0))

    if include_periodic and axes:
        for axis in axes:
            specs.append(periodic(kind="grid-lattice", axes=(axis,)))

        if len(axes) == 3:
            for parity_axes in itertools.combinations(axes, 2):
                specs.append(periodic(kind="parity", axes=parity_axes))

        specs.append(periodic(kind="parity", axes=axes))
        specs.append(periodic(kind="product-lattice", axes=axes))
        specs.append(periodic(kind="grid-lattice", axes=axes))

    specs.extend(transform(spec, invert=True) for spec in tuple(specs) if spec.support is not None)

    if dedupe is None:
        return specs

    return globals()["dedupe"](specs, shape, mode=dedupe)


def constant(value: int) -> Seed:
    """Fill the whole initial support with one value.

    This covers all-dead and all-live starts for later experiments. Structured
    seeds intentionally do not include this family directly.
    """

    value = int(value)

    return Seed(
        support=None,
        selected_value=value,
        fill_value=value,
        family="constant",
        params={"value": value},
    )
