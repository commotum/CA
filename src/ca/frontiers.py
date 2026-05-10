"""Frontier catalog factories built from loci.

This module defines named frontier families for cellular-automata style
next-state generation. A frontier is an update-site interface: it selects which
absolute coordinates in the current state slice are allowed to update. The
generator derives the corresponding next-state write coordinates.

The construction hierarchy mirrors `neighborhoods.py`:

- `loci.py` owns the minimal tensor selector machinery: absolute coordinate
  universes, predicates, mask algebra, ordering, and coordinate/index
  conversion.
- Frontiers are built directly from `loci.py` primitives. The supported
  executable frontier is the full current slice.

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
    family: str | None = None


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
        family="time_slice",
    )
