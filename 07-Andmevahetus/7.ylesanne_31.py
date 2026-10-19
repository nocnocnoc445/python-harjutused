import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "kontaktid.txt")):
    with open(os.path.join(KAUST, "kontaktid.txt"), "w", encoding="utf-8") as fail:
        fail.write('Mari;mari@example.com;5551001\nJüri;jyri@example.com;5551002\nAnna;anna@example.com;5551003\nPeeter;peeter@example.com;5551004\n')

kontaktid = {}
with open(os.path.join(KAUST, "kontaktid.txt"), "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split(";")
        if len(osad) == 3:
            nimi, email, telefon = osad
            kontaktid[nimi.lower()] = (nimi, email, telefon)

while True:
    otsing = input("Sisesta nimi (tühi rida lõpetab): ").strip()
    if otsing == "":
        print("Head aega!")
        break

    if otsing.lower() in kontaktid:
        nimi, email, telefon = kontaktid[otsing.lower()]
        print(f"{nimi} - e-post: {email}, telefon: {telefon}")
    else:
        print("Sellist kontakti ei leitud.")
    print()