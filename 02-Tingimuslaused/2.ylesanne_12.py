temperatuur = float(input("Sisesta temperatuur: "))

if temperatuur < 0:
    print("Külmub")
elif temperatuur <= 15:
    print("Jahe")
elif temperatuur <= 25:
    print("Soe")
else:
    print("Palav")