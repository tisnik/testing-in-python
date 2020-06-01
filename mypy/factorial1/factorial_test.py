"""Jednotkové testy pro výpočet faktoriálu."""

from factorial import factorial


def test_factorial():
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
