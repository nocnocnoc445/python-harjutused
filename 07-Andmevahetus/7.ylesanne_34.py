import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "hinded.txt")):
    with open(os.path.join(KAUST, "hinded.txt"), "w", encoding="utf-8") as fail:
        fail.write('Mari 5\nJüri 3\nAnna 4\nPeeter 2\nKati 5\nMartin 4\n')
HINDEFAIL = os.path.join(KAUST, "hinded.txt")
ARUANDEFAIL = os.path.join(KAUST, "hinnete_aruanne.txt")


def loe_opilased():
    opilased = []
    try:
        with open(HINDEFAIL, "r", encoding="utf-8") as fail:
            for rida in fail:
                osad = rida.split()
                if len(osad) == 2 and osad[1].isdigit():
                    opilased.append((osad[0], int(osad[1])))
    except FileNotFoundError:
        pass
    return opilased


def statistika(opilased):
    read = []
    if not opilased:
        read.append("Andmeid pole.")
        return read
    hinded = [h for nimi, h in opilased]
    read.append(f"Õpilasi: {len(opilased)}")
    read.append(f"Keskmine hinne: {sum(hinded) / len(hinded):.2f}")
    read.append("Hinnete sagedus:")
    for hinne in range(5, 0, -1):
        read.append(f"  {hinne}: {hinded.count(hinne)}")
    return read


while True:
    print()
    print("1. Kuva kõik õpilased")
    print("2. Lisa uus õpilane ja hinne")
    print("3. Otsi õpilast")
    print("4. Kuva hinnete statistika")
    print("5. Salvesta aruanne faili")
    print("6. Lõpeta")
    valik = input("Vali tegevus: ").strip()
    print()

    if valik == "1":
        opilased = loe_opilased()
        if not opilased:
            print("Õpilasi pole.")
        for nimi, hinne in opilased:
            print(f"{nimi:<10} {hinne}")

    elif valik == "2":
        nimi = input("Õpilase nimi: ").strip()
        hinne = input("Hinne (1-5): ").strip()
        if nimi == "" or " " in nimi:
            print("Nimi peab olema üks sõna ega tohi olla tühi.")
        elif hinne not in ["1", "2", "3", "4", "5"]:
            print("Hinne peab olema 1 kuni 5.")
        else:
            with open(HINDEFAIL, "a", encoding="utf-8") as fail:
                fail.write(f"{nimi} {hinne}\n")
            print("Õpilane lisatud.")

    elif valik == "3":
        otsitav = input("Sisesta nimi: ").strip().lower()
        leitud = [o for o in loe_opilased() if o[0].lower() == otsitav]
        if leitud:
            for nimi, hinne in leitud:
                print(f"{nimi}: hinne {hinne}")
        else:
            print("Sellist õpilast ei leitud.")

    elif valik == "4":
        print("\n".join(statistika(loe_opilased())))

    elif valik == "5":
        opilased = loe_opilased()
        read = ["HINNETE ARUANNE", "---------------"]
        for nimi, hinne in opilased:
            read.append(f"{nimi:<10} {hinne}")
        read.append("---------------")
        read += statistika(opilased)
        with open(ARUANDEFAIL, "w", encoding="utf-8") as fail:
            fail.write("\n".join(read) + "\n")
        print("Aruanne salvestati faili hinnete_aruanne.txt.")

    elif valik == "6":
        print("Head aega!")
        break

    else:
        print("Tundmatu valik.")