"""Tests for random number generation behavior."""

import unittest

from ca import rng


class RngTests(unittest.TestCase):
    def test_splitmix64_matches_old_pe_derivation(self) -> None:
        self.assertEqual(rng.splitmix64(12345, 0), 2454886589211414944)
        self.assertEqual(rng.splitmix64(12345, 7), 17950187751348045818)

    def test_derive_episode_rng_uses_stream_policy(self) -> None:
        stream = {"policy": "splitmix64", "base_rng": 12345}

        self.assertEqual(rng.derive_episode_rng(stream, 7), rng.splitmix64(12345, 7))

    def test_numpy_rng_is_deterministic(self) -> None:
        stream = {"policy": "splitmix64", "base_rng": 12345}
        left = rng.numpy_rng(stream, 3).integers(0, 100, size=8)
        right = rng.numpy_rng(stream, 3).integers(0, 100, size=8)

        self.assertEqual(left.tolist(), right.tolist())


if __name__ == "__main__":
    unittest.main()
