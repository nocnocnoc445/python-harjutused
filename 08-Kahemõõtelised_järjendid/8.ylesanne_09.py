tabel = [
    [3, 6, 9],
    [2, 4, 8],
    [5, 10, 15]
]

# Ennustused:
# tabel[0][2] = 9
# tabel[2][0] = 5
# tabel[-1][-1] = 15
# tabel[1] = [2, 4, 8]
# len(tabel) = 3
# len(tabel[0]) = 3
#
# tabel[1] on terve teine rida (järjed[2, 4, 8]),
# tabel[1][0] on selle rea esimene element (üks arv: 2),

print(tabel[0][2])
print(tabel[2][0])
print(tabel[-1][-1])
print(tabel[1])
print(len(tabel))
print(len(tabel[0]))