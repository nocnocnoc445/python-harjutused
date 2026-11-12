paaris = set()

for arv in range(1, 101):
    if arv % 2 == 0:
        paaris.add(arv)

print("Elementide arv:", len(paaris))
print("Kümme esimest:", sorted(paaris)[:10])
