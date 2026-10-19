import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "tekst.txt")):
    with open(os.path.join(KAUST, "tekst.txt"), "w", encoding="utf-8") as fail:
        fail.write('Python on populaarne programmeerimiskeel.\nPython sobib hästi algajatele.\nFailide töötlemine on oluline oskus.\n')

with open(os.path.join(KAUST, "tekst.txt"), "r", encoding="utf-8") as fail:
    tekst = fail.read()

sonad = tekst.split()

print(f"Tekstis on {len(sonad)} sõna.")