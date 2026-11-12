import string

KIRJAVAHEMARGID = string.punctuation + "„“”–—…«»"


def leia_sonad(lause):
    sonad = set()
    for sona in lause.split():
        sona = sona.strip(KIRJAVAHEMARGID).lower()
        if sona:
            sonad.add(sona)
    return sonad


lause1 = input("Sisesta esimene lause: ")
lause2 = input("Sisesta teine lause: ")

sonad1 = leia_sonad(lause1)
sonad2 = leia_sonad(lause2)

print()
print("Esimese lause sõnad:", sorted(sonad1))
print("Teise lause sõnad:", sorted(sonad2))
print("Mõlemas lauses:", sorted(sonad1 & sonad2))
print("Ainult esimeses lauses:", sorted(sonad1 - sonad2))
print("Kõik erinevad sõnad:", sorted(sonad1 | sonad2))
