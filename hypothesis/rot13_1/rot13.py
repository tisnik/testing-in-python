"""Jednoduchá šifra typu ROT13."""

from hypothesis import given
from hypothesis.strategies import text
import string


def rot13(text):
    """Jednoduchá šifra typu ROT13."""
    r = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return text.translate(r)


if __name__ == '__main__':
    sentence = "Příliš žluťoučký kůň úpěl ďábelské ódy."
    print(rot13(sentence))
    print(rot13(rot13(sentence)))
