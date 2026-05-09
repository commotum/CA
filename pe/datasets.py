"""Dataset catalog factories.

Treat this as a tentative plan, not a prescription.

This module is the catalog layer for complete dataset definitions. It replaces
the earlier `data/dataset-configs/*.json` idea in the target repository
structure: dataset construction is expressed as Python factory families here,
while top-level configs choose which dataset ids to include in an experiment.

A dataset factory composes the lower component catalogs into one coherent
dataset spec:

- `alphabets.py` defines the raw value space,
- `neighborhoods.py` defines the read interface,
- `frontiers.py` defines current update sites,
- `seeds.py` defines seed families and seed pools,
- `rules.py` defines the next-state update law,
- dataset-level metadata defines domain, shape, boundary policy, default
  horizon behavior, split/eval conventions, and artifact naming.

`datasets.py` should not generate trajectories, tokenize arrays, create
batches, or train models. It builds declarative dataset specs that `prepare.py`
can freeze into source manifests, train/eval stream specs, and compact vocab
recipes. Runtime realization belongs to `data.batch`, `data.generate`, and
`data.tokenize`.

The same layered construction principle applies here: singular component
catalogs own their own semantics, rules compose those components into update
laws, and datasets compose the finished pieces into named benchmark families
such as `0d-ar2-97`, `1d-dyadrads`, `2d-dyadaxes`, and `3d-dyadaxes`.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from data.components import alphabets, frontiers, neighborhoods, rules, seeds


@dataclass(frozen=True)
class DatasetSpec:
    """Complete declarative dataset specification.

    `id` is the stable dataset family id used by top-level configs and prepared
    artifact paths. The remaining fields are built component specs or
    serializable component recipes. The exact representation can be finalized
    when `prepare.py` starts materializing manifests, but this object should
    carry enough information to regenerate trajectories and tokenized artifacts
    deterministically.
    """

    id: str
    domain: str
    shape: tuple[int, ...]
    alphabet: alphabets.ValueSpace
    neighborhoods: tuple[neighborhoods.Neighborhood, ...]
    frontier: frontiers.Frontier
    rule: rules.Rule
    seeds: tuple[seeds.Seed, ...]
    boundary: Mapping[str, object]
    params: Mapping[str, object] | None = None


def _spatial_seeds(shape: Sequence[int]) -> tuple[seeds.Seed, ...]:
    return (
        seeds.bernoulli(p_low=0.0, p_high=1.0),
        *seeds.structured(shape),
    )


# ---------------------------------------------------------------------------
# Phase 1 Dataset Families
# ---------------------------------------------------------------------------


def ar2_0d_97() -> DatasetSpec:
    """Build the `0d-ar2-97` scalar recurrence dataset spec.

    This dataset uses a `t+0D` domain, a 97-value range alphabet, the AR(2)-style
    temporal neighborhood over current and previous scalar values, a
    full-current-slice frontier, and a modular autoregressive rule.
    """

    shape = ()

    return DatasetSpec(
        id="0d-ar2-97",
        domain="t+0d",
        shape=shape,
        alphabet=alphabets.int_range_alphabet(97),
        neighborhoods=(neighborhoods.ar2_0d(),),
        frontier=frontiers.time_slice(shape),
        rule=rules.ar2_modular_0d(modulus=97),
        seeds=(seeds.uniform_pair(value_count=97, reject_zero_zero=True),),
        boundary={},
    )


def dyadrads_1d() -> DatasetSpec:
    """Build the `1d-dyadrads` dataset spec.

    This dataset uses a `t+1D` spatial line, a boolean alphabet, the
    three-component Dyadrads neighborhood, a full-current-slice frontier, and
    the matching rule family for 1D next-state generation.
    """

    shape = (123,)

    return DatasetSpec(
        id="1d-dyadrads",
        domain="t+1d",
        shape=shape,
        alphabet=alphabets.boolean(),
        neighborhoods=(neighborhoods.dyadrads_1d(),),
        frontier=frontiers.time_slice(shape),
        rule=rules.dyadrads_1d(),
        seeds=_spatial_seeds(shape),
        boundary={"policy": "fixed", "value": 0},
    )


def dyadaxes_2d() -> DatasetSpec:
    """Build the `2d-dyadaxes` dataset spec.

    This dataset uses a `t+2D` spatial grid, a boolean alphabet, the
    three-component 2D Dyadaxes neighborhood, a full-current-slice frontier, and
    the matching rule family for 2D next-state generation.
    """

    shape = (11, 11)

    return DatasetSpec(
        id="2d-dyadaxes",
        domain="t+2d",
        shape=shape,
        alphabet=alphabets.boolean(),
        neighborhoods=(neighborhoods.dyadaxes_2d(),),
        frontier=frontiers.time_slice(shape),
        rule=rules.dyadaxes_2d(),
        seeds=_spatial_seeds(shape),
        boundary={"policy": "fixed", "value": 0},
    )


def dyadaxes_3d() -> DatasetSpec:
    """Build the `3d-dyadaxes` dataset spec.

    This dataset uses a `t+3D` voxel grid, a boolean alphabet, the
    three-component 3D Dyadaxes neighborhood, a full-current-slice frontier, and
    the matching rule family for 3D next-state generation.
    """

    shape = (5, 5, 5)

    return DatasetSpec(
        id="3d-dyadaxes",
        domain="t+3d",
        shape=shape,
        alphabet=alphabets.boolean(),
        neighborhoods=(neighborhoods.dyadaxes_3d(),),
        frontier=frontiers.time_slice(shape),
        rule=rules.dyadaxes_3d(),
        seeds=_spatial_seeds(shape),
        boundary={"policy": "fixed", "value": 0},
    )
