seadmed = {
    "IT001": {
        "tyyp": "Sülearvuti",
        "tootja": "Dell",
        "mudel": "Latitude 5540",
        "asukoht": "Ruum 421",
        "staatus": "Kasutusel"
    },
    "IT002": {
        "tyyp": "Monitor",
        "tootja": "LG",
        "mudel": "27UP650",
        "asukoht": "Ruum 403",
        "staatus": "Kasutusel"
    },
    "IT003": {
        "tyyp": "Printer",
        "tootja": "HP",
        "mudel": "LaserJet Pro",
        "asukoht": "Ladu",
        "staatus": "Laos"
    }
}

STAATUSED = ["Kasutusel", "Laos", "Remondis", "Maha kantud"]

# muudetavad tekstiväljad ja nende nimed ekraanil
VALJAD = {
    "tyyp": "Seadme tüüp",
    "tootja": "Tootja",
    "mudel": "Mudel",
    "asukoht": "Kasutaja või asukoht"
}


def suur_algustaht(tekst):
    return tekst[0].upper() + tekst[1:]


def kusi_tekst(kusimus, vaikimisi=None):
    while True:
        vastus = input(kusimus).strip()
        if vastus:
            return vastus
        if vaikimisi is not None:
            return vaikimisi
        print("Väli ei tohi olla tühi.")


def vali_staatus(praegune=None):
    print("Staatused:")
    for nr, staatus in enumerate(STAATUSED, start=1):
        print(f"  {nr} - {staatus}")

    vihje = f" (Enter = {praegune})" if praegune else ""
    while True:
        valik = input(f"Vali staatus{vihje}: ").strip()
        if not valik and praegune:
            return praegune
        if valik.isdigit() and 1 <= int(valik) <= len(STAATUSED):
            return STAATUSED[int(valik) - 1]
        print("Vigane valik.")


def kusi_inventarinumber():
    return input("Inventarinumber: ").strip().upper()


def tabeli_pais():
    print(f"{'Inv.nr':<8}{'Tüüp':<14}{'Tootja ja mudel':<24}{'Asukoht':<18}Staatus")
    print("-" * 76)


def kuva_rida(inv, andmed):
    seade = f"{andmed['tootja']} {andmed['mudel']}"
    print(f"{inv:<8}{andmed['tyyp']:<14}{seade:<24}{andmed['asukoht']:<18}{andmed['staatus']}")


def kuva_koik():
    if not seadmed:
        print("Inventuuris pole ühtegi seadet.")
        return
    tabeli_pais()
    for inv in sorted(seadmed):
        kuva_rida(inv, seadmed[inv])


def lisa_seade():
    inv = kusi_inventarinumber()
    if not inv:
        print("Inventarinumber ei tohi olla tühi.")
        return
    if inv in seadmed:
        print(f"Inventarinumber {inv} on juba kasutusel.")
        return

    uus = {}
    for vali, nimi in VALJAD.items():
        uus[vali] = kusi_tekst(f"{nimi}: ")
    uus["tyyp"] = suur_algustaht(uus["tyyp"])
    uus["staatus"] = vali_staatus()

    seadmed[inv] = uus
    print(f"Seade {inv} lisati.")


def otsi_seadet():
    otsing = input("Sisesta inventarinumber või otsingusõna: ").strip().lower()
    if not otsing:
        print("Otsingusõna ei tohi olla tühi.")
        return

    # otsitakse inventarinumbrist ja kõigist seadme andmetest
    leitud = {}
    for inv, andmed in seadmed.items():
        tekstid = [inv] + list(andmed.values())
        if any(otsing in tekst.lower() for tekst in tekstid):
            leitud[inv] = andmed

    if not leitud:
        print("Ühtegi seadet ei leitud.")
        return


    tabeli_pais()
    for inv in sorted(leitud):
        kuva_rida(inv, leitud[inv])
    print(f"Leitud seadmeid: {len(leitud)}")



def muuda_seadet():
    inv = kusi_inventarinumber()
    if inv not in seadmed:
        print(f"Seadet {inv} ei leitud.")
        return

    andmed = seadmed[inv]
    print("Vajuta Enter, kui väärtust ei muuda.")
    for vali, nimi in VALJAD.items():
        andmed[vali] = kusi_tekst(f"{nimi} ({andmed[vali]}): ", andmed[vali])
    andmed["tyyp"] = suur_algustaht(andmed["tyyp"])
    andmed["staatus"] = vali_staatus(andmed["staatus"])

    print(f"Seadme {inv} andmed uuendati.")


def eemalda_seade():
    inv = kusi_inventarinumber()
    if inv not in seadmed:
        print(f"Seadet {inv} ei leitud.")
        return

    kuva_rida(inv, seadmed[inv])
    kinnitus = input("Kas eemaldada seade? (j/e) ").strip().lower()
    if kinnitus == "j":
        seadmed.pop(inv)
        print(f"Seade {inv} eemaldati.")
    else:
        print("Eemaldamine tühistati.")


def kokkuvote():
    tyybid = {}
    staatused = {}
    for andmed in seadmed.values():
        tyybid[andmed["tyyp"]] = tyybid.get(andmed["tyyp"], 0) + 1
        staatused[andmed["staatus"]] = staatused.get(andmed["staatus"], 0) + 1

    print(f"Seadmeid kokku: {len(seadmed)}")

    print()
    print("Tüübi järgi:")
    for tyyp, arv in sorted(tyybid.items()):
        print(f"  {tyyp:<16}{arv}")

    print()
    print("Staatuse järgi:")
    for staatus, arv in sorted(staatused.items()):
        print(f"  {staatus:<16}{arv}")


while True:
    print()
    print("==== INVENTUUR ====")
    print()
    print("1 -> Kuva kõik seadmed")
    print("2 -> Lisa seade")
    print("3 -> Otsi seadet")
    print("4 -> Muuda seadet")
    print("5 -> Eemalda seade")
    print("6 -> Kokkuvõte")
    print("0 -> Lõpeta")
    valik = input("Vali tegevus: ").strip()

    if valik == "1":
        kuva_koik()
    elif valik == "2":
        lisa_seade()
    elif valik == "3":
        otsi_seadet()
    elif valik == "4":
        muuda_seadet()
    elif valik == "5":
        eemalda_seade()
    elif valik == "6":
        kokkuvote()
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Vigane valik, proovi uuesti.")