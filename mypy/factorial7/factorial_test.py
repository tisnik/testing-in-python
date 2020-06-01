"""Jednotkové testy pro výpočet faktoriálu."""

from factorial import factorial


def test_factorial():
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_factorial_negative_values():
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(-1) is None
    assert factorial(-1000) is None
