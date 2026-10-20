maatriks = [
    [4, 2, 7],
    [1, 9, 3],
    [6, 5, 8]
]

diagonaal = []
summa = 0

for i in range(len(maatriks)):
    for j in range(len(maatriks[i])):
        if i == j:
            diagonaal.append(maatriks[i][j])
            summa += maatriks[i][j]

tekst = ""
for arv in diagonaal:
    tekst += str(arv) + " "

print("Peadiagonaal:", tekst.strip())
print("Summa:", summa)