"""Implementace jednotkových testů."""

from unittest.mock import *

import module1


def test1():
    with patch("module1.function1", return_value="*mocked"):
        print("*** test1 ***")
        value = module1.function1()
        print("function1 returns: {v}".format(v=value))


def test2():
    with patch("module2.function2", return_value="*mocked"):
        print("*** test2 ***")
        value = module1.function1()
        print("function1 returns: {v}".format(v=value))


def test3():
    with patch("module1.function2", return_value="*mocked"):
        print("*** test3 ***")
        value = module1.function1()
        print("function1 returns: {v}".format(v=value))


def test4():
    with patch("module2.function3", return_value="*mocked"):
        print("*** test4 ***")
        value = module1.function1()
        print("function1 returns: {v}".format(v=value))


def test5():
    with patch("module3.function3", return_value="*mocked"):
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
