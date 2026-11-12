nimed = set()

for i in range(5):
    nimi = input(f"Sisesta {i + 1}. õpilase nimi: ").strip().title()
    if nimi in nimed:
        print(f"Nimi {nimi} on juba sisestatud.")
    nimed.add(nimi)

print()
print("Nimed tähestiku järjekorras:")
for nimi in sorted(nimed):
    print(nimi)
print("Erinevaid nimesid:", len(nimed))
