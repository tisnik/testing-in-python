"""Implementace jednotkových testů."""

import pytest

from adder import init, add


def test_add_basic():
    """Otestování výpočtu součtu dvou celých čísel."""
    init()
    result = add(1, 2)
    expected = 3
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)
