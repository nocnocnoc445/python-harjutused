import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

if not os.path.exists(os.path.join(KAUST, "nimed.txt")):
    with open(os.path.join(KAUST, "nimed.txt"), "w", encoding="utf-8") as fail:
        fail.write('Mari\nJüri\nAnna\nPeeter\nKati\nMartin\n')

with open(os.path.join(KAUST, "nimed.txt"), "r", encoding="utf-8") as fail:
    read = fail.readlines()

# tühje ridu ei loe
nimed = [rida.strip() for rida in read if rida.strip()]

print(f"Failis on {len(nimed)} nime.")