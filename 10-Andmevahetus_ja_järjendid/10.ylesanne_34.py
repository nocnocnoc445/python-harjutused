import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "ulesanded.csv")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("ID;Ulesanne;Tahtaeg;Staatus\n"
                   "1;Python harjutused;2026-10-20;Pooleli\n"
                   "2;Matemaatika kodutoo;2026-10-22;Tegemata\n"
                   "3;Esitluse koostamine;2026-10-25;Valmis\n")

STAATUSED = ["Tegemata", "Pooleli", "Valmis"]


def loe_ulesanded(failitee):
    ulesanded = []
    with open(failitee, "r", encoding="utf-8", newline="") as fail:
        lugeja = csv.reader(fail, delimiter=";")
        next(lugeja)
        for rida in lugeja:
            if len(rida) == 4 and rida[0].isdigit():
                ulesanded.append([int(rida[0]), rida[1], rida[2], rida[3]])
    return ulesanded


def salvesta_ulesanded(failitee, ulesanded):
    with open(failitee, "w", encoding="utf-8", newline="") as fail:
        kirjutaja = csv.writer(fail, delimiter=";")
        kirjutaja.writerow(["ID", "Ulesanne", "Tahtaeg", "Staatus"])
        for ulesanne in ulesanded:
            kirjutaja.writerow(ulesanne)


def kuva_ulesanded(ulesanded):
    if len(ulesanded) == 0:
        print("Ülesandeid pole.")
        return
    print(f"{'ID':<5}{'Ülesanne':<25}{'Tähtaeg':<13}Staatus")
    for ulesande_id, nimetus, tahtaeg, staatus in ulesanded:
        print(f"{ulesande_id:<5}{nimetus:<25}{tahtaeg:<13}{staatus}")


def leia_ulesanne(ulesanded, otsitav_id):
    for ulesanne in ulesanded:
        if ulesanne[0] == otsitav_id:
            return ulesanne
    return None


def kusi_ulesanne(ulesanded):
    sisend = input("Sisesta ülesande ID: ").strip()
    if not sisend.isdigit():
        print("ID peab olema positiivne täisarv.")
        return None
    ulesanne = leia_ulesanne(ulesanded, int(sisend))
    if ulesanne is None:
        print(f"Ülesannet ID-ga {sisend} ei ole olemas.")
    return ulesanne


def kas_kuupaev(tekst):
    # tähtaeg peab olema kujul AAAA-KK-PP, siis saab tähtaegu sõnedena võrrelda
    if len(tekst) != 10 or tekst[4] != "-" or tekst[7] != "-":
        return False
    return tekst[0:4].isdigit() and tekst[5:7].isdigit() and tekst[8:10].isdigit()


def kusi_staatus():
    for i in range(len(STAATUSED)):
        print(f"{i + 1} - {STAATUSED[i]}")
    valik = input("Vali uus staatus: ").strip()
    if valik in ["1", "2", "3"]:
        return STAATUSED[int(valik) - 1]
    print("Tundmatu staatus.")
    return None


ulesanded = loe_ulesanded(FAIL)

# uus ID peab olema suurem kõigist seni kasutatud ID-dest, ka kustutatutest
suurim_id = 0
for ulesanne in ulesanded:
    if ulesanne[0] > suurim_id:
        suurim_id = ulesanne[0]

while True:
    print()
    print("1. Kuva kõik ülesanded")
    print("2. Lisa uus ülesanne")
    print("3. Muuda ülesande staatust")
    print("4. Kustuta ülesanne")
    print("5. Kuva lõpetamata ülesanded")
    print("6. Salvesta ja lõpeta")
    print("7. Sorteeri ülesanded tähtaja järgi")
    valik = input("Vali tegevus: ").strip()
    print()

    if valik == "1":
        kuva_ulesanded(ulesanded)

    elif valik == "2":
        nimetus = input("Ülesande nimetus: ").strip()
        tahtaeg = input("Tähtaeg (AAAA-KK-PP): ").strip()
        if nimetus == "":
            print("Ülesande nimetus ei tohi olla tühi.")
        elif not kas_kuupaev(tahtaeg):
            print("Tähtaeg peab olema kujul AAAA-KK-PP, näiteks 2026-11-01.")
        else:
            suurim_id += 1
            ulesanded.append([suurim_id, nimetus, tahtaeg, "Tegemata"])
            print(f"Ülesanne lisati ID-ga {suurim_id}.")

    elif valik == "3":
        ulesanne = kusi_ulesanne(ulesanded)
        if ulesanne is not None:
            print(f"Praegune staatus: {ulesanne[3]}")
            staatus = kusi_staatus()
            if staatus is not None:
                ulesanne[3] = staatus
                print("Staatus muudetud.")

    elif valik == "4":
        ulesanne = kusi_ulesanne(ulesanded)
        if ulesanne is not None:
            ulesanded.remove(ulesanne)
            print(f"Ülesanne \"{ulesanne[1]}\" kustutati.")

    elif valik == "5":
        lopetamata = []
        for ulesanne in ulesanded:
            if ulesanne[3] != "Valmis":
                lopetamata.append(ulesanne)
        if len(lopetamata) == 0:
            print("Kõik ülesanded on valmis.")
        else:
            kuva_ulesanded(lopetamata)

    elif valik == "6":
        salvesta_ulesanded(FAIL, ulesanded)
        print("Muudatused salvestati faili ulesanded.csv. Head aega!")
        break

    elif valik == "7":
        ulesanded.sort(key=lambda ulesanne: ulesanne[2])
        print("Ülesanded sorteeriti tähtaja järgi.")
        kuva_ulesanded(ulesanded)

    else:
        print("Tundmatu valik.")
