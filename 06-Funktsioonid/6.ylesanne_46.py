def liida(a, b):
    return a + b

def lahuta(a, b):
    return a - b

def korruta(a, b):
    return a * b

def jaga(a, b):
    if b == 0:
        return None
    return a / b

while True:
    print()
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("0. Lõpeta")
    valik = input("Vali tehe: ")

    if valik == "0":
        print("Head aega!")
        break

    if valik not in ["1", "2", "3", "4"]:
        print("Vale valik.")
        continue

    a = float(input("Sisesta esimene arv: "))
    b = float(input("Sisesta teine arv: "))

    if valik == "1":
        print("Tulemus:", liida(a, b))
    elif valik == "2":
        print("Tulemus:", lahuta(a, b))
    elif valik == "3":
        print("Tulemus:", korruta(a, b))
    elif valik == "4":
        tulemus = jaga(a, b)
        if tulemus is None:
            print("Nulliga ei saa jagada.")
        else:
            print("Tulemus:", tulemus)