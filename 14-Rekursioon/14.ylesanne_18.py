def paarisarvude_arv(arvud):
    if not arvud:
        return 0
    if arvud[0] % 2 == 0:
        return 1 + paarisarvude_arv(arvud[1:])
    return paarisarvude_arv(arvud[1:])


for arvud in [[1, 2, 3, 4, 6], [1, 3, 5], []]:
    print(f"paarisarvude_arv({arvud}) = {paarisarvude_arv(arvud)}")
