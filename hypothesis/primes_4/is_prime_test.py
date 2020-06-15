"""Jednotkové testy pro funkci is_prime()."""

from hypothesis import given
from hypothesis.strategies import integers, builds

from is_prime import is_prime


cache = [2, 3]


def generate_nth_prime(n):
    """Vygenerování n-tého prvočísla (lze získat z cache)."""
    if n < len(cache):
        return cache[n]

    x = cache[-1]

    while len(cache) < n:
        # zde je pochopitelně vhodné použít jiný algoritmus, než ten, který je testován!!!
        if not any(x % y == 0 for y in range(3, int(x**0.5) + 1, 2)):
            cache.append(x)
        x += 2
    return cache[-1]


@given(builds(generate_nth_prime, integers(min_value=1, max_value=100)))
def test_is_prime_generator(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value)
