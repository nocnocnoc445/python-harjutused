import math


def kaugus(punkt):
    x, y = punkt
    return math.sqrt(x ** 2 + y ** 2)


punktid = (
    (3, 4),
    (6, 8),
    (1, 2),
    (9, 12),
    (5, 5)
)

kaugeim = punktid[0]
for punkt in punktid:
    print(f"Punkt {punkt}: kaugus {kaugus(punkt):.2f}")
    if kaugus(punkt) > kaugus(kaugeim):
        kaugeim = punkt

x, y = kaugeim
print()
print(f"Kõige kaugem punkt: ({x}, {y}), kaugus alguspunktist {kaugus(kaugeim):.2f}")
