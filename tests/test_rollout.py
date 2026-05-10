"""Tests for rollout behavior."""

from types import SimpleNamespace

import numpy as np
import pytest

import ca
from ca import frontiers, neighborhoods, rules
from ca.specs import RawEpisode


def test_ar2_rollout_returns_raw_episode() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.full_next_slice(()),
        boundary={},
    )

    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=np.array([1, 2]),
        steps=4,
    )

    assert isinstance(episode, RawEpisode)
    assert isinstance(episode.states, np.ndarray)
    assert episode.domain == "t+0d"
    assert episode.shape == ()
    assert episode.rule_id == 0
    assert episode.steps == 4
    assert episode.states.tolist() == [2, 3, 4, 5]
    assert episode.coords is not None
    assert episode.coords.tolist() == [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [2, 0, 0, 0],
        [3, 0, 0, 0],
    ]


def test_spatial_lookup_rule_zero_outputs_zero_state() -> None:
    dynamics = ca.Dynamics(
        domain="t+1d",
        shape=(3,),
        rule=rules.dyadrads_1d(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.full_next_slice((3,)),
        boundary={"policy": "fixed", "value": 0},
    )

    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=np.array([1, 0, 1]),
        steps=2,
    )

    assert episode.states.tolist() == [[1, 0, 1], [0, 0, 0]]
    assert episode.coords is not None
    assert episode.coords.shape == (6, 4)


def test_rollout_can_skip_coord_materialization() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.full_next_slice(()),
        boundary={},
    )

    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=np.array([1, 2]),
        steps=2,
        return_coords=False,
    )

    assert episode.coords is None


def test_dynamics_normalizes_boundary_policy() -> None:
    dynamics = ca.Dynamics(
        domain="t+1d",
        shape=(3,),
        rule=rules.dyadrads_1d(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.full_next_slice((3,)),
        boundary="periodic",
    )

    assert dynamics.boundary == {"policy": "periodic"}


def test_rollout_rejects_unsupported_frontier() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=SimpleNamespace(family="partial"),
        boundary={},
    )

    with pytest.raises(NotImplementedError):
        ca.rollout(
            dynamics=dynamics,
            rule_id=0,
            seed_state=np.array([1, 2]),
            steps=2,
        )


def test_rollout_rejects_shape_mismatch() -> None:
    dynamics = ca.Dynamics(
        domain="t+1d",
        shape=(4,),
        rule=rules.dyadrads_1d(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.full_next_slice((4,)),
        boundary={"policy": "fixed", "value": 0},
    )

    with pytest.raises(ValueError, match="dynamics.shape"):
        ca.rollout(
            dynamics=dynamics,
            rule_id=0,
            seed_state=np.array([1, 0, 1]),
            steps=2,
        )


def test_rollout_rejects_domain_shape_mismatch_before_coord_materialization() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(3,),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.full_next_slice((3,)),
        boundary={},
    )

    with pytest.raises(ValueError, match="requires spatial rank"):
        ca.rollout(
            dynamics=dynamics,
            rule_id=0,
            seed_state=np.array([1, 2]),
            steps=2,
            return_coords=False,
        )
