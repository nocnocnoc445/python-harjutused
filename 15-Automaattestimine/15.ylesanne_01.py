def ruut(arv):
    return arv * arv


assert ruut(4) == 16
assert ruut(-3) == 9
assert ruut(0) == 0
assert ruut(1) == 1
assert ruut(1.5) == 2.25
assert ruut(10) == 100

print("Kõik testid läbisid.")
