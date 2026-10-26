andmed = ("Mari", 18, "ITA26")

# vanust ei saa muuta, aga saab teha uue enniku: algus + uus vanus + lõpp
uued_andmed = andmed[:1] + (19,) + andmed[2:]

print("Algne ennik:", andmed)
print("Uus ennik:", uued_andmed)
