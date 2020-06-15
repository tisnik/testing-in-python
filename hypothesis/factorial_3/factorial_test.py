"""Jednotkové testy pro výpočet faktoriálu."""

from hypothesis import given
from hypothesis.strategies import lists, integers

from factorial import factorial


@given(integers().filter(lambda x: x >= 0))
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) > 0
    assert factorial(value) >= value


@given(integers().filter(lambda x: x < 0))
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) is None
