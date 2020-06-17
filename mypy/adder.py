from typing import TypeVar

IntOrString = TypeVar("IntOrString", str, int)


def add(x: IntOrString, y: IntOrString) -> IntOrString:
    return x + y


print(add(1, 2))
print(add("foo", "bar"))

print(add("foo", 2))
print(add(1, "bar"))

print(42 + add(1, 2))
print(42 + add("foo", "bar"))

print("result: " + add("foo", "bar"))
print("result: " + add(1, 2))
