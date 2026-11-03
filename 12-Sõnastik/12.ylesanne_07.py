hinnakiri = {
    "Piim": 1.25,
    "Leib": 1.80,
    "Juust": 4.50,
    "Või": 2.99,
    "Munad": 3.20
}

toode = input("Sisesta tootenimi: ").strip().capitalize()
hind = hinnakiri.get(toode)   # olematu võtme korral tuleb None, mitte viga

if hind is None:
    print("Toodet ei leitud")
else:
    print(f"{toode} hind on {hind:.2f} €")