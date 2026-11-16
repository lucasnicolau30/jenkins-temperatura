import pytest

from src.temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius


def test_f_para_c_ponto_de_congelamento():
    assert fahrenheit_para_celsius(32) == 0


def test_f_para_c_ponto_de_ebulicao():
    assert fahrenheit_para_celsius(212) == 100


def test_c_para_f_ponto_de_congelamento():
    assert celsius_para_fahrenheit(0) == 32


def test_c_para_f_valor_negativo():
    assert celsius_para_fahrenheit(-40) == pytest.approx(-40)
