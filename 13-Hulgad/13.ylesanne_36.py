esmaspaev = {"Mari", "Jüri", "Anna", "Peeter"}
teisipaev = {"Anna", "Kati", "Peeter", "Karl"}
kolmapaev = {"Mari", "Peeter", "Liis", "Kati"}

paevad = {
    "Esmaspäev": esmaspaev,
    "Teisipäev": teisipaev,
    "Kolmapäev": kolmapaev
}


def kuva(pealkiri, nimed):
    if nimed:
        print(f"{pealkiri} ({len(nimed)}): {', '.join(sorted(nimed))}")
    else:
        print(f"{pealkiri}: puuduvad")


def vahemalt_kahel_paeval(hulgad):
    tulemus = set()
    for i in range(len(hulgad)):
        for j in range(i + 1, len(hulgad)):
            tulemus |= hulgad[i] & hulgad[j]
    return tulemus


koik = esmaspaev | teisipaev | kolmapaev
koigil_kolmel = esmaspaev & teisipaev & kolmapaev
ainult_esmaspaeval = esmaspaev - teisipaev - kolmapaev
vahemalt_kahel = vahemalt_kahel_paeval(list(paevad.values()))

kuva("Kõik erinevad külastajad", koik)
kuva("Käisid kõigil kolmel päeval", koigil_kolmel)
kuva("Käisid ainult esmaspäeval", ainult_esmaspaeval)
kuva("Käisid vähemalt kahel päeval", vahemalt_kahel)

print()
print("Külastajaid päevade kaupa:")
for paev, kulastajad in paevad.items():
    print(f"  {paev:<12}{len(kulastajad)}")
