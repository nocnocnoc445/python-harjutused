ladu = {
    "Monitor": 12,
    "Klaviatuur": 25,
    "Hiir": 40,
    "Sülearvuti": 8,
    "Printer": 5,
    "Veebikaamera": 15,
    "Kõrvaklapid": 22
}

toode = input("Sisesta tootenimi: ").strip().capitalize()

kogus = input("Sisesta saabunud kogus: ").strip()
while not kogus.isdigit():
    kogus = input("Kogus peab olema täisarv. Sisesta uuesti: ").strip()
kogus = int(kogus)

if toode in ladu:
    ladu[toode] += kogus
    print(f"{toode} kogust suurendati, uus kogus: {ladu[toode]}")
else:
    ladu[toode] = kogus
    print(f"Uus toode {toode} lisati, kogus: {kogus}")

print("Laoseis:", ladu)