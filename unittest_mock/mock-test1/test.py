"""Implementace (umělých) jednotkových testů."""

from unittest.mock import *

import application


def test1():
    """První test neprovádí prakticky žádné reálné kontroly, jen zavolá testovanou funkci."""
    print(application.function1())


@patch('application.function1', return_value=42)
def test2(mocked_function):
    """Druhý test používá fake test double - náhradu volané funkce."""
    print(application.function1())


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test1()
    print()
