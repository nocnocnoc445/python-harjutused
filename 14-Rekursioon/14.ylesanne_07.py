def faktoriaal(n):
    if n < 0:
        raise ValueError("Negatiivse arvu faktoriaali ei saa arvutada.")
    if n == 0:
        return 1
    return n * faktoriaal(n - 1)


print("faktoriaal(5) =", faktoriaal(5))
print("faktoriaal(0) =", faktoriaal(0))
print("faktoriaal(7) =", faktoriaal(7))

try:
    faktoriaal(-3)
except ValueError as viga:
    print("faktoriaal(-3) -> ValueError:", viga)
