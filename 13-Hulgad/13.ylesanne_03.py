sona = input("Sisesta sõna: ").strip().lower()

tahed = set()
for mark in sona:
    if mark.isalpha():
        tahed.add(mark)

print("Erinevad tähed:", sorted(tahed))
print("Erinevaid tähti:", len(tahed))
