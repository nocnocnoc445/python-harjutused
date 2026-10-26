andmed = ("Mari", [4, 5, 3])

print("Enne muudatust:", andmed)

andmed[1][0] = 5

print("Pärast muudatust:", andmed)

# Ennik hoiab endas viidet järjendile, mitte järjendi koopiat. Ennik ise ei
# muutunud - selles on ikka sama nimi ja sama järjend. Muutus ainult järjendi
# sisu, aga järjend on muudetav andmestruktuur, seega on see lubatud.
