import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "numbrid.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("5 10 15 20 25 30\n")

with open(FAIL, "r", encoding="utf-8") as fail:
    rida = fail.readline()

arvud = []
for osa in rida.split():
    arvud.append(int(osa))

print("Arvud:", arvud)
print("Summa:", sum(arvud))
