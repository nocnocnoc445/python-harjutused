summa = 1000
aastaid = 0

while summa < 2000:
    summa = summa * 1.05
    aastaid = aastaid + 1
    print(f"{aastaid}. aasta: {summa:.2f} eurot")

print(f"Kontol on vähemalt 2000 eurot {aastaid} aasta pärast.")