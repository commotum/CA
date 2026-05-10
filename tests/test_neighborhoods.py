"""Tests for neighborhood factory behavior."""

import numpy as np
import pytest

from ca import loci, neighborhoods


def _coords(neighborhood: neighborhoods.Neighborhood, component: int = 0) -> list[list[int]]:
    selection = loci.select(neighborhood.components[component])
    assert selection.coords is not None
    return selection.coords.tolist()


def test_literal_offsets_returns_lex_ordered_offsets() -> None:
    neighborhood = neighborhoods.literal_offsets(
        (
            (0, 1, 0, 0),
            (0, -1, 0, 0),
            (0, 0, 0, 0),
        )
    )

    assert _coords(neighborhood) == [
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
    ]


def test_literal_offsets_rejects_invalid_offsets() -> None:
    with pytest.raises(ValueError):
        neighborhoods.literal_offsets(())

    with pytest.raises(ValueError):
        neighborhoods.literal_offsets(((0, 1, 0),))

    with pytest.raises(ValueError):
        neighborhoods.literal_offsets(((0, 1, 0, 0), (0, 1, 0, 0)))


def test_history_preserves_temporal_components() -> None:
    neighborhood = neighborhoods.history((0, -1, -2))

    assert len(neighborhood.components) == 3
    assert _coords(neighborhood, component=0) == [[0, 0, 0, 0]]
    assert _coords(neighborhood, component=1) == [[-1, 0, 0, 0]]
    assert _coords(neighborhood, component=2) == [[-2, 0, 0, 0]]


def test_radius_builds_eca_stencil() -> None:
    neighborhood = neighborhoods.radius(
        axes=("x",),
        metric="linf",
        region="filled",
        radius=1,
    )

    assert _coords(neighborhood) == [
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
    ]


def test_eca_alias_builds_standard_stencil() -> None:
    neighborhood = neighborhoods.eca(r=2, time_offset=-1)

    assert neighborhood.params == {
        "axes": ("x",),
        "metric": "linf",
        "region": "filled",
        "radius": 2,
        "time_offset": -1,
        "include_center": True,
        "read_mode": "compact",
    }
    assert _coords(neighborhood) == [
        [-1, -2, 0, 0],
        [-1, -1, 0, 0],
        [-1, 0, 0, 0],
        [-1, 1, 0, 0],
        [-1, 2, 0, 0],
    ]


def test_radius_builds_moore_without_center() -> None:
    neighborhood = neighborhoods.radius(
        axes=("x", "y"),
        metric="linf",
        region="filled",
        radius=1,
        include_center=False,
    )

    assert _coords(neighborhood) == [
        [0, -1, -1, 0],
        [0, -1, 0, 0],
        [0, -1, 1, 0],
        [0, 0, -1, 0],
        [0, 0, 1, 0],
        [0, 1, -1, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
    ]


def test_moore_alias_matches_linf_filled_without_center() -> None:
    direct = neighborhoods.radius(
        axes=("x", "y"),
        metric="linf",
        region="filled",
        radius=1,
        include_center=False,
    )
    alias = neighborhoods.moore()

    assert alias.params == direct.params
    assert _coords(alias) == _coords(direct)


def test_radius_builds_von_neumann_shells() -> None:
    neighborhood_2d = neighborhoods.radius(
        axes=("x", "y"),
        metric="l1",
        region="shell",
        radius=1,
    )
    neighborhood_3d = neighborhoods.radius(
        axes=("x", "y", "z"),
        metric="l1",
        region="shell",
        radius=1,
    )

    assert _coords(neighborhood_2d) == [
        [0, -1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]
    assert _coords(neighborhood_3d) == [
        [0, -1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, -1],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]


def test_von_neumann_alias_uses_filled_l1_region() -> None:
    neighborhood = neighborhoods.von_neumann(r=2)

    assert neighborhood.params == {
        "axes": ("x", "y"),
        "metric": "l1",
        "region": "filled",
        "radius": 2,
        "time_offset": 0,
        "include_center": False,
        "read_mode": "compact",
    }
    assert _coords(neighborhood) == [
        [0, -2, 0, 0],
        [0, -1, -1, 0],
        [0, -1, 0, 0],
        [0, -1, 1, 0],
        [0, 0, -2, 0],
        [0, 0, -1, 0],
        [0, 0, 1, 0],
        [0, 0, 2, 0],
        [0, 1, -1, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 2, 0, 0],
    ]


def test_shell_matches_radius_shell_without_center() -> None:
    direct = neighborhoods.radius(
        axes=("x", "y"),
        metric="l1",
        region="shell",
        radius=1,
        include_center=False,
    )
    wrapped = neighborhoods.shell(("x", "y"), metric="l1", r=1)

    assert _coords(wrapped) == _coords(direct)
    assert wrapped.name == "shell"


def test_directional_line_offsets() -> None:
    neighborhood = neighborhoods.directional_line("x", (1, 2, 3))
    fixed_neighborhood = neighborhoods.directional_line("x", (-2, -1), fixed={"y": 1})

    assert _coords(neighborhood) == [
        [0, 1, 0, 0],
        [0, 2, 0, 0],
        [0, 3, 0, 0],
    ]
    assert _coords(fixed_neighborhood) == [
        [0, -2, 1, 0],
        [0, -1, 1, 0],
    ]


def test_directional_line_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        neighborhoods.directional_line("x", ())

    with pytest.raises(ValueError):
        neighborhoods.directional_line("q", (1,))

    with pytest.raises(ValueError):
        neighborhoods.directional_line("x", (1,), fixed={"x": 2})


def test_directional_fov_selects_bounded_cone() -> None:
    neighborhood = neighborhoods.directional_fov(
        axes=("x", "y"),
        reference=(0, 0),
        direction=(1, 0),
        aperture=np.pi / 6,
        radius=2,
    )

    assert _coords(neighborhood) == [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 2, 0, 0],
    ]


def test_directional_fov_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        neighborhoods.directional_fov(
            axes=("x", "y"),
            reference=(0, 0),
            direction=(0, 0),
            aperture=np.pi / 3,
            radius=2,
        )

    with pytest.raises(ValueError):
        neighborhoods.directional_fov(
            axes=("x", "y"),
            reference=(0, 3),
            direction=(1, 0),
            aperture=np.pi / 3,
            radius=2,
        )
