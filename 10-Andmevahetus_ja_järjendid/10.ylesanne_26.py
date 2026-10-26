import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "tooted.csv")
VALJUNDFAIL = os.path.join(KAUST, "soodsad.csv")

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

while True:
    sisend = input("Sisesta maksimaalne hind: ").strip().replace(",", ".")
    try:
        max_hind = float(sisend)
        break
    except ValueError:
        print("Hind peab olema arv, näiteks 2.00.")

soodsad = []
for toode in tooted:
    if toode[1] <= max_hind:
        soodsad.append(toode)

if len(soodsad) == 0:
    print("Sellise hinnaga tooteid ei leitud.")
else:
    for nimetus, hind, kogus in soodsad:
        print(f"{nimetus} - {hind:.2f} €")

with open(VALJUNDFAIL, "w", encoding="utf-8", newline="") as fail:
    kirjutaja = csv.writer(fail, delimiter=";")
    kirjutaja.writerow(["Nimetus", "Hind", "Kogus"])
    for nimetus, hind, kogus in soodsad:
        kirjutaja.writerow([nimetus, f"{hind:.2f}", kogus])

print()
print("Sobivad tooted salvestati faili soodsad.csv.")
