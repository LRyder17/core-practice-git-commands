import pytest


def always_returns_true():
    # This is the comment add my LU
    return False


def test_always_returns_true():
    assert always_returns_true()
