"""Implementace jednotkových testů."""

import pytest

from average import average


testdata = [
        ((1, 1), 1),
        ((1, 2), 1.5),
        ((0, 1), 0.5),
        ((1, 2, 3), 2.0),
        ((0, 10), 0.5),
]


@pytest.fixture
def input_values():
    """Vygenerování vstupních hodnot pro jednotkový test."""
    return (1, 2, 3, 4, 5)


@pytest.fixture
def expected_result():
    """Vygenerování očekávaného výsledku testu."""
    return 3


class TestAverageFunction:
    """Jednotkové testy pro otestování funkce average z modulu average."""

    @pytest.mark.parametrize("values,expected", testdata)
    def test_average_basic_1(self, values, expected):
        """Otestování výpočtu průměru."""
        result = average(values)
        assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)

    @pytest.mark.parametrize("values,expected",
                             testdata, ids=["1,1", "1,2", "0,1", "1,2,3", "0,10"])
    def test_average_basic_2(self, values, expected):
        """Otestování výpočtu průměru."""
        result = average(values)
        assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)

    @pytest.mark.parametrize(
        "values,expected",
        [
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
                (0, 10), 0.5
            ),
            pytest.param(
                (), 0
            ),
        ],
    )
    def test_average_basic_3(self, values, expected):
        """Otestování výpočtu průměru."""
        result = average(values)
        assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(expected, result)

    def test_average_empty_list_1(self):
        """Otestování výpočtu průměru pro prázdný vstup."""
        with pytest.raises(ZeroDivisionError) as excinfo:
            result = average([])

    def test_average_empty_list_2(self):
        """Otestování výpočtu průměru pro prázdný vstup."""
        with pytest.raises(Exception) as excinfo:
            result = average([])
        # poměrně křehký způsob testování!
        assert excinfo.type == ZeroDivisionError
        assert str(excinfo.value) == "float division by zero"

    def test_average_five_values(self, input_values, expected_result):
        """Otestování výpočtu průměru."""
        result = average(input_values)
        assert result == expected_result, "Očekávaná hodnota {}, vráceno {}".format(
                expected_result, result)
