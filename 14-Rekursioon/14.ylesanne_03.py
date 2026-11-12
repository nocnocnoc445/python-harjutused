# Ennustus enne käivitamist:
# Algus: 3
# Algus: 2
# Algus: 1
# Algus: 0
# Lopp: 0
# Lopp: 1
# Lopp: 2
# Lopp: 3

def katse(n):
    print("Algus:", n)
    if n > 0:
        katse(n - 1)
    print("Lopp:", n)


katse(3)

# Tulemus vastas ennustusele.
# Lopp-read tulevad vastupidises järjekorras, sest iga väljakutse jääb
# ootama, kuni tema sees tehtud väljakutse lõpetab. Kõige sügavam
# väljakutse (n = 0) lõpetab esimesena ja kõige esimene (n = 3) viimasena.


def katse_muudetud(n):
    print("Algus:", n)
    if n == 1:
        print("Lopp:", n)
        return
    katse_muudetud(n - 1)
    print("Lopp:", n)


print()
print("Muudetud programm (baasjuhtum n == 1):")
katse_muudetud(3)
