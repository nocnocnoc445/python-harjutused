import os
import turtle

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "koordinaadid.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("10 20\n30 40\n50 25\n70 60\n90 15\n")

# turtle-i keskpunkt (0, 0) on akna keskel, seega nihutatakse andmete (0, 0)
# vasakule alla ja suurendatakse koordinaate, et punktid oleksid hästi näha
MOOTKAVA = 4
NIHE_X = -200
NIHE_Y = -150


def loe_punktid(failitee):
    punktid = []
    with open(failitee, "r", encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.split()
            if len(osad) == 2:
                punktid.append([int(osad[0]), int(osad[1])])
    return punktid


def ekraanile(x, y):
    return x * MOOTKAVA + NIHE_X, y * MOOTKAVA + NIHE_Y


def joonista_teljed(t):
    t.color("gray")
    t.penup()
    t.goto(ekraanile(0, 0))
    t.pendown()
    t.goto(ekraanile(105, 0))
    t.write(" x")
    t.penup()
    t.goto(ekraanile(0, 0))
    t.pendown()
    t.goto(ekraanile(0, 75))
    t.write(" y")
    t.penup()


punktid = loe_punktid(FAIL)

ekraan = turtle.Screen()
ekraan.setup(600, 500)
ekraan.title("Punktid failist koordinaadid.txt")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

joonista_teljed(t)

for i in range(len(punktid)):
    x, y = punktid[i]
    ekraani_x, ekraani_y = ekraanile(x, y)
    t.goto(ekraani_x, ekraani_y)
    t.dot(12, "red")
    t.goto(ekraani_x + 8, ekraani_y + 4)
    t.color("black")
    t.write(f"{i + 1}. ({x}, {y})", font=("Arial", 10, "normal"))

turtle.done()
