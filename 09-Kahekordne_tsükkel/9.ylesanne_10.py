arvud = [4, 7, 12, 15, 20, 23, 28, 31]

paaris = []
paaritud = []

for arv in arvud:
    if arv % 2 == 0:
        paaris.append(arv)
    else:
        paaritud.append(arv)


print("Paaris:", paaris, "- elemente", len(paaris))
print("Paaritud:", paaritud, "- elemente", len(paaritud))