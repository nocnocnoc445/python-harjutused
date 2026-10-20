def leia_keskmine(punktid):
    summa = 0
    for p in punktid:
        summa += p
    return summa / len(punktid)


def leia_parim(nimed, punktid):
    parim = 0
    for i in range(len(punktid)):
        if punktid[i] > punktid[parim]:
            parim = i
    return nimed[parim], punktid[parim]


def loenda_vahemalt(punktid, piir):
    loendur = 0
    for p in punktid:
        if p >= piir:
            loendur += 1
    return loendur


def alla_piiri(nimed, punktid, piir):
    tulemus = []
    for i in range(len(punktid)):
        if punktid[i] < piir:
            tulemus.append(nimed[i])
    return tulemus


nimed = ["Mari", "Jüri", "Kati", "Peeter", "Anna"]
punktid = [85, 62, 94, 48, 77]

for i in range(len(nimed)):
    print(f"{nimed[i]}: {punktid[i]}")

print()
print(f"Rühma keskmine: {leia_keskmine(punktid):.2f}")

parim_nimi, parim_tulemus = leia_parim(nimed, punktid)
print(f"Kõrgeim tulemus: {parim_nimi} ({parim_tulemus})")

print("Vähemalt 50 punkti said:", loenda_vahemalt(punktid, 50), "õpilast")
print("Alla 50 punkti said:", alla_piiri(nimed, punktid, 50))