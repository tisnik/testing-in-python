"""Základní použití balíčku ctypes."""

from adder import init, add


def main():
    """Otestování, jestli je možné zavolat nativní funkci."""
    init()
    result = add("foo", "bar")
    print(f"'foo'+'bar'=", result, sep="")


if __name__ == '__main__':
    # pouze se ujistíme, že lze zavolat nativní funkci
    main()
