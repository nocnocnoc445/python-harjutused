import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "arvud2.txt")
VALJUNDFAIL = os.path.join(KAUST, "suuremad.txt")

# kui andmefaili pole, luuakse see näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("3 18 7 25\n12 40\n9 16 2 15 33\n21\n5 11 28\n")

arvud = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        for osa in rida.split():
            arvud.append(int(osa))

while True:
    try:
        piir = int(input("Sisesta piirväärtus: "))
        break
    except ValueError:
        print("Piirväärtus peab olema täisarv, proovi uuesti.")

suuremad = []
for arv in arvud:
    if arv > piir:
        suuremad.append(arv)

if len(suuremad) == 0:
    print(f"Failis pole ühtegi arvu, mis oleks suurem kui {piir}.")
else:
    print(f"Arvud, mis on suuremad kui {piir}: {suuremad}")

with open(VALJUNDFAIL, "w", encoding="utf-8") as fail:
    for arv in suuremad:
        fail.write(str(arv) + "\n")

print("Leitud arvud salvestati faili suuremad.txt.")
