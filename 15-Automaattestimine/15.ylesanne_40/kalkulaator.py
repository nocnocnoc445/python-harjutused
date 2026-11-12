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


def astenda(a, b):
    return a ** b


def jaak(a, b):
    if b == 0:
        raise ZeroDivisionError("Nulliga jagamise jääki ei saa leida.")
    return a % b


TEHTED = {
    "+": liida,
    "-": lahuta,
    "*": korruta,
    "/": jaga,
    "**": astenda,
    "%": jaak,
}


def arvuta(a, b, tehe):
    if tehe not in TEHTED:
        raise ValueError(f"Tundmatu tehe: {tehe}")
    return TEHTED[tehe](a, b)


if __name__ == "__main__":
    a = float(input("Esimene arv: "))
    tehe = input("Tehe (+, -, *, /, **, %): ").strip()
    b = float(input("Teine arv: "))
    try:
        print("Tulemus:", arvuta(a, b, tehe))
    except (ValueError, ZeroDivisionError) as viga:
        print("Viga:", viga)
