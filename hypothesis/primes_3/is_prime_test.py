"""Jednotkové testy pro funkci is_prime()."""

from hypothesis import given
from hypothesis.strategies import integers

from is_prime import is_prime


@given(integers(min_value=0, max_value=39).map(lambda x: x ** 2 + x + 41))
def test_is_prime_polygon(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value)
