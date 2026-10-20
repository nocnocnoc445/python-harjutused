def ruutude_summa(arvud):
    summa = 0
    for arv in arvud:
        summa += arv ** 2
    return summa


print(ruutude_summa([2, 3, 4]))