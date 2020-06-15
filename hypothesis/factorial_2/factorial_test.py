"""Jednotkové testy pro výpočet faktoriálu."""

from hypothesis import given
from hypothesis.strategies import lists, integers

from factorial import factorial


@given(integers(min_value=0))
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) > 0
    assert factorial(value) >= value


@given(integers(max_value=-1))
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) is None
