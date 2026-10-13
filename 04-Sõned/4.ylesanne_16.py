kasutajanimi = input("Kasutajanimi: ")

if len(kasutajanimi) < 5 or len(kasutajanimi) > 15:
    print("Viga: kasutajanime pikkus peab olema 5–15 tähemärki.")
elif not (kasutajanimi.isascii() and kasutajanimi.isalnum()):
    print("Viga: kasutajanimi tohib sisaldada ainult ladina tähti ja numbreid.")
elif not kasutajanimi[0].isalpha():
    print("Viga: kasutajanimi peab algama tähega.")
else:
    print("Kasutajanimi sobib.")