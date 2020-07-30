"""Základní použití balíčku ctypes, modul pro import."""

import ctypes


library = None


def load_library(library_name):
    """Načtení nativní knihovny."""
    return ctypes.CDLL(library_name)


def add(x, y):
    """Zavolání externí funkce."""
    return library.add(x, y)


def init():
    global library
    library = load_library("libadder.so")


def main():
    """Otestování, jestli je možné zavolat nativní funkci."""
    init()
    print(library)
    result = add(1, 2)
    print(f"1+2=", result, sep="")


if __name__ == '__main__':
    # pouze se ujistíme, že lze zavolat nativní funkci
    main()
