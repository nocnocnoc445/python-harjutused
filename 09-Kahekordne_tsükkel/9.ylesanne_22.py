def loenda_paaritud(arvud):
    loendur = 0
    for arv in arvud:
        if arv % 2 != 0:
            loendur += 1
    return loendur


print(loenda_paaritud([1, 2, 3, 4, 5]))
print(loenda_paaritud([7, 9, 11, 13]))
print(loenda_paaritud([2, 4, 6, 8]))