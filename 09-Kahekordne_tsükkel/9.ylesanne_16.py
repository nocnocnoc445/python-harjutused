temperatuurid = [18, 21, 25, 19, 28, 30, 22]

piir = float(input("Sisesta temperatuuripiir: "))

leitud = []
for t in temperatuurid:
    if t > piir:
        leitud.append(t)

if len(leitud) > 0:
    print("Piirist kõrgemad temperatuurid:", leitud)
else:
    print("Ükski temperatuur ei ole piirist kõrgem.")