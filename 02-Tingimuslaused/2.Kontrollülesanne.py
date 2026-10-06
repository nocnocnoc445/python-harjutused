nimi = input("Nimi: ")
punktid = int(input("Punktisumma: "))
puudumised = int(input("Puudumiste arv: "))
esitatud = input("Kas kõik tööd on esitatud (jah/ei): ").strip().lower()

print()

if punktid < 0 or punktid > 100 or puudumised < 0:
    print("Vigased andmed. Punktisumma peab olema 0–100 ja puudumiste arv ei tohi olla negatiivne.")
else:
    if punktid >= 90:
        hinne = 5
    elif punktid >= 75:
        hinne = 4
    elif punktid >= 50:
        hinne = 3
    elif punktid >= 20:
        hinne = 2
    else:
        hinne = 1

    print("Õpilane:", nimi)
    print("Hinne:", hinne)

    if esitatud == "jah":
        print("Kõik tööd on esitatud.")
    else:
        print("Kõik tööd ei ole esitatud.")

    if puudumised > 10:
        print("Hoiatus: liiga palju puudumisi.")
    else:
        print("Puudumiste arv on lubatud.")

    if hinne >= 3 and puudumised <= 10 and esitatud == "jah":
        print("Aine on läbitud.")
    else:
        print("Aine ei ole läbitud.")