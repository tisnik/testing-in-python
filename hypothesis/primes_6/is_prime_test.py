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


@given(integers(min_value=1, max_value=LIMIT))
def test_is_prime(value):
    """Jednotkový test pro funkci is_prime()."""
    assert is_prime(value) == (value in precomputed)
