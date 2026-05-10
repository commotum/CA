"""Deterministic RNG helpers for CA episode generation.

This module owns seed derivation mechanics only. Callers still decide which
stream, rule pool, split, or evaluation row is being realized; `ca.rng` turns
already chosen seed inputs into stable NumPy generators.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import numpy as np


UINT64_MASK = 0xFFFFFFFFFFFFFFFF
SPLITMIX64_GAMMA = 0x9E3779B97F4A7C15


def splitmix64(base_rng: int, episode_index: int = 0) -> int:
    """Derive a stable unsigned 64-bit seed from a base seed and index."""

    value = (int(base_rng) + int(episode_index) + SPLITMIX64_GAMMA) & UINT64_MASK
    value = (value ^ (value >> 30)) * 0xBF58476D1CE4E5B9 & UINT64_MASK
    value = (value ^ (value >> 27)) * 0x94D049BB133111EB & UINT64_MASK
    return (value ^ (value >> 31)) & UINT64_MASK


def derive_episode_rng(seed_stream: Mapping[str, Any] | int, episode_index: int) -> int:
    """Return the deterministic seed for one episode.

    Mapping inputs follow the compact stream seed schema:

    ```text
    {"policy": "splitmix64", "base_rng": ...}
    ```

    Passing an integer is a convenience for direct CA use.
    """

    if isinstance(seed_stream, Mapping):
        policy = seed_stream.get("policy", "splitmix64")
        if policy != "splitmix64":
            raise NotImplementedError(f"unsupported seed stream policy {policy!r}")
        if "base_rng" not in seed_stream:
            raise KeyError("seed_stream requires 'base_rng'")
        base_rng = seed_stream["base_rng"]
    else:
        base_rng = seed_stream

    return splitmix64(int(base_rng), int(episode_index))


def numpy_rng(seed_stream: Mapping[str, Any] | int, episode_index: int | None = None) -> np.random.Generator:
    """Build a deterministic NumPy generator from a stream spec or seed.

    When `episode_index` is provided with an integer seed, the seed is first
    passed through `splitmix64`. When an integer seed is provided without an
    episode index, it is used directly after unsigned 64-bit normalization.
    """

    if isinstance(seed_stream, Mapping):
        index = 0 if episode_index is None else int(episode_index)
        seed = derive_episode_rng(seed_stream, index)
    elif episode_index is None:
        seed = int(seed_stream) & UINT64_MASK
    else:
        seed = splitmix64(int(seed_stream), int(episode_index))

    return np.random.default_rng(seed)


__all__ = [
    "SPLITMIX64_GAMMA",
    "UINT64_MASK",
    "derive_episode_rng",
    "numpy_rng",
    "splitmix64",
]
