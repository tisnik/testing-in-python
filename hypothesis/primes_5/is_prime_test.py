"""Jednotkové testy pro funkci is_prime()."""

from hypothesis import given
from hypothesis.strategies import integers, builds

from is_prime import is_prime


precomputed = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101
]


@given(integers(min_value=1, max_value=100))
def test_is_prime(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value) == (value in precomputed)
