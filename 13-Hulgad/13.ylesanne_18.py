registreeritud = {"Mari", "Jüri", "Kati", "Anna", "Peeter"}
osalenud = {"Mari", "Kati", "Peeter"}

puudujad = registreeritud - osalenud

print("Registreerusid, kuid ei osalenud:", ", ".join(sorted(puudujad)))
print("Puudujate arv:", len(puudujad))
