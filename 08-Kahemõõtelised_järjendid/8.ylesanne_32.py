READE = 5
KOHTI = 8

saal = []
for i in range(READE):
    rida = []
    for j in range(KOHTI):
        rida.append(0)
    saal.append(rida)


def loe_tais_arv(kysimus, vahim, suurim):
    while True:
        sisend = input(kysimus).strip()
        if sisend.isdigit() and vahim <= int(sisend) <= suurim:
            return int(sisend)
        print(f"Sisesta täisarv vahemikus {vahim}–{suurim}.")


def kuva_plaan():
    pais = "Koht:   "
    for koht in range(1, KOHTI + 1):
        pais += str(koht) + " "
    print(pais.strip())
    for i in range(READE):
        tekst = f"Rida {i + 1}: "
        for koht in saal[i]:
            tekst += str(koht) + " "
        print(tekst.strip())
    print("(0 = vaba, 1 = broneeritud)")


def broneeri():
    rida = loe_tais_arv(f"Rida (1–{READE}): ", 1, READE)
    koht = loe_tais_arv(f"Koht (1–{KOHTI}): ", 1, KOHTI)
    if saal[rida - 1][koht - 1] == 1:
        print("See koht on juba broneeritud.")
    else:
        saal[rida - 1][koht - 1] = 1
        print(f"Rida {rida}, koht {koht} broneeritud.")


def kontrolli():
    rida = loe_tais_arv(f"Rida (1–{READE}): ", 1, READE)
    koht = loe_tais_arv(f"Koht (1–{KOHTI}): ", 1, KOHTI)
    if saal[rida - 1][koht - 1] == 1:
        print("Koht on broneeritud.")
    else:
        print("Koht on vaba.")


def vabade_arv():
    arv = 0
    for rida in saal:
        for koht in rida:
            if koht == 0:
                arv += 1
    return arv


while True:
    print()
    print("1 - Kuva istekohtade plaan")
    print("2 - Broneeri koht")
    print("3 - Kontrolli kohta")
    print("4 - Vabade kohtade arv")
    print("0 - Välju")
    valik = input("Valik: ").strip()

    if valik == "1":
        kuva_plaan()
    elif valik == "2":
        broneeri()
    elif valik == "3":
        kontrolli()
    elif valik == "4":
        print("Vabu kohti:", vabade_arv())
    elif valik == "0":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik.")