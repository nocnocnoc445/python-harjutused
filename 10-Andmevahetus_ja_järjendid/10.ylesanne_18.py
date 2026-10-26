import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "tabel2.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("1 2 3\n4 5 6\n")

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

# algse tabeli veerust saab uue tabeli rida
pooratud = []
for veerg in range(len(tabel[0])):
    uus_rida = []
    for rida in range(len(tabel)):
        uus_rida.append(tabel[rida][veerg])
    pooratud.append(uus_rida)

for rida in pooratud:
    print(" ".join(str(arv) for arv in rida))
