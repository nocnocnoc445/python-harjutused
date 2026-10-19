import os

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(os.path.join(KAUST, "tekst.txt")):
    with open(os.path.join(KAUST, "tekst.txt"), "w", encoding="utf-8") as fail:
        fail.write('Python on populaarne programmeerimiskeel.\nPython sobib hästi algajatele.\nFailide töötlemine on oluline oskus.\n')
KIRJAVAHEMARGID = ".,!?;:\"'()[]-–—«»„“”"

failinimi = input("Sisesta analüüsitava faili nimi: ").strip()

try:
    with open(os.path.join(KAUST, failinimi), "r", encoding="utf-8") as fail:
        tekst = fail.read()
except FileNotFoundError:
    print("Viga: sellist faili ei leitud.")
else:
    sonad = []
    for sona in tekst.split():
        puhas = sona.strip(KIRJAVAHEMARGID).lower()
        if puhas:
            sonad.append(puhas)

    # lause = tükk, mis lõpeb . ! või ?
    lausetekst = tekst.replace("!", ".").replace("?", ".")
    lauseid = len([osa for osa in lausetekst.split(".") if osa.strip()])

    pikim = ""
    for sona in sonad:
        if len(sona) > len(pikim):
            pikim = sona

    sagedused = {}
    for sona in sonad:
        sagedused[sona] = sagedused.get(sona, 0) + 1
    top5 = sorted(sagedused.items(), key=lambda paar: paar[1], reverse=True)[:5]

    read = [
        f"TEKSTIANALÜÜS: {failinimi}",
        "------------------------------",
        f"Sõnu: {len(sonad)}",
        f"Lauseid (ligikaudu): {lauseid}",
        f"Pikim sõna: {pikim} ({len(pikim)} tähte)",
        "",
        "Viis sagedasemat sõna:",
    ]
    for nr, (sona, kordi) in enumerate(top5, start=1):
        read.append(f"{nr}. {sona} - {kordi} korda")

    with open(os.path.join(KAUST, "tekstianaluus.txt"), "w", encoding="utf-8") as fail:
        fail.write("\n".join(read) + "\n")

    print()
    print("\n".join(read))
    print()
    print("Tulemused salvestati faili tekstianaluus.txt.")