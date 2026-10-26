import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
OPILASTE_FAIL = os.path.join(KAUST, "opilased.csv")
HINNETE_FAIL = os.path.join(KAUST, "hinded.csv")
# kokkuvote.csv nime kasutab juba kontrollülesanne, seepärast teine nimi
VALJUNDFAIL = os.path.join(KAUST, "hinnete_kokkuvote.csv")

# kui andmefaile pole, luuakse need ülesande näidisandmetega
if not os.path.exists(OPILASTE_FAIL):
    with open(OPILASTE_FAIL, "w", encoding="utf-8") as fail:
        fail.write("ID;Nimi\n101;Mari\n102;Jaan\n103;Kati\n104;Peeter\n")

if not os.path.exists(HINNETE_FAIL):
    with open(HINNETE_FAIL, "w", encoding="utf-8") as fail:
        fail.write("ID;Aine;Hinne\n"
                   "101;Python;5\n102;Python;4\n103;Python;5\n104;Python;3\n"
                   "101;Matemaatika;4\n102;Matemaatika;5\n103;Matemaatika;4\n104;Matemaatika;4\n")

opilased = []
with open(OPILASTE_FAIL, "r", encoding="utf-8", newline="") as fail:
    lugeja = csv.reader(fail, delimiter=";")
    next(lugeja)
    for rida in lugeja:
        if len(rida) == 2:
            opilased.append([rida[0], rida[1]])

hinded = []
with open(HINNETE_FAIL, "r", encoding="utf-8", newline="") as fail:
    lugeja = csv.reader(fail, delimiter=";")
    next(lugeja)
    for rida in lugeja:
        if len(rida) == 3:
            hinded.append([rida[0], rida[1], int(rida[2])])

kokkuvote = []
for opilase_id, nimi in opilased:
    opilase_hinded = []
    kirjeldused = []
    for hinde_id, aine, hinne in hinded:
        if hinde_id == opilase_id:
            opilase_hinded.append(hinne)
            kirjeldused.append(f"{aine} {hinne}")

    if len(opilase_hinded) == 0:
        print(f"{opilase_id} {nimi}: hindeid pole")
        continue

    keskmine = sum(opilase_hinded) / len(opilase_hinded)
    kokkuvote.append([opilase_id, nimi, keskmine])
    print(f"{opilase_id} {nimi}: {', '.join(kirjeldused)} | keskmine {keskmine:.2f}")

with open(VALJUNDFAIL, "w", encoding="utf-8", newline="") as fail:
    kirjutaja = csv.writer(fail, delimiter=";")
    kirjutaja.writerow(["ID", "Nimi", "Keskmine"])
    for opilase_id, nimi, keskmine in kokkuvote:
        kirjutaja.writerow([opilase_id, nimi, f"{keskmine:.2f}"])

print()
print("Kokkuvõte salvestati faili hinnete_kokkuvote.csv.")

if len(kokkuvote) > 0:
    parim = kokkuvote[0][2]
    for opilane in kokkuvote:
        if opilane[2] > parim:
            parim = opilane[2]

    print()
    print(f"Kõrgeim keskmine hinne ({parim:.2f}):")
    for opilase_id, nimi, keskmine in kokkuvote:
        if keskmine == parim:
            print(nimi)
