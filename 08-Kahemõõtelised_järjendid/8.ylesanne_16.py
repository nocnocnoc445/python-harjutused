arvud = [
    [4, 8, 12],
    [5, 10],
    [7, 14, 21, 28],
    [3]
]

summad = []
for rida in arvud:
    summa = 0
    for arv in rida:
        summa += arv
    summad.append(summa)

print(summad)  # väljund: [24, 15, 70, 3]