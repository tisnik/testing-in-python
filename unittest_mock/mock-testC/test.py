"""Implementace jednotkových testů."""

from unittest.mock import *

from module1 import *


def test1():
    print("*** test1 ***")

    value = compute(1, 2, 3)
    print("compute returns: {v}".format(v=value))


def mock_call_info(mocked_function):
    print("mocked function '{n}' called: {c}".format(n=mocked_function._mock_name,
                                                     c=mocked_function.called))
    print("calls: ", mocked_function.mock_calls)
    print()


@patch("module1.f1", name="f1", return_value=0)
def test2(mocked_f1):
    print("*** test1 ***")

    value = compute(10, 20, 30)
    print("compute returns: {v}".format(v=value))

    mock_call_info(mocked_f1)


@patch("module1.f1", name="f1", return_value=0)
@patch("module1.f2", name="f2", return_value=0)
def test3(mocked_f2, mocked_f1):
    print("*** test3 ***")

    value = compute(1, 2, 3)
    print("compute returns: {v}".format(v=value))

    mock_call_info(mocked_f1)
    mock_call_info(mocked_f2)


@patch("module1.f1", name="f1", return_value=0)
@patch("module1.f2", name="f2", return_value=0)
@patch("module1.f3", name="f3", return_value=0)
def test4(mocked_f3, mocked_f2, mocked_f1):
    print("*** test4 ***")

    value = compute(100, 200, 300)
    print("compute returns: {v}".format(v=value))

    mock_call_info(mocked_f1)
    mock_call_info(mocked_f2)
    mock_call_info(mocked_f3)


if __name__ == '__main__':
    test1()
    print()

    test2()
    print()

    test3()
    print()

    test4()
    print()
