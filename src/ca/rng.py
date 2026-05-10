"""Deterministic RNG helpers for CA episode generation.

Phase 1 keeps this module as the stable target for NumPy-compatible RNG
primitives. The old torch-generator path is replaced in the NumPy pass.
"""

from __future__ import annotations

__all__: list[str] = []
