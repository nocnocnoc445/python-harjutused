vanus = int(input("Sisesta vanus: "))

if vanus >= 18:
    print("Oled täisealine.")
elif vanus >= 1 and vanus <= 17:
    print("Oled alaealine.")
elif vanus == 0:
    print("väike beebi oled.")
elif vanus < 0:
    print("mis sa jäppad, sa pole isegi sündinud.")