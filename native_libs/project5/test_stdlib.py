"""Implementace jednotkových testů."""

import pytest
import ctypes

libc = None


def setup_module(module):
    """Zavoláno při inicializaci modulu s testem."""
    global libc
    libc = ctypes.CDLL("libc.so.6")


def test_time():
    """Otestování nativní funkce time()."""
    t = libc.time(None)
    # velmi nepřesný odhad počtu sekund pro 2000-01-01
    t2020 = (2020-1970)*365*24*60*60
    assert t > t2020, "Neočekávaná hodnota {}".format(t)


def test_abs():
    """Otestování nativní funkce abs()."""
    x = libc.abs(-1)
    assert x == 1, "Neočekávaná hodnota {}".format(x)

    x = libc.abs(1)
    assert x == 1, "Neočekávaná hodnota {}".format(x)
