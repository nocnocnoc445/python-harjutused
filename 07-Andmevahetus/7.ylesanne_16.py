import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

tooted = []
while True:
    toode = input("Sisesta toode: ").strip()
    if toode.upper() == "STOP":
        break
    if toode:
        tooted.append(toode)

with open(os.path.join(KAUST, "ostunimekiri.txt"), "w", encoding="utf-8") as fail:
    for toode in tooted:
        fail.write(toode + "\n")

print()
print("Ostunimekiri salvestatud.")