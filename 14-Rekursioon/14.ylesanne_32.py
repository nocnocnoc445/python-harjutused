def faktoriaal_saba(n, tulemus=1):
    if n < 0:
        raise ValueError("Negatiivse arvu faktoriaali ei saa arvutada.")
    if n == 0:
        return tulemus
    return faktoriaal_saba(n - 1, tulemus * n)


# ülesande 7 lahendus võrdluseks
def faktoriaal(n):
    if n < 0:
        raise ValueError("Negatiivse arvu faktoriaali ei saa arvutada.")
    if n == 0:
        return 1
    return n * faktoriaal(n - 1)


print("faktoriaal_saba(5) =", faktoriaal_saba(5))
print("faktoriaal_saba(0) =", faktoriaal_saba(0))
print("faktoriaal(5) =", faktoriaal(5))

# Ülesandes 7 on rida "return n * faktoriaal(n - 1)". Pärast rekursiivset
# väljakutset tuleb veel korrutada n-iga, seega iga väljakutse jääb
# tulemust ootama ja korrutamised tehakse tagasiteel.
# Sabarekursioonis tehakse korrutamine enne väljakutset (tulemus * n) ja
# vahetulemus antakse edasi akumulaatoris. Rekursiivne väljakutse on
# funktsiooni viimane tegevus ja lõpptulemus lihtsalt tagastatakse üles.
