import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "opilased.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Mari 10 15 20 30 40\n"
                   "Jaan 23 16 19 22\n"
                   "Kati 8 22 17 14 32 17 24 21 2 9 11 17\n"
                   "Peeter 12 28 21 45 26 10\n"
                   "Anna 14 32 25 16 89\n")

opilased = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) < 2:
            continue
        punktid = []
        for osa in osad[1:]:
            punktid.append(int(osa))
        opilased.append([osad[0], punktid])

for opilane in opilased:
    print(f"{opilane[0]}: {len(opilane[1])} kontrolltööd")
