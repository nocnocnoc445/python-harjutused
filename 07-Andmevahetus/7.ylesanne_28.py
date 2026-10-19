import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "temperatuurid.txt")):
    with open(os.path.join(KAUST, "temperatuurid.txt"), "w", encoding="utf-8") as fail:
        fail.write('Esmaspäev 12\nTeisipäev 15\nKolmapäev 11\nNeljapäev 17\nReede 14\nLaupäev 19\nPühapäev 16\n')

paevad = []
with open(os.path.join(KAUST, "temperatuurid.txt"), "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 2:
            paevad.append((osad[0], int(osad[1])))

temperatuurid = [t for paev, t in paevad]
keskmine = sum(temperatuurid) / len(temperatuurid)

soojem = paevad[0]
kulmem = paevad[0]
yle_15 = 0
for paev in paevad:
    if paev[1] > soojem[1]:
        soojem = paev
    if paev[1] < kulmem[1]:
        kulmem = paev
    if paev[1] > 15:
        yle_15 += 1

read = [
    "TEMPERATUURI ARUANNE",
    "--------------------",
    f"Nädala keskmine: {keskmine:.2f} °C",
    f"Kõige soojem päev: {soojem[0]} ({soojem[1]} °C)",
    f"Kõige külmem päev: {kulmem[0]} ({kulmem[1]} °C)",
    f"Päevi üle 15 kraadi: {yle_15}",
]

with open(os.path.join(KAUST, "temperatuuri_aruanne.txt"), "w", encoding="utf-8") as fail:
    fail.write("\n".join(read) + "\n")

print("\n".join(read))
print()
print("Aruanne salvestatud faili temperatuuri_aruanne.txt.")