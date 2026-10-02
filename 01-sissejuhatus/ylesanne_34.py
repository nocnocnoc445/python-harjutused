vat_rate = 0.24  # käibemaksumäär 24%

hind = float(input("Sisesta hind ilma käibemaksuta: ").replace("€", "").strip())

kaibemaks = hind * vat_rate
hind_kmga = hind + kaibemaks

print("Käibemaks: " + str(round(kaibemaks, 2)) + " €")
print("Hind koos käibemaksuga: " + str(round(hind_kmga, 2)) + " €")