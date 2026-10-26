import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "tulemused.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("12 15 18\n10 20\n25 15 10 5\n30\n")

reanumber = 0
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 0:
            continue
        reanumber += 1

        arvud = []
        for osa in osad:
            arvud.append(int(osa))
        print(f"Rida {reanumber}: {sum(arvud)}")
