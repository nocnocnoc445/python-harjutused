import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "ostunimekiri.txt")

tooted = []
while True:
    toode = input("Sisesta toode: ").strip()
    if toode.upper() == "STOP":
        break
    if toode:
        tooted.append(toode)

with open(FAIL, "a", encoding="utf-8") as fail:
    for toode in tooted:
        fail.write(toode + "\n")

print()
print("Tooted lisatud ostunimekirja.")
print()
print("Kogu ostunimekiri:")
with open(FAIL, "r", encoding="utf-8") as fail:
    print(fail.read())