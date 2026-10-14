arvud = []

with open("arvud.txt", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida != "":
            arvud.append(int(rida))

print("Arvud:", arvud)
print("Suurim:", max(arvud))
print("Väikseim:", min(arvud))
print(f"Keskmine: {sum(arvud) / len(arvud):.2f}")
print("Kasvavas järjekorras:", sorted(arvud))