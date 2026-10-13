import tkinter as tk

RUUDU_KYLG = 40
VAHE = 10
RUUTUDE_ARV = 10
SERV = 20

laius = SERV * 2 + RUUTUDE_ARV * RUUDU_KYLG + (RUUTUDE_ARV - 1) * VAHE
korgus = SERV * 2 + RUUDU_KYLG

aken = tk.Tk()
aken.title("Värvilised ruudud")

tahvel = tk.Canvas(aken, width=laius, height=korgus, bg="white")
tahvel.pack()

for i in range(RUUTUDE_ARV):
    x1 = SERV + i * (RUUDU_KYLG + VAHE)
    y1 = SERV
    if i % 2 == 0:
        varv = "red"
    else:
        varv = "blue"
    tahvel.create_rectangle(x1, y1, x1 + RUUDU_KYLG, y1 + RUUDU_KYLG, fill=varv)

aken.mainloop()