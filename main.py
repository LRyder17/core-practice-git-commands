import pytest


def always_returns_true():
    # This is Say's change 
    return False


def test_always_returns_true():
    assert always_returns_true()
