from typing import overload
from typing import Optional
from typing import Callable, List
from typing import Dict, Any


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


def asDict(function: Callable, list: List[int]) -> Dict[int, int]:
    return {value: function(value) for value in list}


print(asDict(factorial, [1, 2, 3, 4]))
print(asDict(factorial, [1, 2.2, "foo", 4]))
