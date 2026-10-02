kilomeetrid = float(input("Sisesta teepikkus kilomeetrites: ").replace("km", "").strip())
kütuse = float(input("Sisesta kütusekulu liitrites: ").replace("l", "").strip())
kütusekulu = kütuse / kilomeetrid * 100
print("Kütusekulu 100 km kohta: " + str(kütusekulu) + " l/100 km")