import string

KIRJAVAHEMARGID = string.punctuation + "„“”–—…«»"

tekst = input("Sisesta tekst: ")

sagedus = {}
for sona in tekst.split():
    sona = sona.strip(KIRJAVAHEMARGID).lower()
    if sona:
        sagedus[sona] = sagedus.get(sona, 0) + 1

for sona in sorted(sagedus):
    print(f"{sona}: {sagedus[sona]}")