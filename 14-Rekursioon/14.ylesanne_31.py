def summa_saba(n, tulemus=0):
    if n <= 0:
        return tulemus
    return summa_saba(n - 1, tulemus + n)


print("summa_saba(5) =", summa_saba(5))
print("summa_saba(10) =", summa_saba(10))
print("summa_saba(0) =", summa_saba(0))
