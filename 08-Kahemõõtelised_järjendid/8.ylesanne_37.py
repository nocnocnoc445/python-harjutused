import random


def loo_maatriks(ridu, veerge, algus, lopp):
    maatriks = []
    for i in range(ridu):
        rida = []
        for j in range(veerge):
            rida.append(random.randint(algus, lopp))
        maatriks.append(rida)
    return maatriks


def leia_suurim(maatriks):
    suurim = maatriks[0][0]
    suurim_rida = 0
    suurim_veerg = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if maatriks[i][j] > suurim:
                suurim = maatriks[i][j]
                suurim_rida = i
                suurim_veerg = j
    return suurim, suurim_rida, suurim_veerg


def kuva(maatriks):
    for rida in maatriks:
        tekst = ""
        for arv in rida:
            tekst += f"{arv:4}"
        print(tekst)


m = loo_maatriks(4, 5, 1, 100)
kuva(m)

vaartus, rida, veerg = leia_suurim(m)
print(f"Suurim element: {vaartus} (rida {rida}, veerg {veerg})")