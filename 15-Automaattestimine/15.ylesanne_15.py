def liida(a, b):
    return a + b


def arvuta():
    a = int(input("Esimene arv: "))
    b = int(input("Teine arv: "))
    print(liida(a, b))


assert liida(2, 3) == 5
assert liida(-4, 4) == 0
assert liida(0, 0) == 0
assert liida(-2, -7) == -9
assert liida(100, 250) == 350

print("Kõik testid läbisid.")
print()

if __name__ == "__main__":
    arvuta()
