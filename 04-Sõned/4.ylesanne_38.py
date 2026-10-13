parool = input("Sisesta parool: ")

punktid = 0
puudused = []

if len(parool) >= 8:
    punktid += 1
else:
    puudused.append("Parool on lühem kui 8 tähemärki.")

if any(m.isupper() for m in parool):
    punktid += 1
else:
    puudused.append("Puudub suurtäht.")

if any(m.islower() for m in parool):
    punktid += 1
else:
    puudused.append("Puudub väiketäht.")

if any(m.isdigit() for m in parool):
    punktid += 1
else:
    puudused.append("Puudub number.")

if any(not m.isalnum() and not m.isspace() for m in parool):
    punktid += 1
else:
    puudused.append("Puudub erimärk.")

if punktid <= 2:
    hinnang = "Nõrk parool"
elif punktid <= 4:
    hinnang = "Keskmine parool"
else:
    hinnang = "Kõik nõuded täidetud"

print()
print(f"Tulemus: {punktid}/5")
print(f"Hinnang: {hinnang}")

if puudused:
    print()
    for puudus in puudused:
        print(puudus)