"""Implementace jednotkových testů."""

from unittest.mock import *

from application import *


def test1():
    """První test neprovádí prakticky žádné reálné kontroly, jen zavolá testovanou funkci."""
    print("function1 returns: {v}".format(v=function1()))


@patch('application.function2', return_value=42)
def test2(mocked_function):
    # vytiskneme informaci o tom, zda se mockovaná funkce zavolala
    print("mocked function called: {c}".format(c=mocked_function.called))
    print("function1 returns: {v}".format(v=function1()))
    # opět vytiskneme informaci o tom, zda se mockovaná funkce zavolala
    print("mocked function called: {c}".format(c=mocked_function.called))


def side_effect_handler():
    """Implementace handleru - stub funkce nahrazované mockem."""
    print("side_effect_handler function called")
    return -1


@patch('application.function2', side_effect=side_effect_handler)
def test3(mocked_function):
    """Třetí test zjištuje, zda se volá side_effect_handler."""
    # vytiskneme informaci o tom, zda se mockovaná funkce zavolala
    print("mocked function called: {c}".format(c=mocked_function.called))
    print(function1())
    # opět vytiskneme informaci o tom, zda se mockovaná funkce zavolala
    print("mocked function called: {c}".format(c=mocked_function.called))


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test3()
    print()
