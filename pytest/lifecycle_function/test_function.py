"""Implementace jednotkových testů."""

import pytest


def setup_module(module):
    """Zavoláno při inicializaci modulu s testem."""
    print("\nSETUP MODULE\n")


def teardown_module(module):
    """Zavoláno při finalizaci modulu s testem."""
    print("\nTEARDOWN MODULE")


def setup_function(function):
    """Zavoláno při inicializaci funkce s testem."""
    print("\nSETUP FUNCTION")


def teardown_function(function):
    """Zavoláno při finalizaci funkce s testem."""
    print("\nTEARDOWN FUNCTION")


def test_1(printer):
    """Kostra jednotkového testu."""
    printer("Test #1")


def test_2(printer):
    """Kostra jednotkového testu."""
    printer("Test #2")


testdata = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
]


@pytest.mark.parametrize("value,expected", testdata)
def test_succ(printer, value, expected):
    """Otestování výpočtu následují hodnoty v číselné řadě."""
    printer("Test succ")
    result = value+1
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)
