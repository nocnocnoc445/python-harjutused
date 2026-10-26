opilased = (
    ("Mari", (5, 4, 5, 5)),
    ("Jüri", (3, 4, 3, 4)),
    ("Anna", (5, 5, 5, 4)),
    ("Karl", (2, 3, 4, 3))
)

keskmised = []
print("Õpilaste keskmised hinded:")
for nimi, hinded in opilased:
    keskmine = sum(hinded) / len(hinded)
    keskmised.append((nimi, keskmine))
    print(f"{nimi}: {keskmine:.2f}")

parim = keskmised[0][1]
for nimi, keskmine in keskmised:
    if keskmine > parim:
        parim = keskmine

# võrdse tulemuse korral on parimaid mitu
parimad = []
for nimi, keskmine in keskmised:
    if keskmine == parim:
        parimad.append(nimi)

print()
print(f"Parim keskmine tulemus ({parim:.2f}): {', '.join(parimad)}")

print()
print("Keskmine hinne vähemalt 4.5:")
for nimi, keskmine in keskmised:
    if keskmine >= 4.5:
        print(nimi)
