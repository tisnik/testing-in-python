"""Základní použití balíčku ctypes, modul pro import."""

import ctypes


library = None


def load_library(library_name):
    """Načtení nativní knihovny."""
    return ctypes.CDLL(library_name)


def add(x, y):
    """Zavolání externí funkce."""
    return library.add(x, y)


def equal(x, y):
    """Zavolání externí funkce."""
    return library.equal(x, y)


def init():
    global library
    library = load_library("libadder.so")

    library.add.argtypes = (Complex, Complex)
    library.add.restype = Complex

    library.equal.argtypes = (Complex, Complex)
    library.equal.restype = bool


class Complex(ctypes.Structure):
    _fields_ = [("real", ctypes.c_float), ("imag", ctypes.c_float)]

    def __str__(self):
        return "Complex: %f + i%f" % (self.real, self.imag)

    def __eq__(self, other):
        return equal(self, other)


def main():
    """Otestování, jestli je možné zavolat nativní funkci."""
    init()
    print(library)

    c1 = Complex(1.0, 2.0)
    c2 = Complex(3.0, 4.0)

    c3 = add(c1, c2)

    print(c1)
    print(c2)
    print(c3)

    print("c1==c2?", equal(c1, c2))
    print("c2==c2?", equal(c2, c2))


if __name__ == '__main__':
    # pouze se ujistíme, že lze zavolat nativní funkci
    main()
