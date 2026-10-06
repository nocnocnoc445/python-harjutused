vanus = int(input("Vanus: "))
opilane = input("Kas oled õpilane (jah/ei): ").strip().lower()

if vanus < 7:
    hind = 0
elif vanus <= 17:
    hind = 5
elif vanus >= 65:
    hind = 6
elif opilane == "jah":
    hind = 8
else:
    hind = 12

if hind == 0:
    print("Pilet on tasuta.")
else:
    print(f"Pileti hind on {hind} €.")