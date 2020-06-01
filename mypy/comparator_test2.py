"""Jednotkové testy pro funkci compare."""

from comparator1 import compare
from math import nan


def test_comparator():
    """Jednotkový test komutativity."""
    assert compare(1, 2) is not compare(2, 1)
    assert compare("foo", "bar") is not compare("bar", "foo")
    assert compare(nan, nan) is not compare(nan, nan)
