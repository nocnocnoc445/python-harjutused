import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "opilased.txt")
VALJUNDFAIL = os.path.join(KAUST, "keskmised.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Mari 10 15 20 30 40\n"
                   "Jaan 23 16 19 22\n"
                   "Kati 8 22 17 14 32 17 24 21 2 9 11 17\n"
                   "Peeter 12 28 21 45 26 10\n"
                   "Anna 14 32 25 16 89\n")

opilased = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) < 2:
            continue
        punktid = []
        for osa in osad[1:]:
            punktid.append(int(osa))
        opilased.append([osad[0], punktid])

keskmised = []
for nimi, punktid in opilased:
    keskmised.append(sum(punktid) / len(punktid))

suurim = max(keskmised)

print("Kõrgeim keskmine tulemus:")
for i in range(len(opilased)):
    if keskmised[i] == suurim:
        nimi = opilased[i][0]
        toode_arv = len(opilased[i][1])
        print(f"{nimi} - keskmine {keskmised[i]:.2f}, kontrolltöid {toode_arv}")

# järjestamiseks pannakse keskmine paaris esimeseks
paarid = []
for i in range(len(opilased)):
    paarid.append([keskmised[i], opilased[i][0]])
paarid.sort(reverse=True)

with open(VALJUNDFAIL, "w", encoding="utf-8") as fail:
    for keskmine, nimi in paarid:
        fail.write(f"{nimi} {keskmine:.2f}\n")

print()
print("Kõigi õpilaste keskmised salvestati faili keskmised.txt.")
