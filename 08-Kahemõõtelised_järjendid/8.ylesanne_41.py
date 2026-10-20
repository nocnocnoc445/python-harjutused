from decimal import Decimal, ROUND_HALF_UP

opilased = [
    ["Mari", [5, 4, 5, 3]],
    ["Jüri", [3, 4, 3]],
    ["Kati", [5, 5, 4, 5]],
    ["Peeter", [4, 3, 4]],
    ["Anna", [5, 4]]
]


def keskmine(hinded):
    if len(hinded) == 0:
        return None
    summa = 0
    for hinne in hinded:
        summa += hinne
    return summa / len(hinded)


def vorminda(arv):
    # Ümardab tavapäraselt (4.125 -> 4.13), mitte Pythoni vaikimisi viisil
    if arv is None:
        return "-"
    return str(Decimal(str(arv)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def otsi(nimi):
    for opilane in opilased:
        if opilane[0].lower() == nimi.lower():
            return opilane
    return None


def kuva_opilane(opilane):
    nimi = opilane[0]
    hinded = opilane[1]
    print(f"{nimi:<8}Hinded: {str(hinded):<14}Hindeid: {len(hinded)}  "
          f"Keskmine: {vorminda(keskmine(hinded))}")


def kuva_tulemused():
    print("ÕPILASTE TULEMUSED")
    print()
    for opilane in opilased:
        kuva_opilane(opilane)


def klassi_statistika():
    koik_arv = 0
    summa = 0
    viied = 0
    kolmed = 0
    for opilane in opilased:
        for hinne in opilane[1]:
            koik_arv += 1
            summa += hinne
            if hinne == 5:
                viied += 1
            elif hinne == 3:
                kolmed += 1

    print("KLASSI STATISTIKA")
    print()
    print("Hindeid kokku:", koik_arv)
    if koik_arv > 0:
        print("Klassi keskmine:", vorminda(summa / koik_arv))
    else:
        print("Klassi keskmine: -")
    print("Viite arv:", viied)
    print("Kolmede arv:", kolmed)


def parimad_opilased():
    parim = None
    for opilane in opilased:
        k = keskmine(opilane[1])
        if k is not None and (parim is None or k > parim):
            parim = k

    if parim is None:
        print("Parimat õpilast ei saa leida - hindeid pole.")
        return

    nimed = []
    for opilane in opilased:
        if keskmine(opilane[1]) == parim:
            nimed.append(opilane[0])

    if len(nimed) == 1:
        print(f"Parim õpilane: {nimed[0]} ({vorminda(parim)})")
    else:
        print(f"Parimad õpilased: {', '.join(nimed)} ({vorminda(parim)})")


def otsi_opilane():
    nimi = input("Õpilase nimi: ").strip()
    opilane = otsi(nimi)
    if opilane is None:
        print("Sellise nimega õpilast ei leitud.")
    else:
        print(f"{opilane[0]} hinded: {opilane[1]}")
        print(f"Keskmine: {vorminda(keskmine(opilane[1]))}")


def lisa_hinne():
    nimi = input("Õpilase nimi: ").strip()
    opilane = otsi(nimi)
    if opilane is None:
        print("Sellise nimega õpilast ei leitud.")
        return

    sisend = input("Uus hinne (1-5): ").strip()
    if not sisend.isdigit() or not 1 <= int(sisend) <= 5:
        print("Lubatud on ainult täisarvud 1-5.")
        return

    opilane[1].append(int(sisend))
    print("Hinne lisatud. Uuendatud andmed:")
    kuva_opilane(opilane)


kuva_tulemused()
print()
klassi_statistika()
print()
parimad_opilased()

while True:
    print()
    print("1 - Kuva kõik tulemused")
    print("2 - Klassi statistika")
    print("3 - Parim õpilane")
    print("4 - Otsi õpilast")
    print("5 - Lisa hinne")
    print("0 - Välju")
    valik = input("Valik: ").strip()

    if valik == "1":
        kuva_tulemused()
    elif valik == "2":
        klassi_statistika()
    elif valik == "3":
        parimad_opilased()
    elif valik == "4":
        otsi_opilane()
    elif valik == "5":
        lisa_hinne()
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik.")