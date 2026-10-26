ostukorv = (
    ("Leib", 2.50, 2),
    ("Piim", 1.80, 3),
    ("Juust", 4.20, 1),
    ("Õunad", 2.90, 2)
)

lopp_summa = 0
suurim = ("", 0)

print("OSTUKORV")
print()
for nimetus, hind, kogus in ostukorv:
    maksumus = hind * kogus
    lopp_summa += maksumus
    print(f"{nimetus}: {hind:.2f} € × {kogus} = {maksumus:.2f} €")
    if maksumus > suurim[1]:
        suurim = (nimetus, maksumus)

print()
print(f"Lõppsumma: {lopp_summa:.2f} €")
print(f"Suurima kogumaksumusega toode: {suurim[0]} ({suurim[1]:.2f} €)")
