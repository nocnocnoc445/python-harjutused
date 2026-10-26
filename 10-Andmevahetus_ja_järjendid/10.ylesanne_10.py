import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "inimesed.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Mari 18\nJaan 21\nKati 17\nPeeter 25\nAnna 19\n")

nimed = []
vanused = []
with open(FAIL, "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 2:
            nimed.append(osad[0])
            vanused.append(int(osad[1]))

print("Vähemalt 18-aastased:")
for i in range(len(nimed)):
    if vanused[i] >= 18:
        print(nimed[i])

print()
print(f"Keskmine vanus: {sum(vanused) / len(vanused):.1f}")
