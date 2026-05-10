"""Tests for rule behavior."""

import pytest

from ca import rules


def test_rule_count_uses_declared_rule_range() -> None:
    assert rules.rule_count(rules.ar2_modular_0d()) == 256
    assert rules.rule_count(rules.dyadrads_1d()) == 256
    assert rules.rule_count(rules.dyadaxes_2d()) == 256
    assert rules.rule_count(rules.dyadaxes_3d()) == 256


def test_valid_rule_ids_returns_finite_range() -> None:
    valid = rules.valid_rule_ids(rules.dyadrads_1d())

    assert isinstance(valid, range)
    assert len(valid) == 256
    assert valid.start == 0
    assert valid.stop == 256


def test_rule_count_rejects_open_ended_rule_family() -> None:
    with pytest.raises(ValueError, match="does not declare"):
        rules.rule_count(rules.formulaic())
