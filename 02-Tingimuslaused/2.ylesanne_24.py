aasta = int(input("Sisesta aasta: "))

if aasta % 400 == 0:
    print("On liigaasta.")
elif aasta % 100 == 0:
    print("Ei ole liigaasta.")
elif aasta % 4 == 0:
    print("On liigaasta.")
else:
    print("Ei ole liigaasta.")