hinnad = {
    "Piim": 1.25,
    "Leib": 1.80,
    "Juust": 4.50,
    "Või": 2.99,
    "Munad": 3.20
}

print(f"Leiva hind: {hinnad['Leib']:.2f} €")

hinnad["Juust"] = 4.99   # olemasoleva toote hinna muutmine
hinnad["Kohv"] = 6.49    # uue toote lisamine

print("Uuendatud sõnastik:", hinnad)