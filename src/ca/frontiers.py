"""Frontier catalog factories built from loci.

This module defines named frontier families for cellular-automata style
next-state generation. A frontier is an update-site interface: it selects which
absolute coordinates in the current state slice are allowed to update. The
generator derives the corresponding next-state write coordinates.

The construction hierarchy mirrors `neighborhoods.py`:

- `loci.py` owns the minimal tensor selector machinery: absolute coordinate
  universes, predicates, mask algebra, ordering, and coordinate/index
  conversion.
- Singular frontiers are built directly from `loci.py` primitives. Each
  singular frontier should describe one coherent update-site locus, such as the
  full current slice, a row, a subspace, a parity sublattice, or a metric
  region.
- Compound or multi-component frontiers are built by composing singular
  frontiers. They should combine component supports with explicit Boolean
  semantics, normally OR for update eligibility.

This keeps low-level selector logic centralized in `loci.py`, keeps simple
frontiers reusable, and prevents composite schedules from duplicating primitive
coordinate/predicate construction.

The default convention follows Wolfram-style next-state updates: frontiers
select current-state update sites at time `t`; neighborhoods read around those
sites; rules write the corresponding next-state values at time `t+1`.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal

from . import loci


CombineMode = Literal["or", "and", "xor"]
Metric = Literal["l1", "l2", "linf"]
Region = Literal["filled", "shell"]


@dataclass(frozen=True)
class Frontier:
    """Structured frontier definition.

    `components` stores one or more absolute-coordinate loci selectors.
    Singular frontiers use one component. Compound frontiers use multiple
    components and combine them with `combine`, usually OR, to determine the
    active update-site support for the current state slice.
    """

    components: tuple[loci.Selector, ...]
    combine: CombineMode = "or"
    name: str | None = None
    params: Mapping[str, Any] | None = None


def _not_implemented() -> None:
    raise NotImplementedError("frontiers.py currently contains catalog specs only")


# ---------------------------------------------------------------------------
# Phase 1 Singular Frontier
# ---------------------------------------------------------------------------


def time_slice(shape: Sequence[int]) -> Frontier:
    """Select the full current state slice.

    This is the default full-throttle cellular-automaton frontier: every active
    spatial site at the current time `t` is eligible to update. The selected
    coordinates are current-state sites `[t, x, y, z]`; the generator maps them
    to `[t+1, x, y, z]` when writing.

    This is a singular frontier built directly from `loci.absolute_universe`
    restricted to the current time and wrapped in `loci.selector`.
    """

    space = loci.coordinate_space(shape)

    universe = loci.absolute_universe(space, t=0)
    component = loci.selector(
        universe,
        order="lex",
        frame="absolute",
    )

    return Frontier(
        components=(component,),
        name="time_slice",
        params={"t": 0},
    )


# ---------------------------------------------------------------------------
# Phase 2 General Families
# ---------------------------------------------------------------------------


def where(predicates: Sequence[loci.PredicateFn] = ()) -> Frontier:
    """Select current update sites satisfying arbitrary predicates.

    This is the generic current-slice frontier. It should start from the
    current-time `loci.absolute_universe`, apply the provided predicates, and
    return the selected absolute update-site coordinates.
    """

    _not_implemented()


def schedule_class(modulus: int, phase: int = 0) -> Frontier:
    """Select current update times in a congruence class.

    This is a time-scheduled sub-frontier over current update sites. It selects
    sites whose current time coordinate satisfies `t % modulus == phase`.

    It should be derived from `loci.coord_eq`/`loci.mod_eq` style predicate
    machinery over the absolute time coordinate, not from a separate schedule
    primitive.
    """

    _not_implemented()


def spatial_subspace(
    free_axes: Sequence[str],
    fixed: Mapping[str, int],
) -> Frontier:
    """Select a row, column, plane, point, or lower-rank spatial flat.

    `free_axes` names the spatial axes allowed to vary. `fixed` gives constant
    coordinates for the remaining active spatial axes. This builds singular
    current-slice frontiers such as one row in 2D or one plane in 3D.

    It should be derived from the current-time absolute universe plus
    `loci.coord_eq` predicates on fixed spatial axes.
    """

    _not_implemented()


def diagonal(
    axes: Sequence[str],
    signs: Sequence[int],
    bias: int = 0,
) -> Frontier:
    """Select a diagonal or anti-diagonal spatial frontier.

    The selected current update sites satisfy a linear equality over projected
    spatial coordinates. Different sign choices produce main diagonals,
    anti-diagonals, and higher-dimensional diagonal flats.

    It should be built from `loci.axis_project` and a generic `loci.predicate`
    over absolute current-slice coordinates.
    """

    _not_implemented()


def parity_sublattice(
    axes: Sequence[str],
    phase: int = 0,
    phase_expr: str | None = None,
) -> Frontier:
    """Select a parity or checkerboard sublattice in the current slice.

    With `axes=("x", "y")` and `phase=0`, this selects one checkerboard color.
    `phase_expr` may later express time-alternating phases such as parity tied
    to the current time coordinate.

    It should be derived from `loci.axis_project`, `loci.sum_axes`, and
    `loci.mod_eq`.
    """

    _not_implemented()


def metric_region(
    axes: Sequence[str],
    metric: Metric,
    region: Region,
    radius: int,
    center: Mapping[str, int] | None = None,
) -> Frontier:
    """Select a metric region in the current slice.

    Filled regions use `norm <= radius`; shells use `norm == radius`. This
    covers current-slice diamonds, squares, circles/spheres, shells, and rings.

    It should be built from `loci.norm` plus ordinary comparison predicates over
    the absolute current-slice coordinate grid.
    """

    _not_implemented()


def ring_growth(
    axes: Sequence[str],
    metric: Metric = "l1",
    center: Mapping[str, int] | None = None,
    radius_expr: str = "t",
    filled: bool = False,
) -> Frontier:
    """Select a current-slice ring or filled region whose radius changes over time.

    This is a time-dependent metric frontier. With `radius_expr="t"`, the
    selected shell grows with the current update time. With `filled=True`, the
    selected region is the filled ball up to that radius.

    It should be derived from the same loci pieces as `metric_region`, with a
    predicate that evaluates the radius expression from the current coordinate
    context.
    """

    _not_implemented()


def active_wavefront(offset_family: Any, active_value: int = 1) -> Frontier:
    """Select current sites adjacent to active state according to an offset family.

    This is a state-dependent frontier: a current update site is selected when
    some related source coordinate, usually a neighboring current-state cell,
    has `active_value`.

    It should be derived from `loci.state_exists` using a neighborhood-style
    offset selector. The offset family is not a new frontier primitive; it is a
    reusable read locus used as a predicate over candidate update sites.
    """

    _not_implemented()


def compose(
    components: Sequence[Frontier],
    combine: CombineMode = "or",
) -> Frontier:
    """Compose singular or already-structured frontiers.

    With `combine="or"`, any component may make a current site eligible to
    update. Other Boolean modes are available for intersections or parity-style
    combinations, but Phase 1 full-throttle frontiers should not need them.
    """

    _not_implemented()


# ---------------------------------------------------------------------------
# Phase 3 Aliases
# ---------------------------------------------------------------------------


def skipped_slices(stride: int = 2, offset: int = 0) -> Frontier:
    """Alias for selecting update times in a repeating schedule class.

    This derives from `schedule_class(modulus=stride, phase=offset)`.
    """

    _not_implemented()


def row(axis: str = "y", value: int = 0) -> Frontier:
    """Alias for an axis-fixed spatial subspace.

    In 2D, `row(axis="y", value=0)` selects the current-slice row with
    `y == 0`. It should derive from `spatial_subspace`.
    """

    _not_implemented()


def plane(axis: str = "z", value: int = 0) -> Frontier:
    """Alias for a single fixed-axis plane in 3D.

    `plane(axis="z", value=0)` selects the current-slice plane with `z == 0`.
    It should derive from `spatial_subspace`.
    """

    _not_implemented()


def moving_subspace(
    axis: str,
    value_expr: str = "t",
    wrap: bool = True,
) -> Frontier:
    """Alias for a time-dependent fixed-axis subspace.

    This selects a row, column, or plane whose fixed coordinate depends on the
    current update time. With `wrap=True`, the moving coordinate wraps over the
    active spatial interval.

    It should derive from `spatial_subspace` plus a time-dependent predicate,
    rather than introducing a separate frontier primitive.
    """

    _not_implemented()
