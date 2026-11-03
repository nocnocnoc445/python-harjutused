kontaktid = {
    "Mari": "5551 0001",
    "Jüri": "5551 0002",
    "Kati": "5551 0003",
    "Andres": "5551 0004",
    "Liis": "5551 0005",

}



def korrektne_number(number):
    puhas = number.replace(" ", "").replace("-", "")
    if puhas.startswith("+"):
        puhas = puhas[1:]
    return puhas.isdigit() and len(puhas) >= 5


def kusi_number(kusimus="Sisesta telefoninumber: "):
    number = input(kusimus).strip()
    while not korrektne_number(number):
        number = input("Vigane number. Sisesta uuesti: ").strip()
    return number



def lisa_kontakt():
    nimi = input("Nimi: ").strip().title()
    if not nimi:
        print("Nimi ei tohi olla tühi.")
    elif nimi in kontaktid:
        print(f"Kontakt {nimi} on juba olemas.")
    else:
        kontaktid[nimi] = kusi_number()
        print(f"Kontakt {nimi} lisatud.")



def otsi_kontakti():
    otsing = input("Otsitav nimi või selle osa: ").strip().lower()
    leitud = {nimi: nr for nimi, nr in kontaktid.items() if otsing in nimi.lower()}
    if otsing and leitud:
        for nimi, nr in sorted(leitud.items()):
            print(f"{nimi}: {nr}")
    else:
        print("Kontakti ei leitud.")




def muuda_kontakti():
    nimi = input("Kelle numbrit muuta: ").strip().title()
    if nimi in kontaktid:
        print(f"Praegune number: {kontaktid[nimi]}")
        uus = kusi_number("Sisesta uus telefoninumber: ")
        if uus == kontaktid[nimi]:
            print("Number on juba sama, muudatusi ei tehtud.")
        else:
            kontaktid[nimi] = uus
            print(f"Kontakti {nimi} number muudeti.")
    else:
        print(f"Kontakti {nimi} ei leitud.")



def kustuta_kontakti():
    nimi = input("Kelle kontakt kustutada: ").strip().title()
    number = kontaktid.pop(nimi, None)
    if number is None:
        print(f"Kontakti {nimi} ei leitud.")
    else:
        print(f"Kustutati: {nimi} ({number})")  




def kuva_kõik():
    if not kontaktid:
        print("Telefoniraamat on tühi.")
        return
    for nimi, nr in sorted(kontaktid.items()):
        print(f"{nimi:<15}{nr}")
    print(f"Kontakte kokku: {len(kontaktid)}")



while True:
    print()
    print("==== TELEFONIRAAMAT ====")
    print()
    print("1 -> Lisa kontakt")
    print("2 -> Otsi kontakti")
    print("3 -> Muuda kontakti")
    print("4 -> Kustuta kontakt")
    print("5 -> Kuva kõik kontaktid")
    print("0 -> lõpeta")

    valik = input("Valik: ").strip()
    print()


    if valik == "1":
        lisa_kontakt()
    elif valik == "2":
        otsi_kontakti()
    elif valik == "3":
        muuda_kontakti()
    elif valik == "4":
        kustuta_kontakti()
    elif valik == "5":
        kuva_kõik()
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Vigane valik. Proovi uuesti.")