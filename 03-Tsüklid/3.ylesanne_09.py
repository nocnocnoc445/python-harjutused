i = 1
summa = 0

while i <= 5:
    summa = summa + i
    i = i + 1

print(summa)

# Ennustatud tulemus: 15
#
# Muutujad iga tsükli läbimise järel:
# 1. läbimine: summa = 1,  i = 2
# 2. läbimine: summa = 3,  i = 3
# 3. läbimine: summa = 6,  i = 4
# 4. läbimine: summa = 10, i = 5
# 5. läbimine: summa = 15, i = 6
#
# Kui i = 6, siis tingimus 6 <= 5 on väär ja tsükkel lõpeb.