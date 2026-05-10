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
        frontier=frontiers.time_slice(()),
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
        frontier=frontiers.time_slice((3,)),
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


def test_2d_rollout_returns_raw_episode() -> None:
    dynamics = ca.Dynamics(
        domain="t+2d",
        shape=(3, 3),
        rule=rules.dyadaxes_2d(),
        neighborhoods=(neighborhoods.dyadaxes_2d(),),
        frontier=frontiers.time_slice((3, 3)),
        boundary={"policy": "fixed", "value": 0},
    )

    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=np.array(
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0],
            ]
        ),
        steps=2,
    )

    assert episode.states.shape == (2, 3, 3)
    assert episode.states[1].tolist() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert episode.coords is not None
    assert episode.coords.shape == (18, 4)


def test_3d_rollout_returns_raw_episode() -> None:
    dynamics = ca.Dynamics(
        domain="t+3d",
        shape=(3, 3, 3),
        rule=rules.dyadaxes_3d(),
        neighborhoods=(neighborhoods.dyadaxes_3d(),),
        frontier=frontiers.time_slice((3, 3, 3)),
        boundary={"policy": "fixed", "value": 0},
    )
    seed_state = np.zeros((3, 3, 3), dtype=np.int64)
    seed_state[1, 1, 1] = 1

    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=seed_state,
        steps=2,
    )

    assert episode.states.shape == (2, 3, 3, 3)
    assert np.count_nonzero(episode.states[1]) == 0
    assert episode.coords is not None
    assert episode.coords.shape == (54, 4)


def test_rollout_can_skip_coord_materialization() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.time_slice(()),
    )

    episode = ca.rollout(
        dynamics=dynamics,
        rule_id=0,
        seed_state=np.array([1, 2]),
        steps=2,
        return_coords=False,
    )

    assert episode.coords is None


def test_dynamics_normalizes_boundary_mapping() -> None:
    dynamics = ca.Dynamics(
        domain="t+1d",
        shape=(3,),
        rule=rules.dyadrads_1d(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.time_slice((3,)),
        boundary={"policy": "periodic"},
    )

    assert dynamics.boundary == {"policy": "periodic"}


def test_dynamics_rejects_legacy_boundary_string() -> None:
    with pytest.raises(TypeError, match="boundary must be a mapping"):
        ca.Dynamics(
            domain="t+1d",
            shape=(3,),
            rule=rules.dyadrads_1d(),
            neighborhoods=(neighborhoods.dyadrads_1d(),),
            frontier=frontiers.time_slice((3,)),
            boundary="periodic",  # type: ignore[arg-type]
        )


def test_rollout_rejects_unsupported_frontier() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=SimpleNamespace(family="partial"),
    )

    with pytest.raises(ValueError):
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
        frontier=frontiers.time_slice((4,)),
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
        frontier=frontiers.time_slice((3,)),
    )

    with pytest.raises(ValueError, match="requires spatial rank"):
        ca.rollout(
            dynamics=dynamics,
            rule_id=0,
            seed_state=np.array([1, 2]),
            steps=2,
            return_coords=False,
        )
