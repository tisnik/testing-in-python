from typing import overload
from typing import Optional
from typing import Callable, List


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


def apply(function: Callable, list: List[int]) -> List[int]:
    return [function(e) for e in list]


print(apply(factorial, [1, 2, 3, 4]))
print(apply(factorial, [1, 2.2, "foo", 4]))
