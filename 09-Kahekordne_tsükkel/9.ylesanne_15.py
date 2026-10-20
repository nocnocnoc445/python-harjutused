punktid = [95, 82, 74, 61, 48, 100, 89]
hinded = []

for p in punktid:
    if p >= 90:
        hinded.append("A")
    elif p >= 80:
        hinded.append("B")
    elif p >= 70:
        hinded.append("C")
    elif p >= 60:
        hinded.append("D")
    else:
        hinded.append("F")

a_hindeid = 0
for i in range(len(punktid)):
    print(f"Õppija {i + 1}: {punktid[i]} punkti – hinne {hinded[i]}")
    if hinded[i] == "A":
        a_hindeid += 1

print()
print("Hinded:", hinded)
print("A said:", a_hindeid, "õppijat")