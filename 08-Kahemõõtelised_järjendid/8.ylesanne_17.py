andmed = [
    [12, 5, 19],
    [8, 23, 4],
    [17, 9, 11]
]

kõige_suurem = andmed[0][0]

for i in range(len(andmed)):
    rea_suurim = andmed[i][0]
    for arv in andmed[i]:
        if arv > rea_suurim:
            rea_suurim = arv
    print(f"{i + 1}. rea suurim element: {rea_suurim}")
    if rea_suurim > kõige_suurem:
        kõige_suurem = rea_suurim

print("Kogu andmestruktuuri suurim arv:", kõige_suurem)