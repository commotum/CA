"""Tests for seed behavior."""

import numpy as np
import pytest

from ca import loci, seeds


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


def test_bernoulli_rejects_unknown_support_specs() -> None:
    with pytest.raises(ValueError):
        seeds.bernoulli(support={"family": "initial_slice"})  # type: ignore[arg-type]


def test_compound_rejects_non_seed_components() -> None:
    with pytest.raises(TypeError):
        seeds.compound(kind="plus", components=({"family": "point"},))  # type: ignore[list-item]


def test_compound_rejects_components_without_support() -> None:
    with pytest.raises(ValueError):
        seeds.compound(kind="plus", components=(seeds.constant(1),))


def test_compound_accepts_selector_backed_seed_components() -> None:
    selector = loci.selector(loci.absolute_universe(loci.coordinate_space((3,)), t=0))
    seed = seeds.selector_seed(selector)
    compound = seeds.compound(kind="plus", components=(seed,))

    assert compound.support is not None


def test_structured_can_skip_dedupe() -> None:
    specs = seeds.structured((3,), dedupe_mode=None)

    assert specs
