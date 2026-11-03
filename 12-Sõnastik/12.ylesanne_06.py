kasutajad = {
    "admin": "administraator",
    "mari": "õpetaja",
    "juri": "õpilane",
    "kati": "õpilane",
    "andres": "moderaator"
}

nimi = input("Sisesta kasutajanimi: ").strip().lower()

if nimi in kasutajad:
    print(f"Kasutaja {nimi} roll on: {kasutajad[nimi]}")
else:
    print(f"Kasutajat {nimi} ei leitud.")