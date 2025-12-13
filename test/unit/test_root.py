from calculator.app.operaciones import root
import pytest 

def obtener_datos_test_multiplica():
    return [(-2, 2, False), (1, 1, 1), (4, 2, 2)]

@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_multiplica())
def test_multiplica_parametrize(num1, num2, esperado):
    assert root(num1, num2) == esperado

@pytest.mark.xfail
def test_multiplica_falla():
    assert root(2, 2) == "pez"
