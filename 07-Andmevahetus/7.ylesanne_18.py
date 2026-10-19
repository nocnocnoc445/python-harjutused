import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "sisestatud_arvud.txt")

with open(FAIL, "w", encoding="utf-8") as fail:
    for i in range(1, 6):
        while True:
            try:
                arv = int(input(f"Sisesta {i}. täisarv: "))
                break
            except ValueError:
                print("See pole täisarv, proovi uuesti.")
        fail.write(str(arv) + "\n")

with open(FAIL, "r", encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail if rida.strip()]

print()
print("Sisestatud arvud:", ", ".join(str(a) for a in arvud))
print("Summa:", sum(arvud))
print("Keskmine:", sum(arvud) / len(arvud))