import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "opilased.txt")):
    with open(os.path.join(KAUST, "opilased.txt"), "w", encoding="utf-8") as fail:
        fail.write('Mari 5 4 5 3\nJüri 3 4\nAnna 5 5 4 5 5\nPeeter 2 3 3\nKati 4 5 5 4 5 5\nMartin 3 4 4\n')

opilased = []
with open(os.path.join(KAUST, "opilased.txt"), "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) < 2:
            continue
        hinded = [int(h) for h in osad[1:]]
        opilased.append((osad[0], sum(hinded) / len(hinded)))

read = ["ÕPILASTE ARUANNE", "----------------"]
for nimi, keskmine in opilased:
    read.append(f"{nimi:<8} {keskmine:.2f}")

klassi_keskmine = sum(k for nimi, k in opilased) / len(opilased)
read.append("----------------")
read.append(f"Klassi keskmine: {klassi_keskmine:.2f}")

with open(os.path.join(KAUST, "opilaste_aruanne.txt"), "w", encoding="utf-8") as fail:
    fail.write("\n".join(read) + "\n")

print("\n".join(read))
print()
print("Aruanne salvestati faili opilaste_aruanne.txt.")