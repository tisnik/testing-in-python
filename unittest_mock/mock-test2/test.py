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


def side_effect_handler():
    """Implementace handleru - stub funkce nahrazované mockem."""
    print("side_effect function called")
    return -1


@patch('application.function1', side_effect=side_effect_handler)
def test3(mocked_function):
    """Třetí test používá stub test double - náhradu volané funkce."""
    print(application.function1())


@patch('application.function1', return_value=42, side_effect=side_effect_handler)
def test4(mocked_function):
    """Čtvrtý test se snaží zkombinovat fake a stub."""
    print(application.function1())


def side_effect_handler_2():
    """Implementace handleru: stub funkce nahrazované mockem, který ovlivňuje chování testu."""
    print("side_effect function called")
    return DEFAULT


@patch('application.function1', return_value=42, side_effect=side_effect_handler_2)
def test5(mocked_function):
    """Pátý test se opět snaží zkombinovat fake a stub."""
    print(application.function1())


if __name__ == '__main__':
    print("*** test1 ***")
    test1()
    print()

    print("*** test2 ***")
    test2()
    print()

    print("*** test3 ***")
    test3()
    print()

    print("*** test4 ***")
    test4()
    print()

    print("*** test5 ***")
    test5()
    print()

    print("*** test1 ***")
    test1()
    print()
