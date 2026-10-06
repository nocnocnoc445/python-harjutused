a = float(input("Esimene külg: "))
b = float(input("Teine külg: "))
c = float(input("Kolmas külg: "))

if a + b > c and a + c > b and b + c > a:
    print("Kolmnurk on võimalik.")
else:
    print("Kolmnurk ei ole võimalik.")