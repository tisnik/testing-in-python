"""Výpočet faktoriálu."""

from typing import overload
from typing import Optional


@overload
def factorial(n: None) -> None:
    pass


@overload
def factorial(n: int) -> int:
    pass


def factorial(n: Optional[int]) -> Optional[int]:
    """Rekurzivní výpočet faktoriálu."""
    if n is None:
        return None
    if n < 0:
        return None
    if n == 0:
        return 1

    return n * factorial(n-1)
