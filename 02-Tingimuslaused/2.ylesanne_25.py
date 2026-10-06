esimene = float(input("Esimene arv: "))
tehe = input("Tehe: ")
teine = float(input("Teine arv: "))

if tehe == "+":
    tulemus = esimene + teine
elif tehe == "-":
    tulemus = esimene - teine
elif tehe == "*":
    tulemus = esimene * teine
elif tehe == "/":
    if teine == 0:
        tulemus = None
        print("Nulliga ei saa jagada.")
    else:
        tulemus = esimene / teine
else:
    tulemus = None
    print("Tundmatu tehe.")

if tulemus is not None:
    if tulemus.is_integer():
        tulemus = int(tulemus)
    print("Tulemus:", tulemus)