"""Tests for JSON-safe CA spec helpers."""

import numpy as np
import pytest

import ca


def test_dynamics_from_spec_builds_phase1_runtime_objects() -> None:
    manifest = {
        "dataset_id": "2d-dyadaxes",
        "manifest_version": "v1",
        "domain": "t+2d",
        "shape": [3, 3],
        "dynamics": {
            "neighborhood": {"family": "dyadaxes_2d"},
            "frontier": {"family": "time_slice"},
            "rule": {"family": "dyadaxes_2d", "rule_count": 256},
            "boundary": {"policy": "fixed", "value": 0},
        },
    }

    dynamics = ca.dynamics_from_spec(manifest)
    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=np.ones((3, 3), dtype=np.int64),
        steps=2,
    )

    assert dynamics.domain == "t+2d"
    assert dynamics.shape == (3, 3)
    assert dynamics.frontier.family == "time_slice"
    assert ca.rule_count(dynamics.rule) == 256
    assert dynamics.metadata == {"dataset_id": "2d-dyadaxes", "manifest_version": "v1"}
    assert episode.states.shape == (2, 3, 3)


def test_dynamics_from_spec_accepts_plural_neighborhood_specs() -> None:
    spec = {
        "domain": "t+1d",
        "shape": [3],
        "rule": "dyadrads_1d",
        "neighborhoods": [{"family": "dyadrads_1d"}],
        "frontier": "time_slice",
        "boundary": {"policy": "periodic"},
    }

    dynamics = ca.dynamics_from_spec(spec)

    assert len(dynamics.neighborhoods) == 1
    assert dynamics.boundary == {"policy": "periodic"}


def test_dynamics_from_spec_rejects_old_full_next_slice_name() -> None:
    spec = {
        "domain": "t+1d",
        "shape": [3],
        "rule": "dyadrads_1d",
        "neighborhood": {"family": "dyadrads_1d"},
        "frontier": "full_next_slice",
    }

    with pytest.raises(ValueError, match="unsupported Phase 1 frontier"):
        ca.dynamics_from_spec(spec)
