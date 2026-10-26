import csv
import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
SISENDFAIL = os.path.join(KAUST, "kontrolltood.txt")
VALJUNDFAIL = os.path.join(KAUST, "kokkuvote.csv")
PIIR = 80


def loe_andmed(failitee):
    opilased = []
    try:
        with open(failitee, "r", encoding="utf-8") as fail:
            for rida in fail:
                osad = rida.split()
                if len(osad) == 0:
                    continue
                if len(osad) < 2:
                    print(f"Hoiatus: real pole punkte, rida jäeti vahele: {rida.strip()}")
                    continue
                try:
                    punktid = []
                    for osa in osad[1:]:
                        punktid.append(int(osa))
                except ValueError:
                    print(f"Hoiatus: vigane rida jäeti vahele: {rida.strip()}")
                    continue
                opilased.append([osad[0], punktid])
    except FileNotFoundError:
        return None
    return opilased


def arvuta_tulemused(opilased):
    # iga õpilase kohta: [nimi, tööde arv, summa, keskmine, miinimum, maksimum]
    tulemused = []
    for nimi, punktid in opilased:
        summa = sum(punktid)
        keskmine = summa / len(punktid)
        tulemused.append([nimi, len(punktid), summa, keskmine, min(punktid), max(punktid)])
    return tulemused


def salvesta_tulemused(tulemused, failitee):
    with open(failitee, "w", encoding="utf-8", newline="") as fail:
        kirjutaja = csv.writer(fail, delimiter=";")
        kirjutaja.writerow(["Nimi", "Toode_arv", "Summa", "Keskmine", "Miinimum", "Maksimum"])
        for nimi, toode_arv, summa, keskmine, miinimum, maksimum in tulemused:
            kirjutaja.writerow([nimi, toode_arv, summa, f"{keskmine:.2f}", miinimum, maksimum])


def koik_keskmised(tulemused):
    keskmised = []
    for tulemus in tulemused:
        keskmised.append(tulemus[3])
    return keskmised


def nimed_keskmisega(tulemused, otsitav):
    nimed = []
    for tulemus in tulemused:
        if tulemus[3] == otsitav:
            nimed.append(tulemus[0])
    return nimed


def vahemalt_piir(tulemused, piir):
    nimed = []
    for tulemus in tulemused:
        if tulemus[3] >= piir:
            nimed.append(tulemus[0])
    return nimed


def kuva_opilased(tulemused):
    for nimi, toode_arv, summa, keskmine, miinimum, maksimum in tulemused:
        print(nimi)
        print(f"  Kontrolltöid: {toode_arv}")
        print(f"  Punktide summa: {summa}")
        print(f"  Keskmine: {keskmine:.2f}")
        print(f"  Minimaalne: {miinimum}")
        print(f"  Maksimaalne: {maksimum}")
        print()


def kuva_vordlus(silt_yks, silt_mitu, nimed, keskmine):
    # võrdsete tulemuste korral näidatakse kõiki õpilasi
    if len(nimed) == 1:
        print(f"{silt_yks}: {nimed[0]}")
    else:
        print(f"{silt_mitu}: {', '.join(nimed)}")
    print(f"Keskmine tulemus: {keskmine:.2f}")


def main():
    opilased = loe_andmed(SISENDFAIL)
    if opilased is None:
        print("Viga: faili kontrolltood.txt ei leitud. Kontrolli, et fail oleks kaustas andmed.")
        return
    if len(opilased) == 0:
        print("Failis pole ühtegi õpilast, kelle tulemusi analüüsida.")
        return

    tulemused = arvuta_tulemused(opilased)
    keskmised = koik_keskmised(tulemused)
    parim = max(keskmised)
    norgim = min(keskmised)

    print("ÕPILASTE TULEMUSTE ANALÜÜS")
    print()
    print(f"Õpilasi kokku: {len(tulemused)}")
    print()
    kuva_opilased(tulemused)

    kuva_vordlus("Parim õpilane", "Parimad õpilased", nimed_keskmisega(tulemused, parim), parim)
    print()
    kuva_vordlus("Nõrgim õpilane", "Nõrgimad õpilased", nimed_keskmisega(tulemused, norgim), norgim)
    print()
    print(f"Kõigi õpilaste keskmiste keskmine: {sum(keskmised) / len(keskmised):.2f}")
    print()

    head = vahemalt_piir(tulemused, PIIR)
    if len(head) == 0:
        print(f"Keskmisega vähemalt {PIIR}: selliseid õpilasi pole")
    else:
        print(f"Keskmisega vähemalt {PIIR}: {', '.join(head)}")

    salvesta_tulemused(tulemused, VALJUNDFAIL)
    print()
    print("Tulemused salvestati faili kokkuvote.csv")


main()
