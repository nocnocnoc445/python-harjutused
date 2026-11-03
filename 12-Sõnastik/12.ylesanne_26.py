hinnad1 = {
    "Piim": 1.25,
    "Leib": 1.80,
    "Juust": 4.50
}

hinnad2 = hinnad1
hinnad2["Leib"] = 2.10

print("hinnad1:", hinnad1)
print("hinnad2:", hinnad2)
print("Sama objekt:", hinnad1 is hinnad2)

# Selgitus:
# hinnad2 = hinnad1 ei loo uut sõnastikku. See annab samale sõnastikule
# lihtsalt teise nime. Mõlemad muutujad viitavad mälus samale objektile,
# seega muutus hinnad2 kaudu on nähtav ka hinnad1 kaudu.