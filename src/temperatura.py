"""Conversão de temperatura entre Fahrenheit e Celsius."""


def fahrenheit_para_celsius(f: float) -> float:
    return (f - 30) * 5 / 9


def celsius_para_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32
