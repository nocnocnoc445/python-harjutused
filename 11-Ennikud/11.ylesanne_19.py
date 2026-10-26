jarjend = [1, 2, 3]
ennik = (1, 2, 3)

jarjend[0] = 100
print("Järjendi muutmine õnnestus:", jarjend)

try:
    ennik[0] = 100
    print("Enniku muutmine õnnestus:", ennik)
except TypeError as viga:
    print("Ennikut ei saa muuta:", viga)

print("Ennik on endiselt:", ennik)
