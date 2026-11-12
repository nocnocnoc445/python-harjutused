def summa_iteratiivne(n):
    tulemus = 0
    for i in range(1, n + 1):
        tulemus += i
    return tulemus


def summa_rekursiivne(n):
    if n <= 0:
        return 0
    return n + summa_rekursiivne(n - 1)


for n in [10, 100, 500]:
    iteratiivne = summa_iteratiivne(n)
    rekursiivne = summa_rekursiivne(n)
    print(f"n = {n:>3}: iteratiivne = {iteratiivne:>6}, rekursiivne = {rekursiivne:>6}, "
          f"võrdsed: {iteratiivne == rekursiivne}")

# Mõlemad funktsioonid annavad sama tulemuse.
# Rekursiivne lahendus on lühem ja sarnaneb valemiga S(n) = n + S(n - 1).
# Minu arvates on iteratiivne lahendus siiski lihtsam, sest seda on kergem
# samm-sammult jälgida ja see töötab ka väga suure n korral, kus rekursioon
# jõuaks Pythoni rekursioonipiirini.
