arve = 0
summa = 0
positiivseid = 0
negatiivseid = 0
paarisarve = 0
paarituid = 0

arv = int(input("Sisesta arv: "))

while arv != 0:
    arve = arve + 1
    summa = summa + arv

    if arv > 0:
        positiivseid = positiivseid + 1
    elif arv < 0:
        negatiivseid = negatiivseid + 1

    if arv % 2 == 0:
        paarisarve = paarisarve + 1
    else:
        paarituid = paarituid + 1

    arv = int(input("Sisesta arv: "))

print()
print("--- TULEMUSED ---")
print()

if arve == 0:
    print("Ühtegi arvu ei sisestatud.")
else:
    keskmine = summa / arve
    print("Sisestatud arve:", arve)
    print("Summa:", summa)
    print(f"Keskmine: {keskmine:.2f}")
    print()
    print("Positiivseid arve:", positiivseid)
    print("Negatiivseid arve:", negatiivseid)
    print("Paarisarve:", paarisarve)
    print("Paarituid arve:", paarituid)

# 1. Enne tsüklit: loendurid (arve, positiivseid, negatiivseid, paarisarve,
#    paarituid) ja summa, kõik väärtusega 0.
# 2. Tsükkel töötab seni, kuni arv != 0.
# 3. Loendurit arve suurendatakse iga sisestatud arvu korral, mis pole 0.
# 4. Summat muudetakse samuti iga arvu korral, mis pole 0.
# 5. arv > 0 on positiivne, arv < 0 on negatiivne.
# 6. arv % 2 == 0 on paaris, muidu paaritu.
# 7. Keskmine = summa / arve, aga ainult siis, kui arve > 0
#    (muidu oleks jagamine nulliga).