"""Tests for rollout behavior."""

from types import SimpleNamespace

import numpy as np
import pytest

import ca
from ca import frontiers, neighborhoods, rules
from ca.specs import RawBatch, RawEpisode


def _assert_batch_matches_loop(
    dynamics: ca.Dynamics,
    rule_ids: list[int],
    seed_states: np.ndarray,
    steps: int,
) -> RawBatch:
    batch = ca.rollout_batch(
        dynamics=dynamics,
        rule_ids=np.asarray(rule_ids, dtype=np.int64),
        seed_states=seed_states,
        steps=steps,
    )

    expected = [
        ca.rollout(
            dynamics=dynamics,
            rule_id=rule_id,
            seed_state=seed_state,
            steps=steps,
        )
        for rule_id, seed_state in zip(rule_ids, seed_states)
    ]

    assert isinstance(batch, RawBatch)
    assert batch.domain == dynamics.domain
    assert batch.shape == dynamics.shape
    assert batch.steps == steps
    np.testing.assert_array_equal(batch.rule_ids, np.asarray(rule_ids, dtype=np.int64))
    np.testing.assert_array_equal(batch.states, np.stack([episode.states for episode in expected], axis=0))
    assert batch.coords is not None
    np.testing.assert_array_equal(batch.coords, expected[0].coords)
    return batch


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


def test_ar2_rollout_batch_matches_loop() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.time_slice(()),
    )

    batch = _assert_batch_matches_loop(
        dynamics=dynamics,
        rule_ids=[0, 17, 255],
        seed_states=np.array([[1, 2], [3, 5], [8, 13]], dtype=np.int64),
        steps=5,
    )

    assert batch.states.shape == (3, 5)
    assert ca.RawBatch is RawBatch
    assert ca.rollout_batch is not None


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


def test_1d_rollout_batch_matches_loop() -> None:
    dynamics = ca.Dynamics(
        domain="t+1d",
        shape=(3,),
        rule=rules.dyadrads_1d(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.time_slice((3,)),
        boundary={"policy": "fixed", "value": 0},
    )

    batch = _assert_batch_matches_loop(
        dynamics=dynamics,
        rule_ids=[0, 37, 255],
        seed_states=np.array(
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 1, 0],
            ],
            dtype=np.int64,
        ),
        steps=4,
    )

    assert batch.states.shape == (3, 4, 3)


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


def test_2d_rollout_batch_matches_loop() -> None:
    dynamics = ca.Dynamics(
        domain="t+2d",
        shape=(3, 3),
        rule=rules.dyadaxes_2d(),
        neighborhoods=(neighborhoods.dyadaxes_2d(),),
        frontier=frontiers.time_slice((3, 3)),
        boundary={"policy": "fixed", "value": 0},
    )

    batch = _assert_batch_matches_loop(
        dynamics=dynamics,
        rule_ids=[0, 91],
        seed_states=np.array(
            [
                [
                    [0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0],
                ],
                [
                    [1, 0, 1],
                    [0, 1, 0],
                    [1, 0, 1],
                ],
            ],
            dtype=np.int64,
        ),
        steps=3,
    )

    assert batch.states.shape == (2, 3, 3, 3)


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


def test_3d_rollout_batch_matches_loop() -> None:
    dynamics = ca.Dynamics(
        domain="t+3d",
        shape=(3, 3, 3),
        rule=rules.dyadaxes_3d(),
        neighborhoods=(neighborhoods.dyadaxes_3d(),),
        frontier=frontiers.time_slice((3, 3, 3)),
        boundary={"policy": "fixed", "value": 0},
    )
    seed_states = np.zeros((2, 3, 3, 3), dtype=np.int64)
    seed_states[0, 1, 1, 1] = 1
    seed_states[1, :, 1, :] = 1

    batch = _assert_batch_matches_loop(
        dynamics=dynamics,
        rule_ids=[0, 173],
        seed_states=seed_states,
        steps=3,
    )

    assert batch.states.shape == (2, 3, 3, 3, 3)


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


def test_rollout_batch_can_skip_coord_materialization() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.time_slice(()),
    )

    batch = ca.rollout_batch(
        dynamics=dynamics,
        rule_ids=np.array([0, 1]),
        seed_states=np.array([[1, 2], [3, 5]]),
        steps=2,
        return_coords=False,
    )

    assert batch.coords is None


def test_rollout_batch_rejects_spatial_shape_mismatch() -> None:
    dynamics = ca.Dynamics(
        domain="t+1d",
        shape=(4,),
        rule=rules.dyadrads_1d(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.time_slice((4,)),
        boundary={"policy": "fixed", "value": 0},
    )

    with pytest.raises(ValueError, match="dynamics.shape"):
        ca.rollout_batch(
            dynamics=dynamics,
            rule_ids=np.array([0, 1]),
            seed_states=np.array([[1, 0, 1], [0, 1, 0]]),
            steps=2,
        )


def test_rollout_batch_rejects_batch_size_mismatch() -> None:
    dynamics = ca.Dynamics(
        domain="t+0d",
        shape=(),
        rule=rules.ar2_modular_0d(modulus=97),
        neighborhoods=(),
        frontier=frontiers.time_slice(()),
    )

    with pytest.raises(ValueError, match="batch size"):
        ca.rollout_batch(
            dynamics=dynamics,
            rule_ids=np.array([0, 1, 2]),
            seed_states=np.array([[1, 2], [3, 5]]),
            steps=2,
        )


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
