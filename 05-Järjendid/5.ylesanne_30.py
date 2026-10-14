temperatuurid = []

with open("temperatuurid.txt", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida != "":
            temperatuurid.append(int(rida))

miinus = 0
vahemalt_5 = 0

for temp in temperatuurid:
    if temp < 0:
        miinus += 1
    if temp >= 5:
        vahemalt_5 += 1

keskmine = sum(temperatuurid) / len(temperatuurid)

print("Mõõtmisi:", len(temperatuurid))
print(f"Keskmine temperatuur: {keskmine:.1f} °C")
print(f"Kõrgeim temperatuur: {max(temperatuurid)} °C")
print(f"Madalaim temperatuur: {min(temperatuurid)} °C")
print("Miinuskraadidega päevi:", miinus)
print("Vähemalt 5-kraadiseid päevi:", vahemalt_5)