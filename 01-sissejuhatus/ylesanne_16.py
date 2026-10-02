print(2 ** 3 ** 2)      # 3 ** 2 = 9, 2 ** 9 = 512
print((2 ** 3) ** 2)     # 2 ** 3 = 8, 8 ** 2 = 64
print(2 ** (3 ** 2))     # 3 ** 2 = 9, 2 ** 9 = 512

# see on kuna ** tehted arvutatakse paremalt vasakule, seega 2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512