raamatud = (
    ("Python algajatele", "Kask", 2021, 25.90),
    ("Programmeerimise alused", "Tamm", 2019, 19.50),
    ("Andmestruktuurid", "Saar", 2023, 32.00),
    ("Veebiarendus", "Kivi", 2022, 28.50),
    ("Algoritmid", "Mets", 2020, 35.00)
)


def kuva_raamatud(raamatud):
    if len(raamatud) == 0:
        print("Raamatuid ei leitud.")
        return
    print(f"{'Pealkiri':<26}{'Autor':<8}{'Aasta':<7}{'Hind':>8}")
    for pealkiri, autor, aasta, hind in raamatud:
        print(f"{pealkiri:<26}{autor:<8}{aasta:<7}{hind:>6.2f} €")


def kalleim_ja_odavaim(raamatud):
    kalleim = raamatud[0]
    odavaim = raamatud[0]
    for raamat in raamatud:
        if raamat[3] > kalleim[3]:
            kalleim = raamat
        if raamat[3] < odavaim[3]:
            odavaim = raamat
    return kalleim, odavaim


def keskmine_hind(raamatud):
    summa = 0
    for pealkiri, autor, aasta, hind in raamatud:
        summa += hind
    return summa / len(raamatud)


def ilmunud_parast(raamatud, piiraasta):
    leitud = []
    for raamat in raamatud:
        pealkiri, autor, aasta, hind = raamat
        if aasta > piiraasta:
            leitud.append(raamat)
    return tuple(leitud)


def otsi_pealkirja_jargi(raamatud, otsitav):
    leitud = []
    for raamat in raamatud:
        if otsitav.lower() in raamat[0].lower():
            leitud.append(raamat)
    return tuple(leitud)


while True:
    print()
    print("1 - Kuva kõik raamatud")
    print("2 - Kõige kallim ja odavaim raamat")
    print("3 - Raamatute keskmine hind")
    print("4 - Pärast 2020. aastat ilmunud raamatud")
    print("5 - Otsi raamatut pealkirja järgi")
    print("0 - Välju")
    valik = input("Valik: ").strip()
    print()

    if valik == "1":
        kuva_raamatud(raamatud)
    elif valik == "2":
        kalleim, odavaim = kalleim_ja_odavaim(raamatud)
        print(f"Kõige kallim raamat: {kalleim[0]} ({kalleim[3]:.2f} €)")
        print(f"Kõige odavam raamat: {odavaim[0]} ({odavaim[3]:.2f} €)")
    elif valik == "3":
        print(f"Raamatute keskmine hind: {keskmine_hind(raamatud):.2f} €")
    elif valik == "4":
        kuva_raamatud(ilmunud_parast(raamatud, 2020))
    elif valik == "5":
        otsitav = input("Sisesta pealkiri või selle osa: ").strip()
        if otsitav == "":
            print("Otsingusõna ei tohi olla tühi.")
        else:
            kuva_raamatud(otsi_pealkirja_jargi(raamatud, otsitav))
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik.")
