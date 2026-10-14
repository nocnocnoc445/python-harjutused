# Ennustused:
# arvud[0]               -> 4
# arvud[-1]              -> 20
# arvud[2] + arvud[3]    -> 12 + 16 = 28
# arvud[len(arvud) - 2]  -> arvud[3] = 16
# arvud[1] * 2           -> 8 * 2 = 16
#
# Selgitus: len(arvud) on 5, aga indeksid on 0 kuni 4.
# Viimase elemendi indeks on len(arvud) - 1, seega len(arvud) - 2
# on ühe võrra eespool ehk eelviimane element.

arvud = [4, 8, 12, 16, 20]
print(arvud[0])
print(arvud[-1])
print(arvud[2] + arvud[3])
print(arvud[len(arvud) - 2])
print(arvud[1] * 2)