from app.operaciones import divide
import pytest

def get_data_test_divide():
    return [(10, 2, 5), ("-15/4", "1/2", -7.5), (8, "16", 0.5)]

@pytest.mark.parametrize("num1, num2, esperado", get_data_test_divide())
def test_divide_parametrize(num1, num2, esperado):
    assert divide(num1, num2) == esperado

@pytest.mark.xfail
def test_divide_falla():
    assert divide("7", "0") == "No division by zero is allowed."