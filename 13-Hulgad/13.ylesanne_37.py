skaneering_1 = {
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "192.168.1.15"
}
skaneering_2 = {
    "192.168.1.10",
    "192.168.1.12",
    "192.168.1.20",
    "192.168.1.25"
}


def ip_voti(ip):
    # IP-aadress sorteeritakse arvude, mitte tähtede järgi
    return [int(osa) for osa in ip.split(".")]


def kuva_jaotis(pealkiri, aadressid):
    print(f"{pealkiri} ({len(aadressid)}):")
    if not aadressid:
        print("  -")
    for ip in sorted(aadressid, key=ip_voti):
        print(f"  {ip}")
    print()


def vordluse_aruanne(esimene, teine):
    print("=" * 40)
    print("  VÕRGUSKANEERIMISTE VÕRDLUS")
    print("=" * 40)
    print()
    kuva_jaotis("Mõlemas skaneeringus", esimene & teine)
    kuva_jaotis("Ainult esimeses skaneeringus", esimene - teine)
    kuva_jaotis("Ainult teises skaneeringus", teine - esimene)
    kuva_jaotis("Kõik tuvastatud seadmed", esimene | teine)
    print("=" * 40)


vordluse_aruanne(skaneering_1, skaneering_2)
