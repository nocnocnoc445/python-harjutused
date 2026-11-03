import string

KIRJAVAHEMARGID = string.punctuation + "„“”–—…«»"

tekst = input("Sisesta tekst: ")

sagedus = {}
for sona in tekst.split():
    sona = sona.strip(KIRJAVAHEMARGID).lower()
    if sona:
        sagedus[sona] = sagedus.get(sona, 0) + 1

if not sagedus:
    print("Tekstis pole ühtegi sõna.")
else:
    for sona in sorted(sagedus):
        print(f"{sona}: {sagedus[sona]}")

    suurim = max(sagedus.values())
    koige_sagedasemad = [sona for sona, arv in sagedus.items() if arv == suurim]

    print()
    print("Kõige sagedasem sõna:", ", ".join(koige_sagedasemad))
    print("Esinemiste arv:", suurim)
    print("Erinevaid sõnu kokku:", len(sagedus))