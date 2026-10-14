def arvude_summa(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(arvude_summa(5))
print(arvude_summa(10))