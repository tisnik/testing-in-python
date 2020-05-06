"""Implementace jednotkových testů."""

from unittest.mock import *

import module1


@patch('module1.function1', return_value="*mocked*")
def test1(mocked_function):
    print("*** test1 ***")
    value = module1.function1()
    print("function1 returns: {v}".format(v=value))


@patch('module2.function2', return_value="*mocked*")
def test2(mocked_function):
    print("*** test2 ***")
    value = module1.function1()
    print("function1 returns: {v}".format(v=value))


@patch('module1.function2', return_value="*mocked*")
def test3(mocked_function):
    print("*** test3 ***")
    value = module1.function1()
    print("function1 returns: {v}".format(v=value))


@patch('module2.function3', return_value="*mocked*")
def test4(mocked_function):
    print("*** test4 ***")
    value = module1.function1()
    print("function1 returns: {v}".format(v=value))


@patch('module3.function3', return_value="*mocked*")
def test5(mocked_function):
    print("*** test5 ***")
    value = module1.function1()
    print("function1 returns: {v}".format(v=value))


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test3()
    print()

    test4()
    print()

    test5()
    print()
