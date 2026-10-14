nimed = []
punktid = []

with open("kontrolltoo.csv", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida != "":
            osad = rida.split(";")
            nimed.append(osad[0].strip())
            punktid.append(int(osad[1].strip()))

hinded = []
for p in punktid:
    if p >= 90:
        hinded.append(5)
    elif p >= 75:
        hinded.append(4)
    elif p >= 50:
        hinded.append(3)
    elif p >= 20:
        hinded.append(2)
    else:
        hinded.append(1)

print("KONTROLLTÖÖ TULEMUSED")
print()
for i in range(len(nimed)):
    print(f"{i + 1}. {nimed[i]} - {punktid[i]} punkti")

suurim = max(punktid)
vaikseim = min(punktid)
parimad = []
halvimad = []
sooritanud = 0
mittesooritanud = 0

for i in range(len(nimed)):
    if punktid[i] == suurim:
        parimad.append(nimed[i])
    if punktid[i] == vaikseim:
        halvimad.append(nimed[i])
    if punktid[i] >= 50:
        sooritanud += 1
    else:
        mittesooritanud += 1

keskmine = sum(punktid) / len(punktid)

print()
print("KONTROLLTÖÖ STATISTIKA")
print()
print("Õpilasi kokku:", len(nimed))
print(f"Keskmine punktisumma: {keskmine:.1f}")
print(f"Parim tulemus: {', '.join(parimad)} - {suurim} punkti")
print(f"Madalaim tulemus: {', '.join(halvimad)} - {vaikseim} punkti")
print(f"Kontrolltöö sooritas: {sooritanud} õpilast")
print(f"Kontrolltööd ei sooritanud: {mittesooritanud} õpilast")

print()
print("HINDED")
print()
for i in range(len(nimed)):
    print(f"{nimed[i]} - {punktid[i]} punkti - hinne {hinded[i]}")

print()
print("ÕPILASE OTSIMINE")
otsitav = input("Sisesta õpilase nimi: ").strip().lower()

leitud = False
for i in range(len(nimed)):
    if nimed[i].lower() == otsitav:
        print("Õpilane:", nimed[i])
        print("Punktid:", punktid[i])
        print("Hinne:", hinded[i])
        leitud = True

if not leitud:
    print("Sellist õpilast ei leitud.")