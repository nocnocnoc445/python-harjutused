import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "tervitus.txt")):
    with open(os.path.join(KAUST, "tervitus.txt"), "w", encoding="utf-8") as fail:
        fail.write('Tere tulemast Pythoni kursusele!\nTäna õpime failidega töötamist.\nFailides saab andmeid säilitada.\n')

with open(os.path.join(KAUST, "tervitus.txt"), "r", encoding="utf-8") as fail:
    for nr, rida in enumerate(fail, start=1):
        print(f"{nr}: {rida.strip()}")