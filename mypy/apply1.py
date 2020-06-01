from typing import overload
from typing import Optional


@overload
def factorial(n: None) -> None:
    pass


@overload
def factorial(n: int) -> int:
    pass


def factorial(n: Optional[int]) -> Optional[int]:
    """Rekurzivní výpočet faktoriálu."""
    if n is None:
        return None
    if n < 0:
        return None
    if n == 0:
        return 1

    return n * factorial(n-1)


def apply(function, list):
    return [function(e) for e in list]


print(apply(factorial, [1, 2, 3, 4]))
