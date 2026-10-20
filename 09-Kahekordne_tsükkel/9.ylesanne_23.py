def leia_suuremad(arvud, piir):
    tulemus = []
    for arv in arvud:
        if arv > piir:
            tulemus.append(arv)
    return tulemus


arvud = [4, 12, 7, 19, 3]
print("Tulemus:", leia_suuremad(arvud, 10))
print("Algne järjend:", arvud)