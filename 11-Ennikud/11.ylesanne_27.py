def ristkulik(laius, korgus):
    pindala = laius * korgus
    umbermoot = 2 * (laius + korgus)
    return pindala, umbermoot


pindala, umbermoot = ristkulik(8, 5)

print("Ristküliku laius 8 ja kõrgus 5")
print("Pindala:", pindala)
print("Ümbermõõt:", umbermoot)
