parool = input("Sisesta parool: ")
pikkus = len(parool)

if pikkus < 8:
    print("Parool on liiga lühike.")
elif pikkus <= 11:
    print("Parooli pikkus on sobiv.")
else:
    print("Tegemist on pika parooliga.")