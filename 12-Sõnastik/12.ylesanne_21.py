def leia_opilane(opilased, nimi):
    return opilased.get(nimi)


opilased = {
    "Mari": 5,
    "Jüri": 3,
    "Kati": 4,
    "Andres": 5
}

print("Mari hinne:", leia_opilane(opilased, "Mari"))
print("Peetri hinne:", leia_opilane(opilased, "Peeter"))