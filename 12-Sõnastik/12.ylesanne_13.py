hinnakiri = {
    "Piim": 1.25,
    "Leib": 1.80,
    "Juust": 4.50,
    "Või": 2.99,
    "Munad": 3.20
}

for toode, hind in hinnakiri.items():
    print(f"{toode} – {hind:.2f} €")