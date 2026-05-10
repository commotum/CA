"""Tests for rollout behavior."""

from types import SimpleNamespace

import numpy as np

from ca import neighborhoods, rollout, rules


def test_ar2_rollout_returns_numpy_states() -> None:
    rule = rules.instantiate(rules.ar2_modular_0d(modulus=97), 0)
    states = rollout.rollout(
        initial_state=np.array([1, 2]),
        rule=rule,
        neighborhoods=(),
        frontier=SimpleNamespace(name="time_slice"),
        boundary={},
        steps=4,
    )

    assert isinstance(states, np.ndarray)
    assert states.tolist() == [2, 3, 4, 5]


def test_spatial_lookup_rule_zero_outputs_zero_state() -> None:
    rule = rules.instantiate(rules.dyadrads_1d(), 0)
    states = rollout.rollout(
        initial_state=np.array([1, 0, 1]),
        rule=rule,
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=SimpleNamespace(name="time_slice"),
        boundary={"policy": "fixed", "value": 0},
        steps=2,
    )

    assert states.tolist() == [[1, 0, 1], [0, 0, 0]]


def test_rollout_rejects_unsupported_frontier() -> None:
    rule = rules.instantiate(rules.ar2_modular_0d(modulus=97), 0)

    try:
        rollout.rollout(
            initial_state=np.array([1, 2]),
            rule=rule,
            neighborhoods=(),
            frontier=SimpleNamespace(name="partial"),
            boundary={},
            steps=2,
        )
    except NotImplementedError:
        return

    raise AssertionError("expected unsupported frontier to raise")
