import time


def fibonacci_rekursiivne(n):
    if n < 2:
        return n
    return fibonacci_rekursiivne(n - 1) + fibonacci_rekursiivne(n - 2)


def fibonacci_iteratiivne(n):
    eelmine, praegune = 0, 1
    for _ in range(n):
        eelmine, praegune = praegune, eelmine + praegune
    return eelmine


print("fibonacci_rekursiivne(7) =", fibonacci_rekursiivne(7))
print("fibonacci_iteratiivne(7) =", fibonacci_iteratiivne(7))
print()

for n in [10, 20, 30]:
    algus = time.perf_counter()
    tulemus = fibonacci_rekursiivne(n)
    aeg_rek = time.perf_counter() - algus

    algus = time.perf_counter()
    fibonacci_iteratiivne(n)
    aeg_it = time.perf_counter() - algus

    print(f"n = {n}: F(n) = {tulemus:>6} | rekursiivne {aeg_rek:.6f} s | iteratiivne {aeg_it:.6f} s")

# Lihtne rekursiivne lahendus arvutab samu väärtusi uuesti ja uuesti.
# Näiteks F(5) jaoks arvutatakse F(4) ja F(3), aga F(4) arvutab omakorda
# jälle F(3). Väljakutsete arv kasvab iga n-iga ligikaudu 1,6 korda,
# n = 30 korral tehakse juba üle 2,6 miljoni väljakutse.
# Iteratiivne lahendus arvutab iga liikme ainult ühe korra (n sammu).
