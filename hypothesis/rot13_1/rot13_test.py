"""Test jednoduché šifry typu ROT13."""

from hypothesis import given
from hypothesis.strategies import text

from rot13 import rot13


@given(text())
def test_rot13(s):
    """Test jednoduché šifry typu ROT13."""
    assert rot13(rot13(s)) == s
