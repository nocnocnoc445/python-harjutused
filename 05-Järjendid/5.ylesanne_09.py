ostukorv = []

for i in range(5):
    toode = input(f"Sisesta {i + 1}. toode: ")
    ostukorv.append(toode)

print("Ostukorv:", ostukorv)
print("Toodete arv:", len(ostukorv))