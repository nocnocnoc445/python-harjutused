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

paaris = []
paaritud = []
for arv in arvud:
    if arv % 2 == 0:
        paaris.append(arv)
    else:
        paaritud.append(arv)

print("Paarisarvud:", paaris)
print("Paarisarve kokku:", len(paaris))
print("Paaritud arvud:", paaritud)
print("Paarituid arve kokku:", len(paaritud))
