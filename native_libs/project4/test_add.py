"""Implementace jednotkových testů."""

import pytest

from adder import init, add


def test_add_basic():
    """Otestování výpočtu součtu dvou celých čísel."""
    init()
    result = add(1, 2)
    expected = 3
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)


def test_add_large_ints():
    """Otestování výpočtu součtu dvou větších celých čísel."""
    init()
    result = add(2**31-2, 1)
    expected = 2**31-1
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)


def test_add_even_larger_ints():
    """Otestování výpočtu součtu dvou velkých celých čísel."""
    init()
    result = add(2**31-1, 1)
    expected = 2**31
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)
