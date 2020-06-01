"""Jednotkové testy pro funkci compare."""

from comparator1 import compare


def test_comparator():
    """Jednotkový test pro porovnání dvou prvků."""
    assert compare(1, 2)
    assert compare(1.2, 3.4)
    assert not compare("foo", "bar")
    assert compare([1, 2], [3, 4])
    assert not compare(True, False)
