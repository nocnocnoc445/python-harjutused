import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "muuk.csv")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Kuupäev;Toode;Kogus;Uhikuhind\n"
                   "2026-10-01;Piim;5;1.50\n"
                   "2026-10-01;Leib;3;2.20\n"
                   "2026-10-02;Juust;2;4.50\n"
                   "2026-10-02;Piim;4;1.50\n"
                   "2026-10-03;Leib;6;2.20\n")

tehingud = []
with open(FAIL, "r", encoding="utf-8", newline="") as fail:
    lugeja = csv.reader(fail, delimiter=";")
    next(lugeja)
    for rida in lugeja:
        if len(rida) < 4:
            continue
        tehingud.append([rida[0], rida[1], int(rida[2]), float(rida[3])])

kogukaive = 0
kaive_paevade_kaupa = {}
uhikud_toodete_kaupa = {}

print("Müügitehingud:")
for kuupaev, toode, kogus, uhikuhind in tehingud:
    summa = kogus * uhikuhind
    kogukaive += summa
    print(f"{kuupaev} {toode}: {kogus} × {uhikuhind:.2f} € = {summa:.2f} €")

    if kuupaev in kaive_paevade_kaupa:
        kaive_paevade_kaupa[kuupaev] += summa
    else:
        kaive_paevade_kaupa[kuupaev] = summa

    if toode in uhikud_toodete_kaupa:
        uhikud_toodete_kaupa[toode] += kogus
    else:
        uhikud_toodete_kaupa[toode] = kogus

parim_paev = ""
for kuupaev in kaive_paevade_kaupa:
    if parim_paev == "" or kaive_paevade_kaupa[kuupaev] > kaive_paevade_kaupa[parim_paev]:
        parim_paev = kuupaev

print()
print(f"Kogukäive: {kogukaive:.2f} €")
print(f"Suurima käibega kuupäev: {parim_paev} ({kaive_paevade_kaupa[parim_paev]:.2f} €)")
print()
print("Müüdud ühikud toodete kaupa:")
for toode in uhikud_toodete_kaupa:
    print(f"{toode}: {uhikud_toodete_kaupa[toode]} tk")
