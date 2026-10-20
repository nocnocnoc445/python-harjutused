maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

maatriks[0][0] = 100   # esimese rea esimene
maatriks[1][-1] = 60   # teise rea viimane
maatriks[2][1] = 80    # kolmanda rea keskmine

for rida in maatriks:
    print(rida)