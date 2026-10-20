andmed = [
    [1, 2, 3],
    [4, 5],
    [],
    [6, 7, 8, 9],
    [10]
]

koguarv = 0
pikim_indeks = 0

for i in range(len(andmed)):
    pikkus = len(andmed[i])
    print(f"Indeks {i}: pikkus {pikkus}")
    koguarv += pikkus
    if pikkus > len(andmed[pikim_indeks]):
        pikim_indeks = i

print("Elemente kokku:", koguarv)
print("Kõige pikema sisemise järjendi indeks:", pikim_indeks)