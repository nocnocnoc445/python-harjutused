def arvu_tyyp(arv):
    if arv > 0:
        return "Positiivne"
    elif arv < 0:
        return "Negatiivne"
    else:
        return "Null"

print(arvu_tyyp(15))
print(arvu_tyyp(-8))
print(arvu_tyyp(0))