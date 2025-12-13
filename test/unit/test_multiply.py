from calculator.app.operaciones import multiply
import pytest 

def obtener_datos_test_multiplica():
    return [(-2, 3, -6), (2, 0.5, 1), (10, 2, 20)]

@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_multiplica())
def test_multiplica_parametrize(num1, num2, esperado):
    assert multiply(num1, num2) == esperado

@pytest.mark.xfail
def test_multiplica_falla():
    assert multiply(2, 4) == "pez"
