"""Test jednoduché šifry typu ROT13."""

from hypothesis import given, note, settings
from hypothesis.strategies import text, characters

from rot13 import rot13


@given(text(min_size=5))
@settings(max_examples=500)
def test_rot13(s):
    """Test jednoduché šifry typu ROT13."""
    assert rot13(rot13(s)) == s
