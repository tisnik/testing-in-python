"""Implementace jednotkových testů."""

import pytest


def setup_module(module):
    """Zavoláno při inicializaci modulu s testem."""
    print("SETUP MODULE")


def teardown_module(module):
    """Zavoláno při finalizaci modulu s testem."""
    print("TEARDOWN MODULE")


class TestClass:
    """Jednotkové testy ve třídě."""

    @classmethod
    def setup_class(cls):
        """Zavoláno při inicializaci třídy s testy."""
        print("SETUP CLASS")

    @classmethod
    def teardown_class(cls):
        """Zavoláno při finalizaci třídy s testy."""
        print("\nTEARDOWN CLASS")

    def setup_method(cls):
        """Zavoláno před každou metodou s jednotkovými testy."""
        print("SETUP METHOD")

    def teardown_method(cls):
        """Zavoláno po každé metodě s jednotkovými testy."""
        print("\nTEARDOWN METHOD")

    def test_1(self):
        """Kostra jednotkového testu."""
        print("Test #1")

    def test_2(self):
        """Kostra jednotkového testu."""
        print("Test #2")

    def test_3(self):
        """Kostra jednotkového testu."""
        print("Test #3")
