"""Výpočet faktoriálu."""


def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    assert isinstance(n, int), "Integer expected"

    if n < 0:
        return None
    if n == 0:
        return 1
    result = n * factorial(n-1)

    assert isinstance(result, int), "Internal error in factorial computation"
    return result
