maatriks = [
    [3, 5, 7],
    [2, 4, 6],
    [8, 10, 12]
]

summa = 0
paaris_summa = 0
paaritute_arv = 0

for rida in maatriks:
    for arv in rida:
        summa += arv
        if arv % 2 == 0:
            paaris_summa += arv
        else:
            paaritute_arv += 1

print("Kõikide elementide summa:", summa)
print("Paarisarvude summa:", paaris_summa)
print("Paaritute arvude arv:", paaritute_arv)