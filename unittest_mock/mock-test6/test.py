"""Implementace jednotkových testů."""

from unittest.mock import *

from application import Application


def test1():
    """První test neprovádí prakticky žádné reálné kontroly, jen zavolá testovanou metodu."""
    app = Application()
    print("method1 returns: {v}".format(v=app.method1()))


@patch('application.Application.method2', return_value=42)
def test2(mocked_method):
    app = Application()
    # vytiskneme informaci o tom, zda se mockovaná metoda zavolala
    print("mocked method called: {c}".format(c=mocked_method.called))
    print("method1 returns: {v}".format(v=app.method1()))
    # opět vytiskneme informaci o tom, zda se mockovaná metoda zavolala
    print("mocked method called: {c}".format(c=mocked_method.called))


def side_effect_handler():
    print("side_effect_handler method called")
    return -1


@patch('application.Application.method2', side_effect=side_effect_handler)
def test3(mocked_method):
    app = Application()
    # vytiskneme informaci o tom, zda se mockovaná metoda zavolala
    print("mocked method called: {c}".format(c=mocked_method.called))
    print("method1 returns: {v}".format(v=app.method1()))
    # opět vytiskneme informaci o tom, zda se mockovaná metoda zavolala
    print("mocked method called: {c}".format(c=mocked_method.called))


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test3()
    print()
