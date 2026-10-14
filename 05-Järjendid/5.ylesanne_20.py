arvud = [-12, 5, 0, 18, -7, 23, -3, 9]

positiivseid = 0
negatiivseid = 0
nulle = 0
positiivsete_summa = 0
negatiivsed = []

for arv in arvud:
    if arv > 0:
        positiivseid += 1
        positiivsete_summa += arv
    elif arv < 0:
        negatiivseid += 1
        negatiivsed.append(arv)
    else:
        nulle += 1

print("Positiivseid arve:", positiivseid)
print("Negatiivseid arve:", negatiivseid)
print("Nulle:", nulle)
print("Positiivsete arvude summa:", positiivsete_summa)
print("Negatiivsed arvud:", negatiivsed)