import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "muuk.txt")):
    with open(os.path.join(KAUST, "muuk.txt"), "w", encoding="utf-8") as fail:
        fail.write('Piim 2.50 10\nLeib 1.80 15\nJuust 4.20 6\nÕun 1.20 20\nJogurt 0.90 12\n')

tooted = []
with open(os.path.join(KAUST, "muuk.txt"), "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 3:
            nimi = osad[0]
            hind = float(osad[1])
            kogus = int(osad[2])
            tooted.append((nimi, hind * kogus))

kogutulu = 0
parim = tooted[0]
read = ["MÜÜGIARUANNE", "------------"]
for nimi, tulu in tooted:
    read.append(f"{nimi:<8} {tulu:>8.2f} €")
    kogutulu += tulu
    if tulu > parim[1]:
        parim = (nimi, tulu)

read.append("------------")
read.append(f"Kogu müügitulu: {kogutulu:.2f} €")
read.append(f"Suurim müügitulu: {parim[0]} ({parim[1]:.2f} €)")

with open(os.path.join(KAUST, "muugiaruanne.txt"), "w", encoding="utf-8") as fail:
    fail.write("\n".join(read) + "\n")

print("\n".join(read))
print()
print("Aruanne salvestatud faili muugiaruanne.txt.")