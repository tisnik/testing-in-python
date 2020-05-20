"""Modul s funkcí, která má být testována/mockována."""

from module3 import *


def function2():
    """Testovaná/mockovaná funkce."""
    print("function2")
    return "function2 " + function3()
