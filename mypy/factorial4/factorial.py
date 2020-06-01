"""Výpočet faktoriálu."""


def factorial(n: int) -> int:
    """Rekurzivní výpočet faktoriálu."""
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)
