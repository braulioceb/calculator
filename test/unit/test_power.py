import pytest

from calculator.app.operaciones import power


def get_data_test_power():
    return [
        (2, 3, 8),
        (1, 5, 1),
        (0, 1, 0),
        (0, 0, False),
    ]


@pytest.mark.parametrize(
    "num1, num2, esperado",
    get_data_test_power(),
)
def test_power_parametrized(num1, num2, esperado):
    assert power(num1, num2) == esperado
