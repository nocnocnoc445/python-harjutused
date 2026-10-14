muugid = [125.50, 210.00, 98.75, 340.20, 185.40, 420.00, 275.90]
paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]

for i in range(len(muugid)):
    print(f"{paevad[i]}: {muugid[i]:.2f} €")

kogumuuk = sum(muugid)
keskmine = kogumuuk / len(muugid)

suurima_indeks = 0
for i in range(len(muugid)):
    if muugid[i] > muugid[suurima_indeks]:
        suurima_indeks = i

ule_200 = 0
for muuk in muugid:
    if muuk > 200:
        ule_200 += 1

print()
print(f"Nädala kogumüük: {kogumuuk:.2f} €")
print(f"Keskmine päevamüük: {keskmine:.2f} €")
print(f"Suurim müük: {paevad[suurima_indeks]} ({muugid[suurima_indeks]:.2f} €)")
print("Päevi, kus müük ületas 200 €:", ule_200)