import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
LAHTEFAIL = os.path.join(KAUST, "tulemused.txt")
ARUANNE = os.path.join(KAUST, "aruanne.txt")


def maara_hinne(keskmine):
    if keskmine >= 90:
        return 5
    elif keskmine >= 75:
        return 4
    elif keskmine >= 60:
        return 3
    elif keskmine >= 50:
        return 2
    else:
        return 1


def main():
    try:
        with open(LAHTEFAIL, "r", encoding="utf-8") as fail:
            read = fail.readlines()
    except FileNotFoundError:
        print("Viga: lähtefaili tulemused.txt ei leitud.")
        return

    opilased = []
    for rida in read:
        rida = rida.strip()
        if rida == "":
            continue
        osad = rida.split(";")
        if len(osad) < 2:
            print(f"Hoiatus: vigane rida jäeti vahele: {rida}")
            continue
        nimi = osad[0].strip()
        try:
            punktid = [float(p) for p in osad[1:]]
        except ValueError:
            print(f"Hoiatus: vigane rida jäeti vahele: {rida}")
            continue
        keskmine = sum(punktid) / len(punktid)
        opilased.append((nimi, keskmine, maara_hinne(keskmine)))

    if not opilased:
        print("Failis pole ühtegi korrektset õpilast.")
        return

    klassi_keskmine = sum(o[1] for o in opilased) / len(opilased)
    parim = max(opilased, key=lambda o: o[1])
    norgim = min(opilased, key=lambda o: o[1])
    positiivseid = len([o for o in opilased if o[2] >= 3])

    valjund = ["ÕPILASTE TULEMUSTE ARUANNE", "-" * 30, ""]
    for nimi, keskmine, hinne in opilased:
        valjund.append(f"{nimi:<10} Keskmine: {keskmine:.2f}  Hinne: {hinne}")
    valjund.append("")
    valjund.append("-" * 30)
    valjund.append(f"Klassi keskmine: {klassi_keskmine:.2f}")
    valjund.append(f"Parim õpilane: {parim[0]}")
    valjund.append(f"Nõrgim õpilane: {norgim[0]}")
    valjund.append(f"Positiivse hindega õpilasi: {positiivseid}")

    print("\n".join(valjund))

    with open(ARUANNE, "w", encoding="utf-8") as fail:
        fail.write("\n".join(valjund) + "\n")

    print()
    print("Aruanne salvestati faili aruanne.txt.")


main()