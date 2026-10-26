import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "koordinaadid.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("10 20\n30 40\n50 25\n70 60\n90 15\n")


def loe_punktid(failitee):
    punktid = []
    with open(failitee, "r", encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.split()
            if len(osad) == 2:
                punktid.append([int(osad[0]), int(osad[1])])
    return punktid


def keskmine(arvud):
    return sum(arvud) / len(arvud)


punktid = loe_punktid(FAIL)

x_koordinaadid = []
y_koordinaadid = []
for x, y in punktid:
    x_koordinaadid.append(x)
    y_koordinaadid.append(y)

print("Punktid:", punktid)
print()
print("Väikseim x:", min(x_koordinaadid))
print("Suurim x:", max(x_koordinaadid))
print("Väikseim y:", min(y_koordinaadid))
print("Suurim y:", max(y_koordinaadid))
print()
print(f"Keskmised koordinaadid: ({keskmine(x_koordinaadid):.2f}, {keskmine(y_koordinaadid):.2f})")
