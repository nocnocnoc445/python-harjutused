import os
import turtle

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
JOONIS = os.path.join(KAUST, "joonis.txt")
MAJA = os.path.join(KAUST, "maja.txt")

# kui andmefaile pole, luuakse need näidisandmetega
if not os.path.exists(JOONIS):
    with open(JOONIS, "w", encoding="utf-8") as fail:
        fail.write("UP\n-100 -100\nDOWN\n100 -100\n100 100\n-100 100\n-100 -100\nUP\n0 0\n")

if not os.path.exists(MAJA):
    with open(MAJA, "w", encoding="utf-8") as fail:
        fail.write("UP\n-100 -100\nDOWN\n100 -100\n100 50\n-100 50\n-100 -100\n"
                   "UP\n-100 50\nDOWN\n0 150\n100 50\n"
                   "UP\n-25 -100\nDOWN\n-25 0\n25 0\n25 -100\n"
                   "UP\n40 -20\nDOWN\n80 -20\n80 20\n40 20\n40 -20\n"
                   "UP\n0 -150\n")


def loe_kasud(failitee):
    kasud = []
    with open(failitee, "r", encoding="utf-8") as fail:
        for rida in fail:
            rida = rida.strip()
            if rida != "":
                kasud.append(rida)
    return kasud


def taida_kasud(t, kasud):
    for kask in kasud:
        if kask.upper() == "UP":
            t.penup()
        elif kask.upper() == "DOWN":
            t.pendown()
        else:
            osad = kask.split()
            try:
                t.goto(float(osad[0]), float(osad[1]))
            except (ValueError, IndexError):
                print(f"Tundmatu käsk jäeti vahele: {kask}")


failinimi = input("Sisesta joonise faili nimi (Enter = joonis.txt, maja jaoks maja.txt): ").strip()
if failinimi == "":
    failinimi = "joonis.txt"
failitee = os.path.join(KAUST, failinimi)

if not os.path.exists(failitee):
    print(f"Faili {failinimi} ei leitud.")
else:
    kasud = loe_kasud(failitee)

    ekraan = turtle.Screen()
    ekraan.title(f"Joonis failist {failinimi}")

    t = turtle.Turtle()
    t.pensize(2)
    t.speed(3)
    taida_kasud(t, kasud)

    turtle.done()
