TAISHAALIKUD = "aeiouõäöü"

lause = input("Sisesta lause: ").lower()

kokku = 0
for taht in lause:
    if taht in TAISHAALIKUD:
        kokku += 1

print()
print(f"Täishäälikuid kokku: {kokku}")
print()

for taht in TAISHAALIKUD:
    arv = lause.count(taht)
    if arv > 0:
        print(f"{taht}: {arv}")