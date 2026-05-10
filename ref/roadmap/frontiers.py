"""Roadmap sketches for future frontier families.

These are intentionally outside `src/ca` so they do not appear as supported
runtime API. Before moving any item back into `src/ca/frontiers.py`, choose
whether frontier factories are shape-bound executable selectors or deferred
specs with a separate materialization step.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Literal


Metric = Literal["l1", "l2", "linf"]
Region = Literal["filled", "shell"]
CombineMode = Literal["or", "and", "xor"]


def where(predicates: Sequence[Any] = ()) -> Any:
    """Select current update sites satisfying arbitrary predicates.

    This is the generic current-slice frontier. It should start from the
    current-time loci absolute universe, apply the provided predicates, and
    return selected absolute update-site coordinates.
    """
    ...


def schedule_class(modulus: int, phase: int = 0) -> Any:
    """Select current update times in a congruence class."""
    ...


def spatial_subspace(
    free_axes: Sequence[str],
    fixed: Mapping[str, int],
) -> Any:
    """Select a row, column, plane, point, or lower-rank spatial flat."""
    ...


def diagonal(
    axes: Sequence[str],
    signs: Sequence[int],
    bias: int = 0,
) -> Any:
    """Select a diagonal or anti-diagonal spatial frontier."""
    ...


def parity_sublattice(
    axes: Sequence[str],
    phase: int = 0,
    phase_expr: str | None = None,
) -> Any:
    """Select a parity or checkerboard sublattice in the current slice."""
    ...


def metric_region(
    axes: Sequence[str],
    metric: Metric,
    region: Region,
    radius: int,
    center: Mapping[str, int] | None = None,
) -> Any:
    """Select a metric region in the current slice."""
    ...


def ring_growth(
    axes: Sequence[str],
    metric: Metric = "l1",
    center: Mapping[str, int] | None = None,
    radius_expr: str = "t",
    filled: bool = False,
) -> Any:
    """Select a current-slice ring or filled region whose radius changes over time."""
    ...


def active_wavefront(offset_family: Any, active_value: int = 1) -> Any:
    """Select current sites adjacent to active state according to an offset family."""
    ...


def compose(
    components: Sequence[Any],
    combine: CombineMode = "or",
) -> Any:
    """Compose singular or already-structured frontiers."""
    ...


def skipped_slices(stride: int = 2, offset: int = 0) -> Any:
    """Alias for selecting update times in a repeating schedule class."""
    ...


def row(axis: str = "y", value: int = 0) -> Any:
    """Alias for an axis-fixed spatial subspace."""
    ...


def plane(axis: str = "z", value: int = 0) -> Any:
    """Alias for a single fixed-axis plane in 3D."""
    ...


def moving_subspace(
    axis: str,
    value_expr: str = "t",
    wrap: bool = True,
) -> Any:
    """Alias for a time-dependent fixed-axis subspace."""
    ...
