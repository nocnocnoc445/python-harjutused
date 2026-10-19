import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "kasutaja.txt")

nimi = input("Sisesta nimi: ")
vanus = input("Sisesta vanus: ")
email = input("Sisesta e-posti aadress: ")

with open(FAIL, "w", encoding="utf-8") as fail:
    fail.write(nimi + "\n")
    fail.write(vanus + "\n")
    fail.write(email + "\n")

print()
print("Faili sisu:")
with open(FAIL, "r", encoding="utf-8") as fail:
    print(fail.read())