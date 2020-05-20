"""Modul s funkcí, která má být testována/mockována."""

from module2 import *


def function1():
    """Testovaná/mockovaná funkce."""
    print("function1")
    return "function1 " + function2()
