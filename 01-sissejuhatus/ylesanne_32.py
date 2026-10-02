teepikkus = float(input("Sisesta teepikkus kilomeetrites: ").replace("km", "").strip())
aeg = float(input("Sisesta aeg tundides: ").replace("h", "").strip())
keskmine_kiirus = teepikkus / aeg
print("Keskmine kiirus: " + str(keskmine_kiirus) + " km/h")