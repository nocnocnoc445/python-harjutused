def suurim(arvud):
    if not arvud:
        raise ValueError("Tühjal järjendil pole suurimat elementi.")
    if len(arvud) == 1:
        return arvud[0]

    ulejaanute_suurim = suurim(arvud[1:])
    if arvud[0] > ulejaanute_suurim:
        return arvud[0]
    return ulejaanute_suurim


print("suurim([4, 9, 2, 7]) =", suurim([4, 9, 2, 7]))
print("suurim([-5, -2, -8]) =", suurim([-5, -2, -8]))

try:
    suurim([])
except ValueError as viga:
    print("suurim([]) -> ValueError:", viga)
