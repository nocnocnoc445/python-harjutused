arvud = set()

while True:
    try:
        arv = int(input("Sisesta täisarv (0 lõpetab): "))
    except ValueError:
        print("See ei ole täisarv.")
        continue
    if arv == 0:
        break
    arvud.add(arv)

print()
if arvud:
    print("Erinevad arvud:", sorted(arvud))
    print("Erinevaid arve:", len(arvud))
    print("Väikseim arv:", min(arvud))
    print("Suurim arv:", max(arvud))
else:
    print("Ühtegi arvu peale nulli ei sisestatud.")
