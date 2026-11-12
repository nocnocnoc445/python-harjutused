taishaalikud = set("aeiouõäöü")

lause = input("Sisesta lause: ").lower()

leitud = set()
for taht in lause:
    if taht in taishaalikud:
        leitud.add(taht)

print("Leitud täishäälikud:", sorted(leitud))
print("Erinevaid täishäälikuid:", len(leitud))
