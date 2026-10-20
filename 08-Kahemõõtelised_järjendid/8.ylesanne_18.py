andmed = [
    [1, 2],
    [],
    [3],
    [],
    [4, 5, 6],
    []
]

tuhjad_indeksid = []
uued_andmed = []

for i in range(len(andmed)):
    if len(andmed[i]) == 0:
        tuhjad_indeksid.append(i)
    else:
        uued_andmed.append(andmed[i][:])  # koopia, et algne jääks muutmata

print("Tühje järjendeid:", len(tuhjad_indeksid))
print("Tühjade indeksid:", tuhjad_indeksid)
print("Ilma tühjadeta:", uued_andmed)
print("Algne järjend:", andmed)