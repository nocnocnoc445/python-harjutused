TAISHAALIKUD = "aeiouõäöü"

tekst = input("Sisesta tekst: ")

taishaalikuid = 0
numbreid = 0
for mark in tekst:
    if mark.lower() in TAISHAALIKUD:
        taishaalikuid += 1
    if mark.isdigit():
        numbreid += 1

print()
print("Tähemärke kokku:", len(tekst))
print("Tähemärke ilma tühikuteta:", len(tekst.replace(" ", "")))
print("Sõnu:", len(tekst.split()))
print("Täishäälikuid:", taishaalikuid)
print("Numbreid:", numbreid)