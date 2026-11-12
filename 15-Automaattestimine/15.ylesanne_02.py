def suurem(a, b):
    if a > b:
        return a
    return b


assert suurem(7, 3) == 7
assert suurem(2, 9) == 9
assert suurem(5, 5) == 5
assert suurem(-4, -10) == -4
assert suurem(-3, 2) == 2

print("Kõik testid läbisid.")
