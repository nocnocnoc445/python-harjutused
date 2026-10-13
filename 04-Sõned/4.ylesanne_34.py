import tkinter as tk

RUUDU_KYLG = 50
RUUTE = 8
HELE = "#EEEED2"
TUME = "#769656"

aken = tk.Tk()
aken.title("Malelaud")

tahvel = tk.Canvas(aken, width=RUUDU_KYLG * RUUTE, height=RUUDU_KYLG * RUUTE, highlightthickness=0)
tahvel.pack()

for rida in range(RUUTE):
    for veerg in range(RUUTE):
        x1 = veerg * RUUDU_KYLG
        y1 = rida * RUUDU_KYLG
        if (rida + veerg) % 2 == 0:
            varv = HELE
        else:
            varv = TUME
        tahvel.create_rectangle(x1, y1, x1 + RUUDU_KYLG, y1 + RUUDU_KYLG, fill=varv, outline="")

aken.mainloop()