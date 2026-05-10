"""Boundary policy helpers for CA rollout.

Boundary policy ownership lives here, while coordinate-space and native-index
mechanics stay in `ca.loci`. During the NumPy refactor, `loci` should become
the shared NumPy foundation and this module should remain a thin boundary layer
over it.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np

from . import loci


BoundaryLike = Mapping[str, Any] | str | None

_BOUNDARY_POLICIES = ("none", "fixed", "periodic", "reflective")


def none() -> dict[str, Any]:
    """Return the no-boundary policy."""

    return {"policy": "none"}


def fixed(value: Any = 0) -> dict[str, Any]:
    """Return a fixed-fill boundary policy."""

    return {"policy": "fixed", "value": value}


def periodic() -> dict[str, Any]:
    """Return a periodic spatial boundary policy."""

    return {"policy": "periodic"}


def reflective() -> dict[str, Any]:
    """Return a reflective spatial boundary policy."""

    return {"policy": "reflective"}


def normalize(boundary: BoundaryLike = None) -> dict[str, Any]:
    """Normalize strings, mappings, and empty values into a boundary spec."""

    if boundary is None:
        return none()

    raw: dict[str, Any]
    if isinstance(boundary, str):
        raw = {"policy": boundary}
    else:
        raw = dict(boundary)

    raw_policy = raw.get("policy", raw.get("mode", raw.get("type", "none")))
    if raw_policy in (None, ""):
        raw_policy = "none"
    if not isinstance(raw_policy, str):
        raise TypeError(f"boundary policy must be a string, got {type(raw_policy).__name__}")

    policy = raw_policy.lower()
    if policy not in _BOUNDARY_POLICIES:
        raise ValueError(f"unknown boundary policy {policy!r}")

    spec: dict[str, Any] = {"policy": policy}
    if policy == "fixed":
        spec["value"] = raw.get("value", raw.get("fill_value", 0))
    if "coordinate_space" in raw:
        spec["coordinate_space"] = raw["coordinate_space"]
    return spec


def apply_boundary_read(
    state: Any,
    coord: Sequence[int],
    boundary: BoundaryLike = None,
) -> Any:
    """Resolve one canonical read coordinate against one native state."""

    state_array = np.asarray(state)
    space = loci.coordinate_space(tuple(int(size) for size in state_array.shape), steps=1)
    coord_array = np.asarray(tuple(int(value) for value in coord), dtype=np.int64).reshape(1, 4)
    values = np.expand_dims(state_array, axis=0)
    result = loci.gather(coord_array, values, _for_loci(boundary, coordinate_space=space))[0]
    return result.item() if hasattr(result, "item") else result


def gather(coords: Any, values: Any, boundary: BoundaryLike = None) -> Any:
    """Gather `values` at canonical coordinates under a boundary policy."""

    return loci.gather(coords, values, _for_loci(boundary))


def _for_loci(
    boundary: BoundaryLike,
    *,
    coordinate_space: loci.CoordinateSpace | None = None,
) -> dict[str, Any]:
    """Translate normalized CA boundary specs to the current `loci.gather` shape."""

    spec = normalize(boundary)
    out: dict[str, Any] = {}

    if spec["policy"] != "none":
        out["policy"] = spec["policy"]

    if spec["policy"] == "fixed":
        out["value"] = spec.get("value", 0)

    if "coordinate_space" in spec:
        out["coordinate_space"] = spec["coordinate_space"]

    if coordinate_space is not None:
        out["coordinate_space"] = coordinate_space

    return out


__all__ = [
    "apply_boundary_read",
    "fixed",
    "gather",
    "none",
    "normalize",
    "periodic",
    "reflective",
]
