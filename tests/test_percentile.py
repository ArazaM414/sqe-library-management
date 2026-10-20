
import pytest
from percentile import percentile


def test_first_student():
    assert percentile("Ali", ["Ali", "Sara", "Ahmed"]) == 0.0


def test_last_student():
    assert percentile("Ahmed", ["Ali", "Sara", "Ahmed"]) == 100.0


def test_single_student():
    assert percentile("Ali", ["Ali"]) == 100.0


def test_empty_roster():
    with pytest.raises(ValueError):
        percentile("Ali", [])


def test_missing_student():
    with pytest.raises(ValueError):
        percentile("Zain", ["Ali", "Sara"])
