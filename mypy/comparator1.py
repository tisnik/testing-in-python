def compare(x, y):
    return x < y


if __name__ == '__main__':
    # pouze se ujistíme, že lze spustit funkci compare
    print(compare(1, 2))
    print(compare(1.2, 3.4))
    print(compare("foo", "bar"))
    print(compare([1, 2], [3, 4]))
    print(compare(True, False))
