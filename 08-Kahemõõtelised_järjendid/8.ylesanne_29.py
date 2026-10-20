temperatuurid = [
    [12, 14, 15, 13, 16, 17, 14],
    [10, 11, 13, 12, 14, 15, 13],
    [8, 9, 11, 10, 12, 13, 11]
]
linnad = ["Tartu", "Tallinn", "Pärnu"]

korgeim = temperatuurid[0][0]
korgeima_linn = linnad[0]
soojem_linn = ""
soojem_keskmine = None

for i in range(len(temperatuurid)):
    summa = 0
    for temp in temperatuurid[i]:
        summa += temp
        if temp > korgeim:
            korgeim = temp
            korgeima_linn = linnad[i]
    keskmine = summa / len(temperatuurid[i])
    print(f"{linnad[i]}: keskmine {keskmine:.2f} °C")

    if soojem_keskmine is None or keskmine > soojem_keskmine:
        soojem_keskmine = keskmine
        soojem_linn = linnad[i]

print(f"Nädala kõrgeim temperatuur: {korgeim} °C ({korgeima_linn})")
print(f"Kõige soojem nädal: {soojem_linn} ({soojem_keskmine:.2f} °C)")