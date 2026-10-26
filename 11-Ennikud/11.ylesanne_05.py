puuviljad = ("õun", "pirn", "apelsin", "mandariin", "ploom", "kirss", "viinamari", "kiivi")

print("Puuviljade arv:", len(puuviljad))

for otsitav in ("õun", "banaan"):
    if otsitav in puuviljad:
        print(f'Ennik sisaldab sõna "{otsitav}".')
    else:
        print(f'Ennik ei sisalda sõna "{otsitav}".')
