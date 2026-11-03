hinnad1 = {
    "Piim": 1.25,
    "Leib": 1.80,
    "Juust": 4.50
}

hinnad2 = hinnad1.copy()
hinnad2["Leib"] = 2.10

print("hinnad1:", hinnad1)
print("hinnad2:", hinnad2)
print("Sama objekt:", hinnad1 is hinnad2)

if hinnad1["Leib"] == 1.80:
    print("Algne sõnastik ei muutunud.")
else:
    print("Algne sõnastik muutus.")

# Erinevus ülesandega 26:
# copy() loob uue sõnastiku, kuhu kopeeritakse kõik võtmed ja väärtused.
# hinnad1 ja hinnad2 on nüüd kaks eraldi objekti, seega koopia muutmine
# algset sõnastikku ei mõjuta. Ülesandes 26 viitasid mõlemad nimed samale
# sõnastikule, sellepärast oli muutus nähtav mõlemas.