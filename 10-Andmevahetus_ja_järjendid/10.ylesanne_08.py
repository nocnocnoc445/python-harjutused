import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "andmed.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("4 8 12\n5 10 15\n7 14 21\n")

arvud = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        for osa in rida.split():
            arvud.append(int(osa))

print(arvud)
print("Summa:", sum(arvud))
print(f"Keskmine: {sum(arvud) / len(arvud):.2f}")
