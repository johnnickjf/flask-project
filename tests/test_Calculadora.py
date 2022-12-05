from src.models.CalculadoraModel import Calculadora


def test_sum():
    assert Calculadora.sum(6, 2) == 8


def test_subtract():
    assert Calculadora.subtract(6, 2) == 4


def test_multiplication():
    assert Calculadora.multiplication(5, 2) == 10


def test_divide():
    assert Calculadora.divide(3, 2) == 1.5
