python = {"Mari", "Jüri", "Kati", "Peeter"}
java = {"Jüri", "Peeter", "Anna", "Toomas"}

molemad = python & java

print("Mõlemat programmeerimiskeelt õpivad:")
for nimi in sorted(molemad):
    print(nimi)
