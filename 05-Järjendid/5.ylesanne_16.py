arv = int(input("Sisesta arv: "))

while arv < 1 or arv > 10:
    arv = int(input("Arv peab olema vahemikus 1-10. Sisesta uuesti: "))

print()
for i in range(1, 11):
    print(f"{arv} * {i} = {arv * i}")