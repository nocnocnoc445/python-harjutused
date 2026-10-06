a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
c = int(input("Kolmas arv: "))

if a >= b and a >= c:
    suurim = a
elif b >= a and b >= c:
    suurim = b
else:
    suurim = c

print()
print(f"Suurim arv on {suurim}.")