import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "temperatuurid.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("5\n7\n3\n-2\n0\n4\n8\n")

temperatuurid = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        if rida.strip() != "":
            temperatuurid.append(int(rida))

alla_nulli = 0
yle_nulli = 0
for temperatuur in temperatuurid:
    if temperatuur < 0:
        alla_nulli += 1
    elif temperatuur > 0:
        yle_nulli += 1

keskmine = sum(temperatuurid) / len(temperatuurid)

print(f"Keskmine temperatuur: {keskmine:.2f} °C")
print(f"Kõige kõrgem temperatuur: {max(temperatuurid)} °C")
print(f"Kõige madalam temperatuur: {min(temperatuurid)} °C")
print(f"Päevi alla nulli: {alla_nulli}")
print(f"Päevi üle nulli: {yle_nulli}")
