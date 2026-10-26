import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "ilm.csv")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Kuupaev;Temperatuur;Sademed\n"
                   "2026-10-01;8.5;0\n"
                   "2026-10-02;7.2;3.5\n"
                   "2026-10-03;9.1;1.2\n"
                   "2026-10-04;6.8;0\n"
                   "2026-10-05;5.4;4.1\n"
                   "2026-10-06;7.9;0.5\n"
                   "2026-10-07;8.0;0\n")

paevad = []
with open(FAIL, "r", encoding="utf-8", newline="") as fail:
    lugeja = csv.reader(fail, delimiter=";")
    next(lugeja)
    for rida in lugeja:
        if len(rida) < 3:
            continue
        paevad.append([rida[0], float(rida[1]), float(rida[2])])

temperatuuride_summa = 0
sademete_summa = 0
sademeteta = 0
soojem = paevad[0]
kulmem = paevad[0]

for paev in paevad:
    temperatuuride_summa += paev[1]
    sademete_summa += paev[2]
    if paev[2] == 0:
        sademeteta += 1
    if paev[1] > soojem[1]:
        soojem = paev
    if paev[1] < kulmem[1]:
        kulmem = paev

keskmine = temperatuuride_summa / len(paevad)

print(f"Perioodi keskmine temperatuur: {keskmine:.2f} °C")
print(f"Kõige soojem päev: {soojem[0]} ({soojem[1]:.1f} °C)")
print(f"Kõige külmem päev: {kulmem[0]} ({kulmem[1]:.1f} °C)")
print(f"Sademete kogusumma: {sademete_summa:.1f} mm")
print(f"Sademeteta päevi: {sademeteta}")

print()
print("Keskmisest soojemad päevad:")
for kuupaev, temperatuur, sademed in paevad:
    if temperatuur > keskmine:
        print(f"{kuupaev} ({temperatuur:.1f} °C)")
