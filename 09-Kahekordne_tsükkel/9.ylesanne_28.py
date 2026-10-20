tabel = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

summa = 0
elemente = 0

for rida in tabel:
    for element in rida:
        summa += element
        elemente += 1

keskmine = summa / elemente

print("Summa:", summa)
print(f"Keskmine: {keskmine:.2f}")