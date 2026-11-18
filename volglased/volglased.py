# Leiab arvete (PDF) ja panga väljavõtte (payments.csv) põhjal võlglased.
# Kasutus: python volglased.py [andmete kaust]

import csv
import os
import re
import sys
from datetime import date, datetime

from pypdf import PdfReader


# Teeb nimest võrreldava kuju: "Vesiluuk, Kristel" = "KRISTEL VESILUUK"
def nimi_votmeks(nimi):
    return " ".join(sorted(nimi.replace(",", " ").lower().split()))


# Summa sentideks (täisarvuna ei teki ümardusvigu)
def sentideks(tekst):
    return round(float(tekst.replace(",", ".").replace(" ", "")) * 100)


# Sendid tagasi kujule "130,00 €"
def euro(sendid):
    return f"{sendid / 100:.2f}".replace(".", ",") + " €"


# Loeb kõik PDF-arved ja võtab tekstist välja numbri, kuupäevad, kliendi ja summa
def loe_arved(kaust):
    arved = {}
    for fail in os.listdir(kaust):
        if not fail.lower().endswith(".pdf"):
            continue
        tekst = "\n".join(lk.extract_text() or "" for lk in PdfReader(os.path.join(kaust, fail)).pages)
        nr = int(re.search(r"Arve nr:\s*(\d+)", tekst).group(1))
        arved[nr] = {
            "nr": nr,
            "kuupaev": datetime.strptime(re.search(r"Arve kuupäev:\s*([\d.]+)", tekst).group(1), "%d.%m.%Y").date(),
            "tahtaeg": datetime.strptime(re.search(r"Maksetähtaeg:\s*([\d.]+)", tekst).group(1), "%d.%m.%Y").date(),
            "klient": re.search(r"Klient:\s*\n\s*(.+)", tekst).group(1).strip(),
            "summa": sentideks(re.search(r"SUMMA\s+([\d.,]+)\s*eur", tekst).group(1)),
            "tasutud": 0,
        }
    return arved


# Loeb panga väljavõttest laekumised (K = raha tuli sisse)
def loe_maksed(fail):
    maksed = []
    with open(fail, encoding="utf-8-sig") as f:
        for rida in csv.DictReader(f, delimiter=";"):
            if rida["Deebet/Kreedit"].strip() != "K":
                continue
            maksed.append({
                "kuupaev": datetime.strptime(rida["Kuupäev"], "%d.%m.%Y").date(),
                "maksja": rida["Saaja/Maksja"],
                "selgitus": rida["Selgitus"],
                "summa": sentideks(rida["Summa"]),
                "jaak": sentideks(rida["Summa"]),  # osa maksest, mis on veel sidumata
            })
    return maksed


# Paneb makse arve peale (nii palju, kui maksest on järel ja arvest tasumata)
def seo(makse, arve):
    summa = min(makse["jaak"], arve["summa"] - arve["tasutud"])
    arve["tasutud"] += summa
    makse["jaak"] -= summa


# Seob maksed arvetega kahes läbimises
def seo_maksed(arved, maksed):
    kliendi_arved = {}
    for a in arved.values():
        kliendi_arved.setdefault(nimi_votmeks(a["klient"]), []).append(a)

    # 1. Selgituses on arve number ja maksja on sama klient
    for m in maksed:
        for nr in map(int, re.findall(r"\d+", m["selgitus"])):
            a = arved.get(nr)
            if a and nimi_votmeks(a["klient"]) == nimi_votmeks(m["maksja"]) and m["jaak"] > 0:
                seo(m, a)

    # 2. Numbrita makse: sama kliendi tasumata arve sama summaga (või tema ainus tasumata arve)
    for m in maksed:
        if m["jaak"] <= 0:
            continue
        lahtised = [a for a in kliendi_arved.get(nimi_votmeks(m["maksja"]), [])
                    if a["summa"] > a["tasutud"] and a["kuupaev"] <= m["kuupaev"]]
        tapne = [a for a in lahtised if a["summa"] - a["tasutud"] == m["jaak"]]
        if tapne:
            seo(m, tapne[0])
        elif len(lahtised) == 1:
            seo(m, lahtised[0])


# Leiab andmete kausta: käsurealt, skripti kõrvalt või Downloads kaustast
def leia_kaust():
    if len(sys.argv) > 1:
        return sys.argv[1]
    for kaust in (os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed"),
                  os.path.join(os.path.expanduser("~"), "Downloads", "andmed")):
        if os.path.isdir(kaust):
            return kaust
    sys.exit("Ei leidnud kausta 'andmed'. Anna asukoht: python volglased.py C:\\tee\\andmed")


def main():
    kaust = leia_kaust()
    print("Loen arveid... (2000 PDF-i võtab umbes 10 sekundit)")
    arved = loe_arved(os.path.join(kaust, "invoices"))
    maksed = loe_maksed(os.path.join(kaust, "payments.csv"))
    seo_maksed(arved, maksed)

    # Võlglased = arved, kus tasutud on vähem kui arve summa
    tana = date.today()
    volad = sorted((a for a in arved.values() if a["summa"] > a["tasutud"]), key=lambda a: a["klient"])
    sidumata = [m for m in maksed if m["jaak"] > 0]

    # Tabel ekraanile
    print(f"\nArveid {len(arved)}, makseid {len(maksed)}, sidumata makseid {len(sidumata)}\n")
    print(f"{'Klient':<22}{'Arve':>6}{'Tähtaeg':>12}{'Arve summa':>13}{'Tasutud':>12}{'Võlg':>12}{'Päevi üle':>11}")
    for a in volad:
        print(f"{a['klient']:<22}{a['nr']:>6}{a['tahtaeg'].strftime('%d.%m.%Y'):>12}{euro(a['summa']):>13}"
              f"{euro(a['tasutud']):>12}{euro(a['summa'] - a['tasutud']):>12}{max(0, (tana - a['tahtaeg']).days):>11}")
    print(f"\nVõlglasi {len(volad)}, võlg kokku {euro(sum(a['summa'] - a['tasutud'] for a in volad))}")
    for m in sidumata:
        print(f"Sidumata makse: {m['kuupaev']:%d.%m.%Y} {m['maksja']} {euro(m['jaak'])} ({m['selgitus']})")

    # Sama tabel CSV-faili (Exceli jaoks)
    with open("volglased.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["Klient", "Arve nr", "Arve kuupäev", "Maksetähtaeg", "Arve summa", "Tasutud", "Võlg", "Päevi üle"])
        for a in volad:
            w.writerow([a["klient"], a["nr"], a["kuupaev"].strftime("%d.%m.%Y"), a["tahtaeg"].strftime("%d.%m.%Y"),
                        euro(a["summa"]), euro(a["tasutud"]), euro(a["summa"] - a["tasutud"]),
                        max(0, (tana - a["tahtaeg"]).days)])
    print("\nSalvestatud: volglased.csv")


if __name__ == "__main__":
    main()