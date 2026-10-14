temperatuurid = [12, 18, 25, 9, 31, 22, 16, 28, 7]

soojad = []
jahedad = []

for temp in temperatuurid:
    if temp >= 20:
        soojad.append(temp)
    else:
        jahedad.append(temp)

print("Soojad:", soojad)
print("Jahedad:", jahedad)