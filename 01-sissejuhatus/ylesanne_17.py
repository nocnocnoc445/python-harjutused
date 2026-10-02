# pikkus = int(input("Sisesta pikkus: "))
# laius = int(input("Sisesta laius: "))
# pindala = pikkus * laius
# print("Pindala on:", pindala)




# Mitu meetrit on igas ühikus
ÜHIKUD = {"mm": 0.001, "cm": 0.01, "dm": 0.1, "m": 1, "km": 1000}


def loe_mõõt(küsimus):
    tekst = input(küsimus).strip().lower().replace(",", ".").replace(" ", "")
    arv_osa = tekst.rstrip("abcdefghijklmnopqrstuvwxyz")
    ühik = tekst[len(arv_osa):] or "m"  # kui ühikut pole, siis meeterid
    if ühik not in ÜHIKUD:
        print("Tundmatu ühik:", ühik)
        exit()
    return float(arv_osa), ühik


pikkus, pikkuse_ühik = loe_mõõt("Sisesta pikkus: ")
laius, laiuse_ühik = loe_mõõt("Sisesta laius: ")

if pikkuse_ühik == laiuse_ühik:
    # Samad ühikud, siis vastus sama ühikuga
    pindala = pikkus * laius
    ühik = pikkuse_ühik
else:
    # Erinevad ühikud teisendavad meetriteks
    pindala = pikkus * ÜHIKUD[pikkuse_ühik] * laius * ÜHIKUD[laiuse_ühik]
    ühik = "m"

print(f"Pindala on: {round(pindala, 6):g} {ühik}²")


#natuke igav hakkas ja tahtsin teha, et saaks ka ümber arvutada ühikuid