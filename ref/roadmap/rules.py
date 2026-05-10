"""Roadmap sketches for future rule families and convenience builders."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Literal


DecodeMode = Literal["lsb_rule_bits"]


def isotropic(
    component: int = 0,
    symmetries: Sequence[Any] = (),
    input_order: str = "lex",
) -> Any:
    """Represent one component modulo a symmetry group."""
    ...


def histographic(component: int = 0, alphabet_size: int | None = None) -> Any:
    """Represent one component by a finite-value histogram."""
    ...


def stochastic(
    source: Any | None = None,
    distribution: Any | None = None,
    params: Mapping[str, Any] | None = None,
) -> Any:
    """Build a stochastic output rule."""
    ...


def any_gate(source: Any) -> Any:
    """Alias for `gate(source, type="any")`."""
    ...


def all_gate(source: Any) -> Any:
    """Alias for `gate(source, type="all")`."""
    ...


def majority_gate(source: Any) -> Any:
    """Alias for `gate(source, type="majority")`."""
    ...


def at_least_gate(source: Any, value: int | float) -> Any:
    """Alias for `gate(source, type="atLeast", value=value)`."""
    ...


def at_most_gate(source: Any, value: int | float) -> Any:
    """Alias for `gate(source, type="atMost", value=value)`."""
    ...


def exactly_gate(source: Any, value: int | float) -> Any:
    """Alias for `gate(source, type="exactly", value=value)`."""
    ...


def min_gate(source: Any, value: int | float) -> Any:
    """Alias for `gate(source, type="min", value=value)`."""
    ...


def max_gate(source: Any, value: int | float) -> Any:
    """Alias for `gate(source, type="max", value=value)`."""
    ...


def clamp_gate(source: Any, min: int | float, max: int | float) -> Any:
    """Alias for `gate(source, type="clamp", min=min, max=max)`."""
    ...


def ceil_gate(source: Any) -> Any:
    """Alias for `gate(source, type="ceil")`."""
    ...


def floor_gate(source: Any) -> Any:
    """Alias for `gate(source, type="floor")`."""
    ...


def binary_lookup(num_bits: int, decode: DecodeMode = "lsb_rule_bits") -> Any:
    """Alias for a binary exhaustive lookup over `num_bits` channel outputs."""
    ...


def modular_ar(
    order: int,
    modulus: int,
    coefficients: Sequence[int] | None = None,
    constant: int = 1,
    decode: str | None = None,
) -> Any:
    """Alias family for modular autoregressive scalar recurrences."""
    ...


def dyadaxes(
    rank: Literal[2, 3],
    primary_gate: Mapping[str, Any] | None = None,
    secondary_gate: Mapping[str, Any] | None = None,
) -> Any:
    """Alias for rank-specific Dyadaxes rule families."""
    ...
