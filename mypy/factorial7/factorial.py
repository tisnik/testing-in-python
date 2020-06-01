"""Výpočet faktoriálu."""

from typing import Optional


def factorial(n: Optional[int]) -> Optional[int]:
    """Rekurzivní výpočet faktoriálu."""
    if n is None:
        return None
    if n < 0:
        return None
    if n == 0:
        return 1

    r = factorial(n-1)

    if r is None:
        return None
    return n * r
