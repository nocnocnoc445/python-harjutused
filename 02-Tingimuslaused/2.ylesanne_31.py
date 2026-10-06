cpu = float(input("CPU kasutus (%): "))
malu = float(input("Mälu kasutus (%): "))
ketas = float(input("Ketta kasutus (%): "))

if cpu > 90 or malu > 90 or ketas > 90:
    olek = "KRIITILINE"
elif cpu > 75 or malu > 75 or ketas > 75:
    olek = "HOIATUS"
else:
    olek = "OK"

print()
print("Serveri olek:", olek)