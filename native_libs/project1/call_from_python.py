"""Základní použití balíčku ctypes."""

import ctypes


def load_library(library_name):
    """Načtení nativní knihovny."""
    return ctypes.CDLL(library_name)


def main():
    """Otestování, jestli je možné zavolat nativní funkci."""
    library = load_library("libadder.so")
    print(library)
    result = library.add(1, 2)
    print(f"1+2=", result, sep="")


if __name__ == '__main__':
    # pouze se ujistíme, že lze zavolat nativní funkci
    main()
