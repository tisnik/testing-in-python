from typing import Union


def compare(x: Union[int, str], y: Union[int, str]) -> bool:
    return x < y


print(compare(1, 2))
print(compare(1.2, 3.4))
print(compare("foo", "bar"))
print(compare([1, 2], [3, 4]))
print(compare(True, False))
print(compare(1, "bar"))
print(compare("foo", 2))
