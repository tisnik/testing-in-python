def compare(x: int, y: int) -> bool:
    return x < y


print(compare(1, 2))
print(compare(1.2, 3.4))
print(compare("foo", "bar"))
print(compare([1, 2], [3, 4]))
print(compare(True, False))
print("string" + compare(True, False))
