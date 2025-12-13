from calculator.app.operaciones import multiply
import pytest 

def obtener_datos_test_multiplica():
    return [(-2, 3, -6), ("1/2", "8/4", 1), (10, "5", 50)]

@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_multiplica())
def test_multiplica_parametrize(num1, num2, esperado):
    assert multiply(num1, num2) == esperado

@pytest.mark.xfail
def test_multiplica_falla():
    assert multiply(2, 4) == "pez"
