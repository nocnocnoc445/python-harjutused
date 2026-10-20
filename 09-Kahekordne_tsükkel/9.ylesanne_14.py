arvud = [-5, 8, 0, -3, 12, -7, 4]

positiivseid = 0
negatiivseid = 0
nulle = 0
positiivsete_summa = 0

for arv in arvud:
    if arv > 0:
        positiivseid += 1
        positiivsete_summa += arv
    elif arv < 0:
        negatiivseid += 1
    else:
        nulle += 1

print("Positiivseid:", positiivseid)
print("Negatiivseid:", negatiivseid)
print("Nulle:", nulle)
print("Positiivsete arvude summa:", positiivsete_summa)