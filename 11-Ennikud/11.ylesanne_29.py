def loenda_arvud(arvud):
    paaris = 0
    paaritud = 0
    for arv in arvud:
        if arv % 2 == 0:
            paaris += 1
        else:
            paaritud += 1
    return paaris, paaritud


arvud = (3, 8, 11, 14, 20, 27, 31, 42, 55)
paaris, paaritud = loenda_arvud(arvud)

print("Arvud:", arvud)
print("Paarisarve:", paaris)
print("Paarituid arve:", paaritud)
