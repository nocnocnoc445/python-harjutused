import os
import string

KAUST = os.path.dirname(os.path.abspath(__file__))
ANDMED = os.path.join(KAUST, "andmed")
SISEND = os.path.join(ANDMED, "tekst.txt")
VALJUND = os.path.join(ANDMED, "sagedused.txt")

KIRJAVAHEMARGID = string.punctuation + "„“”–—…«»"

NAIDISTEKST = """Python on lihtne ja populaarne programmeerimiskeel.
Python sobib hästi nii algajatele kui ka kogenud programmeerijatele.
Sõnastik on Pythonis väga kasulik andmestruktuur.
Sõnastikus on igal võtmel oma väärtus.
Võtme abil saab väärtuse kiiresti kätte.
Sõnastikku saab lisada uusi võtmeid ja väärtusi.
Sõnastikust saab võtmeid ka kustutada.
Failist loetud teksti saab sõnastiku abil analüüsida.
Iga sõna esinemiste arv salvestatakse sõnastikku.
Nii on lihtne leida teksti kõige sagedasemad sõnad.
Programmeerimine on oskus, mida arendatakse harjutamise kaudu.
Mida rohkem harjutad, seda paremini Python sulle selgeks saab.
"""

# kui tekstifaili veel pole, luuakse see kausta andmed/
if not os.path.exists(SISEND):
    os.makedirs(ANDMED, exist_ok=True)
    with open(SISEND, "w", encoding="utf-8") as f:
        f.write(NAIDISTEKST)

with open(SISEND, "r", encoding="utf-8") as f:
    tekst = f.read()

sagedus = {}
for sona in tekst.split():
    sona = sona.strip(KIRJAVAHEMARGID).lower()
    if sona:
        sagedus[sona] = sagedus.get(sona, 0) + 1

jarjestatud = sorted(sagedus.items(), key=lambda paar: (-paar[1], paar[0]))

print("10 kõige sagedasemat sõna:")
for koht, (sona, arv) in enumerate(jarjestatud[:10], start=1):
    print(f"{koht:>2}. {sona}: {arv}")

# kõik sõnad tähestikulises järjekorras faili
with open(VALJUND, "w", encoding="utf-8") as f:
    for sona in sorted(sagedus):
        f.write(f"{sona} {sagedus[sona]}\n")

print()
print(f"{len(sagedus)} sõna sagedused salvestati faili andmed/sagedused.txt")