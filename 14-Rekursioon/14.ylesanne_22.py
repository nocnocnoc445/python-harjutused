def otsi_vahemikus(arvud, otsitav, algus, lopp):
    if algus > lopp:
        return -1

    kesk = (algus + lopp) // 2
    if arvud[kesk] == otsitav:
        return kesk
    if arvud[kesk] < otsitav:
        return otsi_vahemikus(arvud, otsitav, kesk + 1, lopp)
    return otsi_vahemikus(arvud, otsitav, algus, kesk - 1)


def binaarne_otsing(arvud, otsitav):
    return otsi_vahemikus(arvud, otsitav, 0, len(arvud) - 1)


arvud = [1, 3, 5, 7, 9]
print(f"binaarne_otsing({arvud}, 7) =", binaarne_otsing(arvud, 7))
print(f"binaarne_otsing({arvud}, 4) =", binaarne_otsing(arvud, 4))
print(f"binaarne_otsing({arvud}, 1) =", binaarne_otsing(arvud, 1))
print("binaarne_otsing([], 3) =", binaarne_otsing([], 3))
