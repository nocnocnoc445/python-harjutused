def analuusi_temperatuure(temperatuurid):
    keskmine = sum(temperatuurid) / len(temperatuurid)
    return min(temperatuurid), max(temperatuurid), keskmine


temperatuurid = (18, 20, 17, 22, 25, 21, 19)
madalaim, korgeim, keskmine = analuusi_temperatuure(temperatuurid)

print(f"Madalaim temperatuur: {madalaim:.1f} °C")
print(f"Kõrgeim temperatuur: {korgeim:.1f} °C")
print(f"Keskmine temperatuur: {keskmine:.1f} °C")
