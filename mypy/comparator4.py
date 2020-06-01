from typing import Union
from typing import TypeVar

IntOrString = TypeVar("IntOrString", str, int)


def compare(x: IntOrString, y: IntOrString) -> bool:
    return x < y


print(compare(1, 2))
print(compare(1.2, 3.4))
print(compare("foo", "bar"))
print(compare([1, 2], [3, 4]))
print(compare(True, False))
