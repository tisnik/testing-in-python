"""Implementace jednotkových testů."""

import pytest

import average


@pytest.mark.parametrize(
    "values,expected",
    (
        pytest.param(
            (1, 1), 1
        ),
        pytest.param(
            (1, 2), 1.5
        ),
        pytest.param(
            (0, 1), 0.5
        ),
        pytest.param(
            (1, 2, 3), 2.0
        ),
        pytest.param(
            (0, 10), 5.0
        ),
    ),
)
def test_average_more_values(values, expected):
    """Otestování výpočtu průměru."""
    result = average.avg(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)
