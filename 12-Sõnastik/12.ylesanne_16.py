lause = input("Sisesta lause: ")

sagedus = {}
for mark in lause.lower():
    if mark.isalpha():   # tühikud ja kirjavahemärgid jäävad välja
        sagedus[mark] = sagedus.get(mark, 0) + 1

for taht in sorted(sagedus):
    print(f"{taht}: {sagedus[taht]}")