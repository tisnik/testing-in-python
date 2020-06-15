"""Jednotkové testy pro funkci is_prime()."""

from hypothesis import given
from hypothesis.strategies import integers

from is_prime import is_prime


@given(integers(min_value=3).filter(lambda x: x % 2 == 0))
def test_is_prime_for_even_values(value):
    """Jednotkový test pro funkci is_prime()."""
    assert not is_prime(value)
