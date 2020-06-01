"""Výpočet faktoriálu."""

from typing import Union


def factorial(n: int) -> Union[int, None]:
    """Rekurzivní výpočet faktoriálu."""
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)
