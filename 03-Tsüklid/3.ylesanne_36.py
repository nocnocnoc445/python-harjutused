i = 1

while i <= 5:
    print(i)
    i = i + 1

# 1. Mis juhtub: algne programm prindib lõputult arvu 1 (lõpmatu tsükkel).
# 2. Vea põhjus: i väärtust tsükli sees ei muudeta, seega i jääb alati 1
#    ja tingimus i <= 5 on alati tõene.
# 3. Parandus: lisasin tsükli sisse rea i = i + 1.