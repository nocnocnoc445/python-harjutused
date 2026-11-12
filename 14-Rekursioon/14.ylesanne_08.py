def aste(a, n):
    if n == 0:
        return 1
    return a * aste(a, n - 1)


print("aste(2, 5) =", aste(2, 5))
print("aste(3, 3) =", aste(3, 3))
print("aste(5, 0) =", aste(5, 0))
