import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "maatriks.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("5 8 3\n12 4 7\n6 19 2\n")

maatriks = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 0:
            continue
        maatriksi_rida = []
        for osa in osad:
            maatriksi_rida.append(int(osa))
        maatriks.append(maatriksi_rida)

suurim = maatriks[0][0]
suurima_rida = 0
suurima_veerg = 0
for i in range(len(maatriks)):
    for j in range(len(maatriks[i])):
        if maatriks[i][j] > suurim:
            suurim = maatriks[i][j]
            suurima_rida = i
            suurima_veerg = j

print("Suurim arv:", suurim)
print("Rida:", suurima_rida + 1)
print("Veerg:", suurima_veerg + 1)
