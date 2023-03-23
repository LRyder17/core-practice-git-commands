import pytest


def always_returns_true():
    # i changed the comments again.
    return False


def test_always_returns_true():
    assert always_returns_true()
