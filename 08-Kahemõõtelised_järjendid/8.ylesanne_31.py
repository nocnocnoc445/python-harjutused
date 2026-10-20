opilased = [
    ["Mari", 5, 4, 5],
    ["Jüri", 3, 4, 3],
    ["Kati", 5, 5, 4],
    ["Peeter", 4, 3, 4]
]


def keskmine(opilane):
    hinded = opilane[1:]
    summa = 0
    for hinne in hinded:
        summa += hinne
    return summa / len(hinded)


def loe_tais_arv(kysimus, vahim, suurim):
    while True:
        sisend = input(kysimus).strip()
        if sisend.isdigit() and vahim <= int(sisend) <= suurim:
            return int(sisend)
        print(f"Sisesta täisarv vahemikus {vahim}-{suurim}.")


for opilane in opilased:
    print(f"{opilane[0]:<8}Keskmine: {keskmine(opilane):.2f}")

print()
nimi = input("Sisesta otsitava õpilase nimi: ").strip()

leitud = None
for opilane in opilased:
    if opilane[0].lower() == nimi.lower():
        leitud = opilane

if leitud is None:
    print("Sellise nimega õpilast ei leitud.")
else:
    print(f"{leitud[0]} hinded: {leitud[1:]}")
    hinnete_arv = len(leitud) - 1
    jrk = loe_tais_arv(f"Mitmendat hinnet muuta (1-{hinnete_arv})? ", 1, hinnete_arv)
    uus = loe_tais_arv("Uus hinne (1-5): ", 1, 5)
    leitud[jrk] = uus
    print(f"Uuendatud hinded: {leitud[1:]}")
    print(f"Uuendatud keskmine: {keskmine(leitud):.2f}")