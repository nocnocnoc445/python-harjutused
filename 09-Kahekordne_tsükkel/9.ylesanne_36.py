temperatuurid = [12, 15, 14, 18, 21, 19, 16]
paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]

summa = 0
for t in temperatuurid:
    summa += t
keskmine = summa / len(temperatuurid)

soojem = 0
kulmem = 0
for i in range(len(temperatuurid)):
    if temperatuurid[i] > temperatuurid[soojem]:
        soojem = i
    if temperatuurid[i] < temperatuurid[kulmem]:
        kulmem = i

ule_keskmise = 0
for t in temperatuurid:
    if t > keskmine:
        ule_keskmise += 1

tousud = 0
for i in range(1, len(temperatuurid)):
    if temperatuurid[i] > temperatuurid[i - 1]:
        tousud += 1

print(f"Nädala keskmine temperatuur: {keskmine:.2f}")
print(f"Kõige soojem päev: {paevad[soojem]} ({temperatuurid[soojem]}°)")
print(f"Kõige külmem päev: {paevad[kulmem]} ({temperatuurid[kulmem]}°)")
print("Keskmisest soojemaid päevi:", ule_keskmise)
print("Järgmine päev oli eelmisest soojem:", tousud, "korral")