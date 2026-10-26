ilm = (
    ("Esmaspäev", 18),
    ("Teisipäev", 21),
    ("Kolmapäev", 19),
    ("Neljapäev", 24),
    ("Reede", 22),
    ("Laupäev", 26),
    ("Pühapäev", 23)
)

summa = 0
soojem = ilm[0]
kulmem = ilm[0]
for paev, temperatuur in ilm:
    summa += temperatuur
    if temperatuur > soojem[1]:
        soojem = (paev, temperatuur)
    if temperatuur < kulmem[1]:
        kulmem = (paev, temperatuur)

keskmine = summa / len(ilm)

print("NÄDALA ILMAKOKKUVÕTE")
print()
print(f"Keskmine temperatuur: {keskmine:.1f} °C")
print(f"Kõige soojem päev: {soojem[0]} ({soojem[1]} °C)")
print(f"Kõige külmem päev: {kulmem[0]} ({kulmem[1]} °C)")
