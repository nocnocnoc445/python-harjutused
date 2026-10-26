import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "punktid.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("8 7 9\n5 6 7\n10 9 8\n6 8 7\n")

punktid = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 0:
            continue
        opilase_punktid = []
        for osa in osad:
            opilase_punktid.append(int(osa))
        punktid.append(opilase_punktid)

for i in range(len(punktid)):
    summa = 0
    for punkt in punktid[i]:
        summa += punkt
    print(f"Õpilane {i + 1}: {summa} punkti")
