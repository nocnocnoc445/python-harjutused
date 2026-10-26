import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "tooted.csv")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Nimetus;Hind;Kogus\nPiim;1.50;12\nLeib;2.20;8\nSai;1.80;15\nJuust;4.50;5\nJogurt;0.90;20\n")

tooted = []
with open(FAIL, "r", encoding="utf-8", newline="") as fail:
    lugeja = csv.reader(fail, delimiter=";")
    next(lugeja)  # päiserida jäetakse vahele
    for rida in lugeja:
        if len(rida) < 3:
            continue
        nimetus = rida[0]
        hind = float(rida[1])
        kogus = int(rida[2])
        tooted.append([nimetus, hind, kogus])

print(f"{'Nimetus':<10}{'Hind':>10}{'Kogus':>8}")
for nimetus, hind, kogus in tooted:
    print(f"{nimetus:<10}{hind:>8.2f} €{kogus:>8}")
