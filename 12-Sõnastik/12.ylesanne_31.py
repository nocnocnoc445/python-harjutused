import os
import string

KAUST = os.path.dirname(os.path.abspath(__file__))
ANDMED = os.path.join(KAUST, "andmed")
FAIL = os.path.join(ANDMED, "tekst.txt")

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
if not os.path.exists(FAIL):
    os.makedirs(ANDMED, exist_ok=True)
    with open(FAIL, "w", encoding="utf-8") as f:
        f.write(NAIDISTEKST)

with open(FAIL, "r", encoding="utf-8") as f:
    tekst = f.read()

sagedus = {}
for sona in tekst.split():
    sona = sona.strip(KIRJAVAHEMARGID).lower()
    if sona:
        sagedus[sona] = sagedus.get(sona, 0) + 1

# sageduse järgi kahanevalt, võrdse sageduse korral tähestiku järgi
jarjestatud = sorted(sagedus.items(), key=lambda paar: (-paar[1], paar[0]))

print("10 kõige sagedasemat sõna:")
for koht, (sona, arv) in enumerate(jarjestatud[:10], start=1):
    print(f"{koht:>2}. {sona}: {arv}")