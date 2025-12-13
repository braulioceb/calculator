from app.operaciones import subtract
import pytest 

def get_data_test_subtact():
    return [(0.5, 0.5, 0), ("1/2", "1", -0.5), (10, "5", 5)]


@pytest.mark.parametrize("num1, num2, esperado", get_data_test_subtact())
def test_subtract_parametrize(num1, num2, esperado):
    assert subtract(num1, num2) == esperado


@pytest.mark.xfail
def test_resta_falla():
    assert subtract(2, 2) == 5