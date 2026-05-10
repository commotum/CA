"""Tests for boundary policy behavior."""

import numpy as np
import pytest

from ca import boundary


def test_apply_boundary_read_reads_centered_coordinate() -> None:
    state = np.array([10, 20, 30])

    assert boundary.apply_boundary_read(state, [0, -1, 0, 0]) == 10
    assert boundary.apply_boundary_read(state, [0, 0, 0, 0]) == 20
    assert boundary.apply_boundary_read(state, [0, 1, 0, 0]) == 30


def test_boundary_policy_factories() -> None:
    state = np.array([10, 20, 30])

    assert boundary.apply_boundary_read(state, [0, 2, 0, 0], boundary.fixed(99)) == 99
    assert boundary.apply_boundary_read(state, [0, 2, 0, 0], boundary.periodic()) == 10
    assert boundary.apply_boundary_read(state, [0, 2, 0, 0], boundary.reflective()) == 20


def test_none_boundary_raises_for_spatial_oob() -> None:
    with pytest.raises(IndexError):
        boundary.apply_boundary_read(np.array([10, 20, 30]), [0, 2, 0, 0])


def test_boundary_gather_uses_trajectory_time_axis() -> None:
    states = np.array([[1, 2, 3], [4, 5, 6]])
    coords = np.array([[1, 0, 0, 0]])

    assert boundary.gather(coords, states).tolist() == [5]
