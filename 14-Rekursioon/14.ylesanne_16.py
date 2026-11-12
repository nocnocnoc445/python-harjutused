def jarjendi_summa(arvud):
    if not arvud:
        return 0
    return arvud[0] + jarjendi_summa(arvud[1:])


for arvud in [[2, 4, 6], [10], []]:
    print(f"jarjendi_summa({arvud}) = {jarjendi_summa(arvud)}")
