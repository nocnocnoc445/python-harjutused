import os
import turtle

KAUST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "andmed")
os.makedirs(KAUST, exist_ok=True)
FAIL = os.path.join(KAUST, "mootmised.txt")

# kui andmefaili pole, luuakse see ülesande näidisandmetega
if not os.path.exists(FAIL):
    with open(FAIL, "w", encoding="utf-8") as fail:
        fail.write("1 12\n2 15\n3 14\n4 18\n5 21\n6 19\n7 23\n")

# joonistusala suurus pikslites, graafik venitatakse sellele alale
LAIUS = 500
KORGUS = 300


def loe_mootmised(failitee):
    mootmised = []
    with open(failitee, "r", encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.split()
            if len(osad) == 2:
                mootmised.append([int(osad[0]), float(osad[1])])
    return mootmised


def ekraanile(x, y):
    # min_x, min_y ja mõõtkavad arvutatakse allpool pärast andmete lugemist
    ekraani_x = -LAIUS / 2 + (x - min_x) * mootkava_x
    ekraani_y = -KORGUS / 2 + (y - min_y) * mootkava_y
    return ekraani_x, ekraani_y


def joonista_teljed(t, mootmised):
    t.color("gray")
    t.penup()
    t.goto(-LAIUS / 2 - 20, KORGUS / 2 + 20)
    t.pendown()
    t.goto(-LAIUS / 2 - 20, -KORGUS / 2 - 20)
    t.goto(LAIUS / 2 + 20, -KORGUS / 2 - 20)
    t.penup()

    # y-teljele väikseim ja suurim väärtus, x-teljele mõõtmiste numbrid
    t.goto(-LAIUS / 2 - 55, -KORGUS / 2 - 6)
    t.write(f"{min_y:.1f}")
    t.goto(-LAIUS / 2 - 55, KORGUS / 2 - 6)
    t.write(f"{max_y:.1f}")
    for x, y in mootmised:
        ekraani_x, ekraani_y = ekraanile(x, y)
        t.goto(ekraani_x - 3, -KORGUS / 2 - 40)
        t.write(str(x))


def joonista_graafik(t, mootmised):
    t.color("blue")
    t.penup()
    for x, y in mootmised:
        t.goto(ekraanile(x, y))
        t.pendown()
        t.dot(10)
    t.penup()


def joonista_keskmine(t, keskmine):
    t.color("red")
    t.goto(ekraanile(min_x, keskmine))
    t.pendown()
    t.goto(ekraanile(max_x, keskmine))
    t.penup()
    t.write(f"  Keskmine: {keskmine:.2f}")


mootmised = loe_mootmised(FAIL)

x_vaartused = []
y_vaartused = []
for x, y in mootmised:
    x_vaartused.append(x)
    y_vaartused.append(y)

keskmine = sum(y_vaartused) / len(y_vaartused)
print(f"Mõõdetud väärtuste keskmine: {keskmine:.2f}")

min_x = min(x_vaartused)
max_x = max(x_vaartused)
min_y = min(y_vaartused)
max_y = max(y_vaartused)

# mõõtkava arvutatakse andmete järgi; kui kõik väärtused on võrdsed, väldime nulliga jagamist
if max_x > min_x:
    mootkava_x = LAIUS / (max_x - min_x)
else:
    mootkava_x = 1
if max_y > min_y:
    mootkava_y = KORGUS / (max_y - min_y)
else:
    mootkava_y = 1

ekraan = turtle.Screen()
ekraan.setup(LAIUS + 200, KORGUS + 200)
ekraan.title("Mõõtmiste graafik")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

joonista_teljed(t, mootmised)
joonista_graafik(t, mootmised)
joonista_keskmine(t, keskmine)

turtle.done()
