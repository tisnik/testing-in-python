"""Implementace jednotkových testů."""

import pytest

from average import average


def pytest_configure(config):
    """Konfigurace jednotkových testů."""
    config.addinivalue_line(
        "markers", "smoketest: mark test that are performed very smoketest"
    )


testdata = [
        ((1, 1), 1),
        ((1, 2), 1.5),
        ((0, 1), 0.5),
        ((1, 2, 3), 2.0),
        ((0, 10), 5.0),
]


@pytest.mark.parametrize("values,expected", testdata)
def test_average_basic_1(printer, values, expected):
    """Otestování výpočtu průměru."""
    printer("About to compute average from {} with expected output {}".format(values, expected))
    result = average(values)
    printer("Computed average is {}".format(result))
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)
