import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "read.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Esimene rida\nTeine rida\nKolmas rida\nNeljas rida\n")

with open(FAIL, "r", encoding="utf-8") as fail:
    read = fail.readlines()

mittetuhjad = 0
for rida in read:
    if rida.strip() != "":
        mittetuhjad += 1

print(f"Failis on {len(read)} rida.")
print(f"Mittetühje ridu on {mittetuhjad}.")
