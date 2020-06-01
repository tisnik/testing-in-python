"""Výpočet faktoriálu."""


def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)
