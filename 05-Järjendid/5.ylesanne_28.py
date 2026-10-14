arvude_arv = 0
summa = 0

with open("arvud.txt", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida != "":
            summa += int(rida)
            arvude_arv += 1

print("Arvude arv:", arvude_arv)
print("Arvude summa:", summa)