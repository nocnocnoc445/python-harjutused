def statistika(arvud):
    keskmine = sum(arvud) / len(arvud)
    return min(arvud), max(arvud), keskmine


arvud = (4, 8, 15, 16, 23, 42)
vaikseim, suurim, keskmine = statistika(arvud)

print("Arvud:", arvud)
print("Väikseim arv:", vaikseim)
print("Suurim arv:", suurim)
print(f"Aritmeetiline keskmine: {keskmine:.2f}")
