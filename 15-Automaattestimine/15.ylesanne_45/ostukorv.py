def kontrolli_toodet(nimi, andmed):
    hind = andmed["hind"]
    kogus = andmed["kogus"]

    # bool on Pythonis int-i alamtüüp, seega välistatakse see eraldi
    if isinstance(hind, bool) or not isinstance(hind, (int, float)):
        raise ValueError(f"Toote {nimi} hind peab olema arv.")
    if isinstance(kogus, bool) or not isinstance(kogus, int):
        raise ValueError(f"Toote {nimi} kogus peab olema täisarv.")
    if hind < 0:
        raise ValueError(f"Toote {nimi} hind ei tohi olla negatiivne.")
    if kogus < 0:
        raise ValueError(f"Toote {nimi} kogus ei tohi olla negatiivne.")


def kontrolli_ostukorvi(ostukorv):
    for nimi, andmed in ostukorv.items():
        kontrolli_toodet(nimi, andmed)


def arvuta_summa(ostukorv):
    kontrolli_ostukorvi(ostukorv)
    summa = 0
    for andmed in ostukorv.values():
        summa += andmed["hind"] * andmed["kogus"]
    return round(summa, 2)


def leia_kalleim(ostukorv):
    kontrolli_ostukorvi(ostukorv)
    if not ostukorv:
        return None
    # suurim ühikuhind, võrdse hinna korral tähestikus esimene nimi
    return min(ostukorv, key=lambda nimi: (-ostukorv[nimi]["hind"], nimi))


def toodete_arv(ostukorv):
    kontrolli_ostukorvi(ostukorv)
    kokku = 0
    for andmed in ostukorv.values():
        kokku += andmed["kogus"]
    return kokku


def rakenda_soodustus(summa, protsent):
    if summa < 0:
        raise ValueError("Summa ei tohi olla negatiivne.")
    if protsent < 0 or protsent > 100:
        raise ValueError("Soodustus peab olema vahemikus 0–100%.")
    return round(summa * (100 - protsent) / 100, 2)


def eemalda_toode(ostukorv, nimi):
    uus = {}
    for toode, andmed in ostukorv.items():
        if toode != nimi:
            uus[toode] = dict(andmed)
    return uus
