arvud = [4, 7, 4, 9, 2, 7, 5, 9, 1]
hulk = set(arvud)

print("Algne järjend:", arvud)
print("Hulk:", hulk)
print("Elemente järjendis:", len(arvud))
print("Erinevaid väärtusi hulgas:", len(hulk))

# Hulgas saab iga väärtus esineda ainult üks kord. Järjendis korduvad
# arvud 4, 7 ja 9, seega jääb neist hulka alles ainult üks koopia ja
# elementide arv väheneb.
