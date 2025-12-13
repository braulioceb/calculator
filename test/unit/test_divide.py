from calculator.app.operaciones import divide
import pytest

def get_data_test_divide():
    return [(10, 2, 5), (4, 2, 2.0), (9, 3, 3)]

@pytest.mark.parametrize("num1, num2, esperado", get_data_test_divide())
def test_divide_parametrize(num1, num2, esperado):
    assert divide(num1, num2) == esperado

@pytest.mark.xfail
def test_divide_falla():
    assert divide("7", "0") == 8