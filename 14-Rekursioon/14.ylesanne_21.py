def lineaarne_otsing(arvud, otsitav, indeks=0):
    if indeks == len(arvud):
        return -1
    if arvud[indeks] == otsitav:
        return indeks
    return lineaarne_otsing(arvud, otsitav, indeks + 1)


print("lineaarne_otsing([4, 7, 2, 9], 2) =", lineaarne_otsing([4, 7, 2, 9], 2))
print("lineaarne_otsing([4, 7, 2, 9], 5) =", lineaarne_otsing([4, 7, 2, 9], 5))
print("lineaarne_otsing([], 3) =", lineaarne_otsing([], 3))
