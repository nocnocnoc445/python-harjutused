hinded = {
    "Mari": 5,
    "Jüri": 3,
    "Kati": 4,
    "Andres": 5,
    "Liis": 4,
    "Martin": 2,
    "Laura": 5,
    "Rasmus": 4
}

vaartused = hinded.values()

summa = sum(vaartused)
keskmine = summa / len(vaartused)

print("Hinnete summa:", summa)
print(f"Keskmine hinne: {keskmine:.2f}")
print("Kõrgeim hinne:", max(vaartused))
print("Madalaim hinne:", min(vaartused))