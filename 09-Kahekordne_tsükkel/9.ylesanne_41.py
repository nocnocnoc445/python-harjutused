def opilase_keskmine(punktid):
    summa = 0
    for p in punktid:
        summa += p
    return summa / len(punktid)


def leia_keskmised(tulemused):
    keskmised = []
    for punktid in tulemused:
        keskmised.append(opilase_keskmine(punktid))
    return keskmised


def leia_parim(opilased, keskmised):
    parim = 0
    for i in range(len(keskmised)):
        if keskmised[i] > keskmised[parim]:
            parim = i
    return opilased[parim], keskmised[parim]


def toode_keskmised(tulemused):
    keskmised = []
    for too in range(len(tulemused[0])):
        summa = 0
        for opilane in range(len(tulemused)):
            summa += tulemused[opilane][too]
        keskmised.append(summa / len(tulemused))
    return keskmised


def alla_piiri(opilased, keskmised, piir):
    norgad = []
    for i in range(len(keskmised)):
        if keskmised[i] < piir:
            norgad.append(opilased[i])
    return norgad


def kuva_tabel(opilased, tulemused, keskmised):
    laius = len("Õpilane")
    for nimi in opilased:
        if len(nimi) > laius:
            laius = len(nimi)
    laius += 4

    print("KLASSI TULEMUSED")
    print()
    print(f"{'Õpilane':<{laius}}", end="")
    for too in range(len(tulemused[0])):
        print(f"{'Töö ' + str(too + 1):<8}", end="")
    print("Keskmine")

    for i in range(len(opilased)):
        print(f"{opilased[i]:<{laius}}", end="")
        for p in tulemused[i]:
            print(f"{p:<8}", end="")
        print(f"{keskmised[i]:.2f}")


def otsi_opilast(opilased, tulemused, nimi):
    for i in range(len(opilased)):
        if opilased[i].lower() == nimi.lower():
            print()
            print(f"{opilased[i]} tulemused:")
            for too in range(len(tulemused[i])):
                print(f"Töö {too + 1}: {tulemused[i][too]}")
            print(f"Keskmine: {opilase_keskmine(tulemused[i]):.2f}")
            return
    print(f"Õpilast nimega {nimi} ei leitud.")


opilased = ["Mari", "Jüri", "Kati", "Peeter", "Anna"]
tulemused = [
    [85, 90, 78],
    [62, 75, 68],
    [95, 88, 100],
    [40, 55, 48],
    [77, 82, 80]
]

keskmised = leia_keskmised(tulemused)
kuva_tabel(opilased, tulemused, keskmised)

parim_nimi, parim_keskmine = leia_parim(opilased, keskmised)
print()
print(f"Parim õpilane: {parim_nimi} ({parim_keskmine:.2f})")

norgad = alla_piiri(opilased, keskmised, 50)
if len(norgad) > 0:
    print("Alla 50 punkti keskmiselt:", ", ".join(norgad))
else:
    print("Alla 50 punkti keskmiselt: puuduvad")

print()
print("Kontrolltööde keskmised:")
too_keskmised = toode_keskmised(tulemused)
for i in range(len(too_keskmised)):
    print(f"Töö {i + 1}: {too_keskmised[i]:.2f}")

print()
nimi = input("Sisesta õpilase nimi: ")
otsi_opilast(opilased, tulemused, nimi)