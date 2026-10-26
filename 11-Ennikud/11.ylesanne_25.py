opilased = (
    ("Mari", 5),
    ("Jüri", 4),
    ("Anna", 3),
    ("Karl", 5)
)

viied = 0
for nimi, hinne in opilased:
    print(f"{nimi}: {hinne}")
    if hinne == 5:
        viied += 1

print()
print("Hinde 5 sai", viied, "õpilast.")
