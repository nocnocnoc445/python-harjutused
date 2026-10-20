def Leia_suurim_ja_väikseim(arvud):
    # Alustame esimesest elemendist, et programm töötaks ka negatiivsete arvudega

    suurim = arvud[0]
    väikseim = arvud[0]

    for arv in arvud:
        if arv > suurim:
            suurim = arv
        elif arv < väikseim:
            väikseim = arv

    return suurim, väikseim



arvud = [23, 5, 78, 12, 45, 9]
suurim, väikseim = Leia_suurim_ja_väikseim(arvud)
print("Järjend", arvud)
print("Suurim", suurim)
print("Väikseim", väikseim)

print()

negatiivsed = [-23, -5, -78, -12, -45, -9]
suurim, väikseim = Leia_suurim_ja_väikseim(negatiivsed)
print("Järjend:", negatiivsed)
print("Suurim:", suurim)
print("Väikseim:", väikseim)