def tervita(nimi):
    return "Tere, " + nimi + "!"


assert tervita("Mari") == "Tere, Mari!"
assert tervita("") == "Tere, !"
assert tervita("Jüri") == "Tere, Jüri!"
assert tervita("Õie") == "Tere, Õie!"

print("Kõik testid läbisid.")
