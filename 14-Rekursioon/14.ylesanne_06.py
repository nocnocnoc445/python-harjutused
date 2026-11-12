def summa(n):
    if n <= 0:
        return 0
    return n + summa(n - 1)


print("summa(5) =", summa(5))
print("summa(10) =", summa(10))
print("summa(0) =", summa(0))
