def raha_eurodes(kastid, hind_sentides):
    return round(kastid * 5 *(hind_sentides / 100), 1)


failinimi = input("Sisesta failinimi: ")
hind = int(input("sisestage kilo hind sendides: "))

fail = open(failinimi, "r", encoding="UTF-8")
kokku = 0
paev = 1
for rida in fail:
    rida = rida.strip()
    if rida == "":
        continue
    eurod = raha_eurodes(int(rida), hind)
    print(str(paev) + ". päeval sai " + str(eurod) + " eurot.")
    kokku += eurod
    paev += 1
fail.close()

print("Kokku sai: " + str(kokku) + " eurot.")
