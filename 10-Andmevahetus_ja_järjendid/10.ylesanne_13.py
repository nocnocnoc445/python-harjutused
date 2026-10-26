import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "tabel.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("1 2 3\n4 5 6\n7 8 9\n")

tabel = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 0:
            continue
        tabelirida = []
        for osa in osad:
            tabelirida.append(int(osa))
        tabel.append(tabelirida)

print("[")
for i in range(len(tabel)):
    if i < len(tabel) - 1:
        print("    " + str(tabel[i]) + ",")
    else:
        print("    " + str(tabel[i]))
print("]")
