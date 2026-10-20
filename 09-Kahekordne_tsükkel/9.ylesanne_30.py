def veergude_summad(tabel):
    summad = []
    for veerg in range(len(tabel[0])):
        summa = 0
        for rida in range(len(tabel)):
            summa += tabel[rida][veerg]
        summad.append(summa)
    return summad


tabel = [
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
]
print(veergude_summad(tabel))

# Rohkem ridu kui veerge
tabel2 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
print(veergude_summad(tabel2))