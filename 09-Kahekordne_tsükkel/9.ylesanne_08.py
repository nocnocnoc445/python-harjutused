arvud = [12, 18, 7, 25, 14, 9]

# Esimene lahendus - ilma sum() funktsioonita
summa = 0
for arv in arvud:
    summa += arv


keskmine = summa / len(arvud)

print("Summa:", summa)
print(f"Keskmine: {keskmine:.2f}")

# Teine lahendus - sum() funktsiooniga
print()
print("Summa (sum):", sum(arvud))
print(f"Keskmine (sum): {sum(arvud) / len(arvud):.2f}")