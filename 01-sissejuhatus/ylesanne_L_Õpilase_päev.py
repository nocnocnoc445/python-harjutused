nimi = input("Nimi: ")
vanus = int(input("Vanus: "))
koolitee_km = float(input("Koolitee: "))
aeg_min = int(input("Aeg minutites: "))

vanus_jargmisel_aastal = vanus + 1
koolitee_m = round(koolitee_km * 1000)
tunnid = aeg_min // 60
minutid = aeg_min % 60
kiirus = koolitee_km / (aeg_min / 60)

print("Tere, " + nimi + "!")
print("Järgmisel aastal oled " + str(vanus_jargmisel_aastal) + "-aastane.")
print("Sinu koolitee pikkus on " + str(koolitee_m) + " meetrit.")
print("Koolitee kestab " + str(tunnid) + " tundi ja " + str(minutid) + " minutit.")
print("Keskmine kiirus on " + str(round(kiirus, 2)) + " km/h.")