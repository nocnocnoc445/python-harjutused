vanus = int(input("Sisesta vanus: "))

if vanus < 18 or vanus >= 65:
    print("Pileti hind on 6 eurot.")
else:
    print("Pileti hind on 10 eurot.")