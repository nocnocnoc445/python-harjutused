import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "tekst.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Python on populaarne programmeerimiskeel.\n"
                   "Paljud õpilased alustavad programmeerimist pythoniga.\n"
                   "Failide lugemine on lihtne oskus.\n"
                   "PYTHON sobib hästi andmete töötlemiseks.\n"
                   "Kodutööd tuleb esitada õigeaegselt.\n"
                   "Ka see rida räägib Pythonist.\n")

otsitav = input("Sisesta otsitav sõna: ").strip()

if otsitav == "":
    print("Otsitav sõna ei tohi olla tühi.")
else:
    leitud = 0
    reanumber = 0
    with open(FAIL, "r", encoding="utf-8") as fail:
        for rida in fail:
            reanumber += 1
            if otsitav.lower() in rida.lower():
                print(f"Rida {reanumber}: {rida.strip()}")
                leitud += 1

    print(f"Sobivaid ridu: {leitud}")
