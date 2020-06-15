"""Jednotkové testy pro funkci is_prime()."""

from hypothesis import given
from hypothesis.strategies import integers, builds

from is_prime import is_prime


# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Odds-only_version_of_the_array_sieve_above
def primes(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    # okrajový případ
    if limit < 2:
        return []

    # druhý případ - 2 je speciálním prvočíslem
    if limit < 3:
        return [2]

    lmtbf = (limit - 3) // 2

    # naplnění tabulky, která se bude prosívat
    buf = [True] * (lmtbf + 1)

    # vlastní prosívání
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)

    # vytvoření seznamu prvočísel
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]


LIMIT = 1000

precomputed = primes(LIMIT)


@given(integers(min_value=3).filter(lambda x: x % 2 == 0))
def test_is_prime_for_even_values_filter(value):
    """Jednotkový test pro funkci is_prime()."""
    assert not is_prime(value)


@given(integers(min_value=2).map(lambda x: 2 * x))
def test_is_prime_for_even_values_map(value):
    """Jednotkový test pro funkci is_prime()."""
    assert not is_prime(value)


@given(integers(min_value=0, max_value=39).map(lambda x: x ** 2 + x + 41))
def test_is_prime_using_polygon(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value)


@given(integers(min_value=1, max_value=LIMIT))
def test_is_prime_using_primes_function(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value) == (value in precomputed)


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


primes_table = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101
]


@given(integers(min_value=1, max_value=100))
def test_is_prime_precomputed(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value) == (value in primes_table)
