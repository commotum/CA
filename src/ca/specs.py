"""Shared CA runtime specs and result types."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from . import boundary as boundary_lib


@dataclass(frozen=True)
class Dynamics:
    """Reusable CA mechanics needed to evolve raw states.

    `Dynamics` deliberately excludes per-episode inputs such as `rule_id`,
    `seed_state`, and `steps`; PE passes those separately for each stream row.
    """

    domain: str
    shape: tuple[int, ...]
    rule: Any
    neighborhoods: tuple[Any, ...]
    frontier: Any
    boundary: Mapping[str, Any] = field(default_factory=boundary_lib.none)
    metadata: Mapping[str, Any] | None = None

    def __init__(
        self,
        domain: str,
        shape: Sequence[int],
        rule: Any,
        neighborhoods: Sequence[Any],
        frontier: Any,
        boundary: Mapping[str, Any] | str | None = None,
        metadata: Mapping[str, Any] | None = None,
    ) -> None:
        object.__setattr__(self, "domain", str(domain).lower())
        object.__setattr__(self, "shape", tuple(int(size) for size in shape))
        object.__setattr__(self, "rule", rule)
        object.__setattr__(self, "neighborhoods", tuple(neighborhoods))
        object.__setattr__(self, "frontier", frontier)
        object.__setattr__(self, "boundary", boundary_lib.normalize(boundary))
        object.__setattr__(self, "metadata", None if metadata is None else dict(metadata))


@dataclass(frozen=True)
class RawEpisode:
    """Raw generated episode before PE tokenization or batching."""

    domain: str
    shape: tuple[int, ...]
    rule_id: int
    steps: int
    states: np.ndarray
    coords: np.ndarray | None = None
    metadata: Mapping[str, Any] | None = None


__all__ = [
    "Dynamics",
    "RawEpisode",
]
