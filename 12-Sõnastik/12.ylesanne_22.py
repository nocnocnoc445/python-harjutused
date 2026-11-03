def lisa_toode(ladu, nimi, kogus):
    if nimi in ladu:
        ladu[nimi] += kogus
    else:
        ladu[nimi] = kogus


ladu = {
    "Monitor": 12,
    "Hiir": 40,
    "Printer": 5
}

print("Algne ladu:", ladu)

lisa_toode(ladu, "Hiir", 10)        # olemasolev toode
print("Pärast hiirte lisamist:", ladu)

lisa_toode(ladu, "Mikrofon", 7)     # uus toode
print("Pärast mikrofonide lisamist:", ladu)