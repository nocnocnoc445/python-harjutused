andmed = [
    [10, 20, 30],
    [40, 50],
    [60, 70, 80, 90]
]

#Vastused:
# 1) Välimises järjendis on 3 elementi
# 2) Esimeses sisemises järjendis on 3 elementi
# 3) andmed[1][1] = 50
# 4) Väärtus 80 asub indeksitel [2][2]
# 5) len(andmed) on 3
# len(andmed[2]) on 4

print("Välimise järjendi elemente:", len(andmed))
print("Esimese sisemise järjendi elemente:", len(andmed[0]))
print("andmed[1][1] =", andmed[1][1])
print("andmed[2][2] =", andmed[2][2])
print("len(andmed) =", len(andmed))
print("len(andmed[2]) =", len(andmed[2]))