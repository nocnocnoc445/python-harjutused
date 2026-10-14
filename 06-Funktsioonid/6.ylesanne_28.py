def taishaalikuid(tekst):
    taishaalikud = "aeiouõäöü"
    arv = 0
    for taht in tekst.lower():
        if taht in taishaalikud:
            arv += 1
    return arv

print(taishaalikuid("Programmeerimine"))
print(taishaalikuid("ÕUNAPÜÜ"))
print(taishaalikuid("Tartu"))
print(taishaalikuid(""))