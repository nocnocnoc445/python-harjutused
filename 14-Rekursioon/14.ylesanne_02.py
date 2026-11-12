def loenda_ules(n):
    if n > 0:
        loenda_ules(n - 1)
    # väljastamine on pärast väljakutset, seega trükitakse arvud alles
    # tagasiteel: kõigepealt 0, siis 1 ja nii edasi kuni n-ni
    print(n)


loenda_ules(4)
