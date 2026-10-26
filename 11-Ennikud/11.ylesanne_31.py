def opilase_tulemus(nimi, hinded):
    keskmine = sum(hinded) / len(hinded)
    return nimi, keskmine, len(hinded)


tulemus = opilase_tulemus("Mari", (5, 4, 5, 3, 5))
print("Tagastatud ennik:", tulemus)

nimi, keskmine, hinnete_arv = tulemus
print(f"{nimi}: keskmine hinne {keskmine:.2f}, hindeid kokku {hinnete_arv}")
