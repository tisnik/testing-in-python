"""Jednotkové testy pro výpočet faktoriálu."""

from hypothesis import given
from hypothesis.strategies import lists, integers

from factorial import factorial


@given(integers())
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) > 0
    assert factorial(value) >= value
