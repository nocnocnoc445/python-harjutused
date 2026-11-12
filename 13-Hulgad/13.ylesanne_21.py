a = {3, 6, 9, 12}
b = {12, 9, 6, 3}

print("a:", a)
print("b:", b)
print("Kas hulgad on võrdsed?", a == b)

b.add(15)

print()
print("Pärast arvu 15 lisamist hulka b:")
print("a:", a)
print("b:", b)
print("Kas hulgad on võrdsed?", a == b)

# Hulgal pole järjekorda ega indekseid. Kaks hulka on võrdsed siis, kui
# neis on täpselt samad elemendid, seega elementide järjestus ei loe.
