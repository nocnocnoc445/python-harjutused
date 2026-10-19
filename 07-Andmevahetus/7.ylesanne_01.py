import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(os.path.join(KAUST, "tervitus.txt")):
    with open(os.path.join(KAUST, "tervitus.txt"), "w", encoding="utf-8") as fail:
        fail.write('Tere tulemast Pythoni kursusele!\nTäna õpime failidega töötamist.\nFailides saab andmeid säilitada.\n')

fail = open(os.path.join(KAUST, "tervitus.txt"), "r", encoding="utf-8")
sisu = fail.read()
fail.close()

print(sisu)