"""Tests for seed behavior."""

import numpy as np

from ca import seeds


def test_pair_seed_renders_numpy_pair() -> None:
    rendered = seeds.render(seeds.pair(3, 5), ())

    assert isinstance(rendered, np.ndarray)
    assert rendered.tolist() == [3, 5]


def test_constant_seed_renders_full_shape() -> None:
    rendered = seeds.render(seeds.constant(7), (2, 3))

    assert rendered.tolist() == [[7, 7, 7], [7, 7, 7]]


def test_point_seed_uses_centered_coordinates() -> None:
    rendered = seeds.render(seeds.point({"x": 0}, value=1), (3,))

    assert rendered.tolist() == [0, 1, 0]


def test_bernoulli_seed_is_deterministic_with_rng() -> None:
    seed = seeds.bernoulli(p_low=0.5, p_high=0.5)
    left = seeds.render(seed, (4,), rng=np.random.default_rng(123))
    right = seeds.render(seed, (4,), rng=np.random.default_rng(123))

    assert left.tolist() == right.tolist()
