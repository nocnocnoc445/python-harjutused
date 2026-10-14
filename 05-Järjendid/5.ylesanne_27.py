linnade_arv = 0

with open("linnad.txt", encoding="utf-8") as fail:
    for rida in fail:
        linn = rida.strip()
        if linn != "":
            print(linn)
            linnade_arv += 1

print("Linnade arv:", linnade_arv)