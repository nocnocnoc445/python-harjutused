tulemused = (
    ("Mari", 85),
    ("Jüri", 72),
    ("Anna", 95),
    ("Karl", 68),
    ("Liisa", 91)
)

# sorteerimisvõtmeks on iga enniku teine element ehk punktisumma
sorteeritud = tuple(sorted(tulemused, key=lambda tulemus: tulemus[1], reverse=True))

print("Sorteeritud tulemused:", sorteeritud)
print()
print("Kolm parimat:")
for i in range(3):
    nimi, punktid = sorteeritud[i]
    print(f"{i + 1}. {nimi} - {punktid} punkti")
