"""Roadmap sketches for seed features not supported by runtime code yet."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any


def symmetry_dedupe(specs: Sequence[Any], shape: Sequence[int]) -> list[Any]:
    """Remove duplicate seed supports modulo a future symmetry group."""
    ...


def transform_orientation(
    seed_spec: Any,
    reflect: Sequence[str] = (),
    permute: Sequence[str] | None = None,
    rotate: Any | None = None,
) -> Any:
    """Reflect, permute, or rotate seed supports once coordinate transforms exist."""
    ...
