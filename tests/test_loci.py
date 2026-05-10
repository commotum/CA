"""Tests for coordinate loci behavior."""

import numpy as np
import pytest

from ca import loci


def test_rank_zero_coord_grid_is_two_dimensional() -> None:
    grid = loci.coord_grid(loci.coordinate_space((), steps=3))

    assert grid.shape == (3, 4)
    assert grid.tolist() == [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0]]


def test_centered_axis_values() -> None:
    assert loci.axis_values("x", 3).tolist() == [-1, 0, 1]
    assert loci.axis_values("x", 4).tolist() == [-1, 0, 1, 2]


def test_absolute_universe_time_major_1d() -> None:
    space = loci.coordinate_space((3,), steps=2)
    universe = loci.absolute_universe(space)

    assert universe.tolist() == [
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [1, -1, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
    ]


def test_selector_predicates_and_order() -> None:
    space = loci.coordinate_space((3,))
    selector = loci.selector(
        loci.absolute_universe(space),
        predicates=(loci.coord_between("x", 0, 1),),
        order="lex",
    )

    selected = loci.select(selector)

    assert selected.coords.tolist() == [[0, 0, 0, 0], [0, 1, 0, 0]]


def test_gather_boundary_policies() -> None:
    values = np.array([[10, 20, 30]])
    coords = np.array([[0, 2, 0, 0]])

    assert loci.gather(coords, values, {"policy": "fixed", "value": 99}).tolist() == [99]
    assert loci.gather(coords, values, {"policy": "periodic"}).tolist() == [10]
    assert loci.gather(coords, values, {"policy": "reflective"}).tolist() == [20]


def test_gather_reads_centered_coordinate() -> None:
    values = np.array([[10, 20, 30]])
    coords = np.array([
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
    ])

    assert loci.gather(coords, values).tolist() == [10, 20, 30]


def test_gather_uses_trajectory_time_axis() -> None:
    states = np.array([[1, 2, 3], [4, 5, 6]])
    coords = np.array([[1, 0, 0, 0]])

    assert loci.gather(coords, states).tolist() == [5]


def test_gather_rejects_legacy_boundary_aliases() -> None:
    values = np.array([[10, 20, 30]])
    coords = np.array([[0, 2, 0, 0]])

    with pytest.raises(ValueError, match="unsupported boundary fields"):
        loci.gather(coords, values, {"mode": "periodic"})

    with pytest.raises(ValueError, match="unsupported boundary fields"):
        loci.gather(coords, values, {"policy": "fixed", "fill_value": 99})
