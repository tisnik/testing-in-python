"""Implementace jednotkových testů."""

import pytest

import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average.avg([1, 2])
    expected = 1.5
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)


def test_average_empty_list():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average.avg([])
