puuviljad = ["õun", "pirn", "banaan", "õun", "ploom"]
print("Algne:", puuviljad)

puuviljad.append("apelsin")
print("Lisatud apelsin:", puuviljad)

puuviljad.insert(1, "kiivi") # teine koht = indeks 1
print("Lisatud kiivi:", puuviljad)

indeks = puuviljad.index("banaan")
puuviljad[indeks] = "mango"
print("Banaan -> mango:", puuviljad)

puuviljad.remove("õun") # eemaldab esimese õuna
print("Eemaldatud esimene õun:", puuviljad)

print("'õun' esineb veel:", puuviljad.count("õun"), "korda")