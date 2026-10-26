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
    next(lugeja)
    for rida in lugeja:
        if len(rida) < 3:
            continue
        tooted.append([rida[0], float(rida[1]), int(rida[2])])

koguvaartus = 0
print("Toodete koguväärtused:")
for nimetus, hind, kogus in tooted:
    vaartus = hind * kogus
    koguvaartus += vaartus
    print(f"{nimetus}: {hind:.2f} € × {kogus} = {vaartus:.2f} €")

kalleim = tooted[0]
for toode in tooted:
    if toode[1] > kalleim[1]:
        kalleim = toode

print()
print(f"Lao koguväärtus: {koguvaartus:.2f} €")
print(f"Kõige kallima ühikuhinnaga toode: {kalleim[0]} ({kalleim[1]:.2f} €)")
