import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "arvud.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("12\n7\n25\n6\n10\n")

arvud = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        if rida.strip() != "":
            arvud.append(int(rida))

print("Arvude summa:", sum(arvud))
