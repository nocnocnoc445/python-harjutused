koik_oigused = {"read", "write", "delete", "admin"}

kasutajad = {
    "mari": {"read", "write"},
    "juri": {"read"},
    "admin": {"read", "write", "delete", "admin"}
}

# tegevused ja nende jaoks nõutud õigused
tegevused = {
    "vaatamine": {"read"},
    "muutmine": {"read", "write"},
    "kustutamine": {"read", "write", "delete"},
    "haldamine": {"read", "write", "delete", "admin"}
}


def vorminda(oigused):
    if not oigused:
        return "-"
    return ", ".join(sorted(oigused))


def kusi_kasutaja(kusimus="Kasutajanimi: "):
    nimi = input(kusimus).strip().lower()
    if nimi not in kasutajad:
        print(f"Kasutajat {nimi} ei ole olemas.")
        print(f"Olemasolevad kasutajad: {vorminda(kasutajad)}")
        return None
    return nimi


def kusi_oigus(kusimus="Õigus: "):
    oigus = input(kusimus).strip().lower()
    if oigus not in koik_oigused:
        print(f"Tundmatu õigus: {oigus}")
        print(f"Lubatud õigused: {vorminda(koik_oigused)}")
        return None
    return oigus


def lisa_kasutaja():
    nimi = input("Uue kasutaja nimi: ").strip().lower()
    if not nimi:
        print("Nimi ei tohi olla tühi.")
        return
    if nimi in kasutajad:
        print(f"Kasutaja {nimi} on juba olemas.")
        return

    print(f"Lubatud õigused: {vorminda(koik_oigused)}")
    sisend = input("Algsed õigused komadega eraldatult (Enter = ilma õigusteta): ")
    oigused = set(sisend.lower().replace(",", " ").split())

    tundmatud = oigused - koik_oigused
    if tundmatud:
        print(f"Tundmatud õigused: {vorminda(tundmatud)}. Kasutajat ei lisatud.")
        return

    kasutajad[nimi] = oigused
    print(f"Kasutaja {nimi} lisati. Õigused: {vorminda(oigused)}")


def lisa_oigus():
    nimi = kusi_kasutaja()
    if nimi is None:
        return
    oigus = kusi_oigus("Lisatav õigus: ")
    if oigus is None:
        return

    if oigus in kasutajad[nimi]:
        print(f"Kasutajal {nimi} on õigus {oigus} juba olemas.")
    else:
        kasutajad[nimi].add(oigus)
        print(f"Kasutajale {nimi} lisati õigus {oigus}.")


def eemalda_oigus():
    nimi = kusi_kasutaja()
    if nimi is None:
        return
    oigus = kusi_oigus("Eemaldatav õigus: ")
    if oigus is None:
        return

    if oigus in kasutajad[nimi]:
        kasutajad[nimi].remove(oigus)
        print(f"Kasutajalt {nimi} eemaldati õigus {oigus}.")
    else:
        print(f"Kasutajal {nimi} ei ole õigust {oigus}.")


def kuva_oigused():
    nimi = kusi_kasutaja()
    if nimi is None:
        return
    print(f"Kasutaja {nimi} õigused: {vorminda(kasutajad[nimi])}")


def vordle_kasutajaid():
    nimi1 = kusi_kasutaja("Esimene kasutaja: ")
    if nimi1 is None:
        return
    nimi2 = kusi_kasutaja("Teine kasutaja: ")
    if nimi2 is None:
        return

    a = kasutajad[nimi1]
    b = kasutajad[nimi2]
    print()
    print(f"Ühised õigused: {vorminda(a & b)}")
    print(f"Ainult kasutajal {nimi1}: {vorminda(a - b)}")
    print(f"Ainult kasutajal {nimi2}: {vorminda(b - a)}")
    if a == b:
        print("Kasutajate õigused on täpselt samad.")


def leia_oigusega():
    oigus = kusi_oigus("Otsitav õigus: ")
    if oigus is None:
        return

    leitud = set()
    for nimi, oigused in kasutajad.items():
        if oigus in oigused:
            leitud.add(nimi)

    if leitud:
        print(f"Õigus {oigus} on kasutajatel: {vorminda(leitud)}")
    else:
        print(f"Õigust {oigus} ei ole ühelgi kasutajal.")


def kontrolli_tegevust():
    nimi = kusi_kasutaja()
    if nimi is None:
        return

    nimekiri = list(tegevused)
    print("Tegevused:")
    for nr, tegevus in enumerate(nimekiri, start=1):
        print(f"  {nr} - {tegevus} (vaja: {vorminda(tegevused[tegevus])})")

    valik = input("Vali tegevus: ").strip()
    if not (valik.isdigit() and 1 <= int(valik) <= len(nimekiri)):
        print("Vigane valik.")
        return

    tegevus = nimekiri[int(valik) - 1]
    nouded = tegevused[tegevus]
    if nouded <= kasutajad[nimi]:
        print(f"Kasutajal {nimi} on kõik õigused tegevuseks: {tegevus}.")
    else:
        print(f"Kasutaja {nimi} ei saa teha tegevust: {tegevus}.")
        print(f"Puuduvad õigused: {vorminda(nouded - kasutajad[nimi])}")


while True:
    print()
    print("==== KASUTAJATE ÕIGUSED ====")
    print()
    print("1 -> Lisa uus kasutaja")
    print("2 -> Lisa kasutajale õigus")
    print("3 -> Eemalda kasutajalt õigus")
    print("4 -> Kuva kasutaja õigused")
    print("5 -> Võrdle kahe kasutaja õigusi")
    print("6 -> Leia kasutajad kindla õigusega")
    print("7 -> Kontrolli tegevuseks vajalikke õigusi")
    print("0 -> Lõpeta")
    valik = input("Vali tegevus: ").strip()
    print()

    if valik == "1":
        lisa_kasutaja()
    elif valik == "2":
        lisa_oigus()
    elif valik == "3":
        eemalda_oigus()
    elif valik == "4":
        kuva_oigused()
    elif valik == "5":
        vordle_kasutajaid()
    elif valik == "6":
        leia_oigusega()
    elif valik == "7":
        kontrolli_tegevust()
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Vigane valik, proovi uuesti.")
