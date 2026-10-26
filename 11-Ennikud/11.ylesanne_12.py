arvud = (4, 7, 12, 15, 18, 21, 24, 29)

paaris = 0
paaritud = 0
for arv in arvud:
    if arv % 2 == 0:
        paaris += 1
    else:
        paaritud += 1

print("Paarisarve:", paaris)
print("Paarituid arve:", paaritud)
