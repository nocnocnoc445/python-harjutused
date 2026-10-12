oige_parool = "python123"
katseid = 0
lubatud = False

while katseid < 3:
    parool = input("Sisesta parool: ")
    katseid = katseid + 1

    if parool == oige_parool:
        lubatud = True
        break
    else:
        print("Vale parool!")
        print()

if lubatud:
    print("Ligipääs lubatud!")
else:
    print("Ligipääs blokeeritud!")