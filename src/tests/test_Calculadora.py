from src.models.CalculadoraModel import Calculadora


def test_sum():
    assert Calculadora.sum(1, 2) == 3


def test_subtract():
    assert Calculadora.subtract(1, 2) == -1


def test_multiplication():
    assert Calculadora.multiplication(1, 2) == 2


def test_divide():
    assert Calculadora.divide(1, 2) == 0.5
