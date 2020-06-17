"""Test, zda je vstupní hodnota prvočíslem."""


def is_prime(x):
    """Test, zda je vstupní hodnota prvočíslem."""
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    return not any(x % y == 0 for y in range(3, int(x**0.5) + 1, 2))
