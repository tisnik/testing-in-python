"""Implementace jednotkových testů."""

import pytest

from adder import Complex, init, add, equal


def test_add_basic():
    """Otestování výpočtu součtu dvou komplexních čísel."""
    init()

    c1 = Complex(1.0, 2.0)
    c2 = Complex(3.0, 4.0)

    result = add(c1, c2)
    expected = Complex(4.0, 6.0)
    assert result == expected, \
        "Očekávaná hodnota {}, vráceno {}".format(expected, result)


def test_add_failure():
    """Otestování výpočtu součtu dvou komplexních čísel."""
    init()

    c1 = Complex(1.0, 2.0)
    c2 = Complex(0.0, 0.0)

    result = add(c1, c2)
    expected = Complex(4.0, 6.0)
    assert result == expected, \
        "Očekávaná hodnota {}, vráceno {}".format(expected, result)
