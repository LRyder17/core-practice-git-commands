import pytest


def always_returns_true():
    # This is a brand new comment
    return False


def test_always_returns_true():
    # now I'm adding a comment to test always returns true 
    assert always_returns_true()
