email = input("Sisesta e-post: ")

if " " in email:
    print("Viga: aadressis ei tohi olla tühikuid.")
elif email.count("@") != 1:
    print("Viga: aadressis peab olema täpselt üks @ märk.")
else:
    nimi, domeen = email.split("@")

    if len(nimi) < 1:
        print("Viga: @ ees peab olema vähemalt üks tähemärk.")
    elif "." not in domeen:
        print("Viga: domeeniosas peab olema punkt.")
    elif domeen.startswith(".") or domeen.endswith("."):
        print("Viga: domeeniosa ei tohi alata ega lõppeda punktiga.")
    else:
        print("Aadressi kuju on sobiv.")