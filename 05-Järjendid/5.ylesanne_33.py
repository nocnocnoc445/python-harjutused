hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]

koguarv = len(hinded)
keskmine = sum(hinded) / koguarv

suurim_esinemine = 0
for hinne in range(1, 6):
    if hinded.count(hinne) > suurim_esinemine:
        suurim_esinemine = hinded.count(hinne)

sagedasemad = []
for hinne in range(1, 6):
    if hinded.count(hinne) == suurim_esinemine:
        sagedasemad.append(hinne)

positiivseid = 0
mitterahuldavaid = 0
for hinne in hinded:
    if hinne >= 3:
        positiivseid += 1
    else:
        mitterahuldavaid += 1

print("Hinnete koguarv:", koguarv)
print(f"Keskmine hinne: {keskmine:.2f}")
print("Kõige sagedasem hinne:", sagedasemad, f"({suurim_esinemine} korda)")
print("Positiivseid hindeid:", positiivseid)
print("Mitterahuldavaid hindeid:", mitterahuldavaid)
print()

for hinne in range(1, 6):
    print(f"Hinne {hinne}: {hinded.count(hinne)} korda")

print()

for hinne in range(1, 6):
    print(f"Hinne {hinne}: {'*' * hinded.count(hinne)}")