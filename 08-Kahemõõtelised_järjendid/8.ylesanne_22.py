maatriks = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for rida in maatriks:
    tekst = ""
    for arv in rida:
        tekst += str(arv) + " "
    print(tekst.strip())