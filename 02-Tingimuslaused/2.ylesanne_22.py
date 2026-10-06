kasutajanimi = input("Kasutajanimi: ")

if kasutajanimi == "admin":
    parool = input("Parool: ")
    if parool == "python123":
        print("Tere tulemast!")
    else:
        print("Vale parool.")
else:
    print("Tundmatu kasutaja.")