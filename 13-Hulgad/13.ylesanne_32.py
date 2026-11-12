import os

KAUST = os.path.dirname(os.path.abspath(__file__))
ANDMED = os.path.join(KAUST, "andmed")
FAIL_A = os.path.join(ANDMED, "grupp_a.txt")
FAIL_B = os.path.join(ANDMED, "grupp_b.txt")

NIMED_A = "Mari\nJüri\nAnna\nPeeter\nKati\n"
NIMED_B = "Anna\nKati\nToomas\nKarl\nJüri\n"


def loo_fail(fail, sisu):
    if not os.path.exists(fail):
        os.makedirs(ANDMED, exist_ok=True)
        with open(fail, "w", encoding="utf-8") as f:
            f.write(sisu)


def loe_nimed(fail):
    nimed = set()
    with open(fail, "r", encoding="utf-8") as f:
        for rida in f:
            nimi = rida.strip()
            if nimi:
                nimed.add(nimi)
    return nimed


# kui faile veel pole, luuakse need kausta andmed/
loo_fail(FAIL_A, NIMED_A)
loo_fail(FAIL_B, NIMED_B)

grupp_a = loe_nimed(FAIL_A)
grupp_b = loe_nimed(FAIL_B)

print("Mõlemas failis:", ", ".join(sorted(grupp_a & grupp_b)))
print("Ainult ühes failis:", ", ".join(sorted(grupp_a ^ grupp_b)))
