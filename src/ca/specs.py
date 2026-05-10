"""Shared CA runtime specs and result types."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from . import frontiers as frontiers_lib
from . import neighborhoods as neighborhoods_lib
from . import rules as rules_lib


_BOUNDARY_POLICIES = ("none", "fixed", "periodic", "reflective")


def _none_boundary() -> dict[str, Any]:
    return {"policy": "none"}


@dataclass(frozen=True)
class Dynamics:
    """Reusable CA mechanics needed to evolve raw states.

    `Dynamics` deliberately excludes per-episode inputs such as `rule_id`,
    `seed_state`, and `steps`; callers pass those separately for each episode.
    """

    domain: str
    shape: tuple[int, ...]
    rule: Any
    neighborhoods: tuple[Any, ...]
    frontier: Any
    boundary: Mapping[str, Any] = field(default_factory=_none_boundary)
    metadata: Mapping[str, Any] | None = None

    def __init__(
        self,
        domain: str,
        shape: Sequence[int],
        rule: Any,
        neighborhoods: Sequence[Any],
        frontier: Any,
        boundary: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
    ) -> None:
        object.__setattr__(self, "domain", str(domain).lower())
        object.__setattr__(self, "shape", tuple(int(size) for size in shape))
        object.__setattr__(self, "rule", rule)
        object.__setattr__(self, "neighborhoods", tuple(neighborhoods))
        object.__setattr__(self, "frontier", frontier)
        object.__setattr__(self, "boundary", _normalize_boundary(boundary))
        object.__setattr__(self, "metadata", None if metadata is None else dict(metadata))


@dataclass(frozen=True)
class RawEpisode:
    """Raw generated episode before downstream representation or batching."""

    domain: str
    shape: tuple[int, ...]
    rule_id: int
    steps: int
    states: np.ndarray
    coords: np.ndarray | None = None
    metadata: Mapping[str, Any] | None = None


def dynamics_from_spec(spec: Mapping[str, Any]) -> Dynamics:
    """Build runtime `Dynamics` from a JSON-safe manifest-style mapping."""

    spec_dict = dict(spec)
    dynamics_spec = dict(spec_dict.get("dynamics", spec_dict))

    domain = dynamics_spec.get("domain", spec_dict.get("domain"))
    if domain is None:
        raise ValueError("dynamics spec requires domain")

    shape = dynamics_spec.get("shape", spec_dict.get("shape"))
    if shape is None:
        raise ValueError("dynamics spec requires shape")
    shape_tuple = tuple(int(size) for size in shape)

    metadata = dict(dynamics_spec.get("metadata", {}))
    for key in ("dataset_id", "manifest_version"):
        if key in spec_dict and key not in metadata:
            metadata[key] = spec_dict[key]

    return Dynamics(
        domain=str(domain),
        shape=shape_tuple,
        rule=rule_from_spec(_required_field(dynamics_spec, "rule")),
        neighborhoods=neighborhoods_from_spec(
            dynamics_spec.get("neighborhoods", dynamics_spec.get("neighborhood"))
        ),
        frontier=frontier_from_spec(_required_field(dynamics_spec, "frontier"), shape_tuple),
        boundary=dynamics_spec.get("boundary"),
        metadata=metadata or None,
    )


def rule_from_spec(spec: Mapping[str, Any] | str | rules_lib.Rule) -> rules_lib.Rule:
    """Build a supported Phase 1 rule family from a JSON-safe spec."""

    if isinstance(spec, rules_lib.Rule):
        return spec
    spec_dict = _family_spec(spec)
    family = spec_dict["family"]
    params = _params(spec_dict)

    if family == "ar2_modular_0d":
        coefficient_grid = params.get("coefficient_grid", (16, 16))
        return rules_lib.ar2_modular_0d(
            modulus=int(params.get("modulus", 97)),
            coefficient_grid=tuple(int(value) for value in coefficient_grid),
            constant=int(params.get("constant", 1)),
        )
    if family == "dyadrads_1d":
        return rules_lib.dyadrads_1d()
    if family == "dyadaxes_2d":
        return rules_lib.dyadaxes_2d()
    if family == "dyadaxes_3d":
        return rules_lib.dyadaxes_3d()

    raise ValueError(f"unsupported Phase 1 rule family {family!r}")


def neighborhoods_from_spec(spec: Any) -> tuple[neighborhoods_lib.Neighborhood, ...]:
    """Build supported Phase 1 neighborhoods from JSON-safe specs."""

    if spec is None:
        return ()
    if isinstance(spec, neighborhoods_lib.Neighborhood):
        return (spec,)
    if isinstance(spec, Mapping) or isinstance(spec, str):
        return (_neighborhood_from_one_spec(spec),)
    return tuple(_neighborhood_from_one_spec(item) for item in spec)


def _neighborhood_from_one_spec(
    spec: Mapping[str, Any] | str | neighborhoods_lib.Neighborhood,
) -> neighborhoods_lib.Neighborhood:
    if isinstance(spec, neighborhoods_lib.Neighborhood):
        return spec
    spec_dict = _family_spec(spec)
    family = spec_dict["family"]
    params = _params(spec_dict)

    if family == "ar2_0d":
        return neighborhoods_lib.ar2_0d(**params)
    if family == "dyadrads_1d":
        return neighborhoods_lib.dyadrads_1d(**params)
    if family == "dyadaxes_2d":
        return neighborhoods_lib.dyadaxes_2d(**params)
    if family == "dyadaxes_3d":
        return neighborhoods_lib.dyadaxes_3d(**params)

    raise ValueError(f"unsupported Phase 1 neighborhood family {family!r}")


def frontier_from_spec(
    spec: Mapping[str, Any] | str | frontiers_lib.Frontier,
    shape: Sequence[int],
) -> frontiers_lib.Frontier:
    """Build a supported Phase 1 frontier from a JSON-safe spec."""

    if isinstance(spec, frontiers_lib.Frontier):
        return spec
    spec_dict = _family_spec(spec)
    family = spec_dict["family"]

    if family == "time_slice":
        return frontiers_lib.time_slice(shape)

    raise ValueError(f"unsupported Phase 1 frontier family {family!r}")


def _required_field(spec: Mapping[str, Any], key: str) -> Any:
    value = spec.get(key)
    if value is None:
        raise ValueError(f"dynamics spec requires field {key!r}")
    return value


def _family_spec(spec: Mapping[str, Any] | str) -> dict[str, Any]:
    if isinstance(spec, str):
        return {"family": spec}
    spec_dict = dict(spec)
    family = spec_dict.get("family")
    if not isinstance(family, str) or not family:
        raise ValueError("spec requires non-empty string field 'family'")
    spec_dict["family"] = family
    return spec_dict


def _params(spec: Mapping[str, Any]) -> dict[str, Any]:
    params = dict(spec.get("params", {}))
    for key, value in spec.items():
        if key not in {"family", "params", "rule_count"}:
            params.setdefault(key, value)
    return params


def _normalize_boundary(boundary: Mapping[str, Any] | None = None) -> dict[str, Any]:
    if boundary is None:
        return _none_boundary()
    if not isinstance(boundary, Mapping):
        raise TypeError(f"boundary must be a mapping or None, got {type(boundary).__name__}")

    spec = dict(boundary)
    policy = spec.get("policy")
    if not isinstance(policy, str) or not policy:
        raise ValueError("boundary requires non-empty string field 'policy'")

    policy = policy.lower()
    if policy not in _BOUNDARY_POLICIES:
        raise ValueError(f"unknown boundary policy {policy!r}")

    allowed = {"policy"}
    out: dict[str, Any] = {"policy": policy}
    if policy == "fixed":
        allowed.add("value")
        out["value"] = spec.get("value", 0)

    extra = set(spec).difference(allowed)
    if extra:
        raise ValueError(f"unsupported boundary fields: {sorted(extra)}")

    return out


__all__ = [
    "Dynamics",
    "RawEpisode",
    "dynamics_from_spec",
    "frontier_from_spec",
    "neighborhoods_from_spec",
    "rule_from_spec",
]
