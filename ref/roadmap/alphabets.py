"""Roadmap sketches for future value-space families."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal


@dataclass(frozen=True)
class IntegerSpace:
    """Discrete integer value space for future number-based systems."""

    lower: int | None = None
    upper: int | None = None
    family: str = "integer_space"
    params: Mapping[str, Any] | None = None
    name: str | None = None


@dataclass(frozen=True)
class RealInterval:
    """Continuous scalar interval for future continuous systems."""

    low: float = 0.0
    high: float = 1.0
    closed: bool = True
    family: str = "real_interval"
    params: Mapping[str, Any] | None = None
    name: str | None = None


def composite(
    layers: Mapping[str, Any],
    mode: Literal["product", "tagged_union"] = "product",
) -> Any:
    """Build a finite composite alphabet from finite layers."""
    ...


def integer_space(lower: int | None = 0, upper: int | None = None) -> IntegerSpace:
    """Build an integer value space for future number-based systems."""
    ...


def real_interval(low: float = 0.0, high: float = 1.0, closed: bool = True) -> RealInterval:
    """Build a continuous scalar interval for future continuous systems."""
    ...
