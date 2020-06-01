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
    return n * factorial(n-1)
