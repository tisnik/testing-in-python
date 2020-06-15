"""Jednotkové testy pro výpočet faktoriálu."""

from hypothesis import given
from hypothesis.strategies import lists, integers

from factorial import factorial

precomputed = [
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
    3628800,
    39916800,
    479001600,
    6227020800,
    87178291200,
    1307674368000,
    20922789888000,
    355687428096000,
    6402373705728000,
    121645100408832000,
    2432902008176640000,
    51090942171709440000,
    1124000727777607680000,
    25852016738884976640000,
    620448401733239439360000,
    15511210043330985984000000,
    403291461126605635584000000,
    10888869450418352160768000000,
    304888344611713860501504000000,
    8841761993739701954543616000000,
    265252859812191058636308480000000,
]


@given(integers(min_value=1, max_value=30))
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) == precomputed[value]


@given(integers().filter(lambda x: x < 0))
def test_factorial(value):
    """Jednotkový test pro výpočet faktoriálu."""
    assert factorial(value) is None
