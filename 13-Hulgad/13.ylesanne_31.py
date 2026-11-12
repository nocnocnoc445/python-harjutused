opilased = {
    "Mari", "Jüri", "Anna", "Peeter",
    "Kati", "Toomas", "Karl", "Liis"
}
kohal = {"Mari", "Anna", "Kati", "Karl", "Liis"}

puudu = opilased - kohal
osakaal = len(kohal) / len(opilased) * 100

print("Kohalolijad:", ", ".join(sorted(kohal)))
print("Puudujad:", ", ".join(sorted(puudu)))
print("Kohalolijate arv:", len(kohal))
print("Puudujate arv:", len(puudu))
print(f"Kohalolijate osakaal: {osakaal:.1f}%")
