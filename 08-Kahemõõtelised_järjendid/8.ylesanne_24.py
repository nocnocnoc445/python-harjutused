maatriks = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

for veerg in range(len(maatriks[0])):
    summa = 0
    for rida in range(len(maatriks)):
        summa += maatriks[rida][veerg]
    print(f"{veerg + 1}. veerg: {summa}")