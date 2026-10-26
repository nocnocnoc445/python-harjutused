import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "sonum.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("Python on programmeerimiskeel.\nFailides saab andmeid säilitada.\nFailide töötlemine on kasulik oskus.\n")

with open(FAIL, "r", encoding="utf-8") as fail:
    sisu = fail.read()

print(sisu, end="")
