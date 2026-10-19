import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "arvud.txt")):
    with open(os.path.join(KAUST, "arvud.txt"), "w", encoding="utf-8") as fail:
        fail.write('12\n8\n25\n4\n19\n32\n')

with open(os.path.join(KAUST, "arvud.txt"), "r", encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail if rida.strip()]

paaris = 0
paaritu = 0
for arv in arvud:
    if arv % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

print("Paarisarve:", paaris)
print("Paarituid arve:", paaritu)