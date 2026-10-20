tabel = [
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
]

rea_summad = []

for rida in tabel:
    summa = 0
    for element in rida:
        summa += element
    rea_summad.append(summa)


print(rea_summad)