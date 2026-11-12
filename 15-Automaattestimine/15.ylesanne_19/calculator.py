def liida(a, b):
    return a + b


def lahuta(a, b):
    return a - b


def korruta(a, b):
    return a * b


def jaga(a, b):
    if b == 0:
        raise ZeroDivisionError("Nulliga ei saa jagada.")
    return a / b
