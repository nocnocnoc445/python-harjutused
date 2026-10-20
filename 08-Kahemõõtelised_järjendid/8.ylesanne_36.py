a = [[1, 2], [3, 4]]
b = a
c = a[:]

b[0][0] = 99
c[1][1] = 88

print(a)
print(b)
print(c)

# Ennustus: kõik kolm väljastavad [[99, 2], [3, 88]]
#
# Selgitus:
# b = a ei tee koopiat – b ja a on sama järjend, seega b muutmine muudab ka a-d.
# c = a[:] teeb ainult pinnapealse koopia: välimine järjend on uus,
# aga sisemised järjendid on samad objektid mis a-s.
# Seepärast c[1][1] = 88 muudab sisemist järjendit, mida jagavad a, b ja c.

print()
print("Sõltumatu koopia:")

a = [[1, 2], [3, 4]]
c = []
for rida in a:
    c.append(rida[:])  # iga sisemine järjend kopeeritakse eraldi

c[1][1] = 88

print("a:", a)
print("c:", c)