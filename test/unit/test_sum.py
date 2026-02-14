from calculator.app.operaciones import sum
import pytest


def get_data_test_sum():
    return [(0.5, 0.5, 1), (-3, -3, -6), (4, 6, 10)]

@pytest.mark.parametrize("num1, num2, esperado", get_data_test_sum())
def test_suma_parametrize(num1, num2, esperado):
    assert sum(num1, num2) == esperado

@pytest.mark.xfail
def test_suma_falla():
    assert sum(2, 2) == 5
