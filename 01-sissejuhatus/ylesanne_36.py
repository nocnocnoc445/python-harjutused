# VIGA: input() tagastab alati teksti (str), näiteks "17".
# "17" + 1 annab TypeError, sest teksti ja arvu ei saa kokku liita.
# PARANDUS: teisenda sisend int() abil arvuks.

age = int(input("Sisesta vanus: "))
age_next_year = age + 1

print(age_next_year)