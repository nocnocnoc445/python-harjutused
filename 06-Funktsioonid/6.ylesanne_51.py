def lisa_opilane(nimed, punktid, nimi, tulemus):
    nimed.append(nimi.title())
    punktid.append(tulemus)

def arvuta_hinne(punktid):
    if punktid >= 90:
        return 5
    elif punktid >= 75:
        return 4
    elif punktid >= 50:
        return 3
    elif punktid >= 20:
        return 2
    else:
        return 1

def leia_keskmine(punktid):
    summa = 0
    for p in punktid:
        summa += p
    return summa / len(punktid)

def leia_parim(nimed, punktid):
    indeks = 0
    for i in range(len(punktid)):
        if punktid[i] > punktid[indeks]:
            indeks = i
    return nimed[indeks], punktid[indeks]

def leia_norgim(nimed, punktid):
    indeks = 0
    for i in range(len(punktid)):
        if punktid[i] < punktid[indeks]:
            indeks = i
    return nimed[indeks], punktid[indeks]

def opilase_sona(arv):
    if arv == 1:
        return "õpilane"
    return "õpilast"

def pealkiri(tekst, laius=33):
    print("=" * laius)
    print(tekst.center(laius))
    print("=" * laius)

def kuva_opilased(nimed, punktid):
    if len(nimed) == 0:
        print("Õpilasi pole veel lisatud.")
        return
    pealkiri("KÕIK ÕPILASED")
    for i in range(len(nimed)):
        print(f"{i + 1}. {nimed[i]} - {punktid[i]} p - hinne {arvuta_hinne(punktid[i])}")

def kuva_statistika(nimed, punktid):
    if len(nimed) == 0:
        print("Õpilasi pole veel lisatud.")
        return

    parim_nimi, parim_punktid = leia_parim(nimed, punktid)
    norgim_nimi, norgim_punktid = leia_norgim(nimed, punktid)

    pealkiri("KLASSI STATISTIKA")
    print()
    print("Õpilasi kokku:", len(nimed))
    print(f"Keskmine punktisumma: {leia_keskmine(punktid):.2f}")
    print(f"Parim tulemus: {parim_nimi} ({parim_punktid} p)")
    print(f"Nõrgim tulemus: {norgim_nimi} ({norgim_punktid} p)")
    print()
    print("Hinnete jaotus:")
    for hinne in range(5, 0, -1):
        arv = 0
        for p in punktid:
            if arvuta_hinne(p) == hinne:
                arv += 1
        print(f"Hinne {hinne}: {arv} {opilase_sona(arv)}")

def otsi_opilane(nimed, punktid, nimi):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            return nimed[i], punktid[i]
    return None

def kuva_menuu():
    print()
    pealkiri("ÕPILASTE HINNETE SÜSTEEM")
    print()
    print("1. Lisa õpilane")
    print("2. Kuva kõik õpilased")
    print("3. Kuva klassi statistika")
    print("4. Otsi õpilast nime järgi")
    print("0. Välju")
    print()

def kusi_punktid():
    while True:
        sisend = input("Sisesta punktisumma (0-100): ").strip()
        if sisend.isdigit() and int(sisend) <= 100:
            return int(sisend)
        print("Vigane punktisumma. Proovi uuesti.")

def kas_nimi_olemas(nimed, nimi):
    for olemasolev in nimed:
        if olemasolev.lower() == nimi.lower():
            return True
    return False

nimed = []
punktid = []

while True:
    kuva_menuu()
    valik = input("Vali tegevus: ").strip()

    if valik == "1":
        nimi = input("Sisesta õpilase nimi: ").strip()
        if nimi == "":
            print("Nimi ei tohi olla tühi.")
        elif kas_nimi_olemas(nimed, nimi):
            print("Selle nimega õpilane on juba olemas.")
        else:
            tulemus = kusi_punktid()
            lisa_opilane(nimed, punktid, nimi, tulemus)
            print(f"Õpilane {nimi.title()} lisatud.")
    elif valik == "2":
        kuva_opilased(nimed, punktid)
    elif valik == "3":
        kuva_statistika(nimed, punktid)
    elif valik == "4":
        nimi = input("Sisesta otsitava õpilase nimi: ").strip()
        leitud = otsi_opilane(nimed, punktid, nimi)
        if leitud is None:
            print("Sellist õpilast ei leitud.")
        else:
            print("Õpilane:", leitud[0])
            print("Punktid:", leitud[1])
            print("Hinne:", arvuta_hinne(leitud[1]))
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Vigane valik. Proovi uuesti.")