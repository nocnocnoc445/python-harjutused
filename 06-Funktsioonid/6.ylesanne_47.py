def keskmine(punktid):
    summa = 0
    for p in punktid:
        summa += p
    return summa / len(punktid)

def parim_tulemus(punktid):
    parim = punktid[0]
    for p in punktid:
        if p > parim:
            parim = p
    return parim

def norgim_tulemus(punktid):
    norgim = punktid[0]
    for p in punktid:
        if p < norgim:
            norgim = p
    return norgim

def edukate_arv(punktid, piir=50):
    arv = 0
    for p in punktid:
        if p >= piir:
            arv += 1
    return arv

punktid = [78, 45, 92, 67, 34, 100, 56, 81]

print(f"Keskmine: {keskmine(punktid):.2f}")
print("Parim tulemus:", parim_tulemus(punktid))
print("Nõrgim tulemus:", norgim_tulemus(punktid))
print("Vähemalt 50 punkti:", edukate_arv(punktid))
print("Vähemalt 80 punkti:", edukate_arv(punktid, 80))