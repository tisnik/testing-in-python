"""Implementace jednotkových testů."""

from unittest.mock import *

import module1


def test1():
    print("*** test1 ***")

    with patch("module1.add_implementation") as mocked_function:
        mocked_function.return_value = 42

        value = module1.add(1, 2)
        print("add returns: {v}".format(v=value))
        print("mocked function called: {c}".format(c=mocked_function.called))
        mocked_function.assert_called_with(1, 2)

        value = module1.add(100, 100)
        print("add returns: {v}".format(v=value))
        print("mocked function called: {c}".format(c=mocked_function.called))
        mocked_function.assert_called_with(100, 100)

        print("calls: ", mocked_function.mock_calls)


def test2():
    print("*** test2 ***")

    with patch("module1.add_implementation") as mocked_function:
        mocked_function.return_value = 42

        value = module1.add(1, 2)
        print("add returns: {v}".format(v=value))
        print("mocked function called: {c}".format(c=mocked_function.called))
        mocked_function.assert_called_with(1, 1)


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()
