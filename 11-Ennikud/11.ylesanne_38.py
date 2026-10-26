tooted = (
    ("Monitor", 200, 180),
    ("Hiir", 30, 35),
    ("Klaviatuur", 80, 65),
    ("Printer", 150, 150)
)

for nimetus, vana_hind, uus_hind in tooted:
    muutus = (uus_hind - vana_hind) / vana_hind * 100

    if uus_hind > vana_hind:
        olukord = "tõusis"
    elif uus_hind < vana_hind:
        olukord = "langes"
    else:
        olukord = "jäi samaks"

    print(f"{nimetus}: {vana_hind} € -> {uus_hind} €, hind {olukord} ({muutus:.2f}%)")
