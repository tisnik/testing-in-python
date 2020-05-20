"""Modul s funkcí, která má být testována/mockována."""

from module2 import *


def function1():
    print("function1")
    return "function1 " + function2()
