import tkinter as tk

LAIUS = 600
KORGUS = 300
TRIIBU_KORGUS = KORGUS / 3

aken = tk.Tk()
aken.title("Eesti lipp")

tahvel = tk.Canvas(aken, width=LAIUS, height=KORGUS, highlightthickness=0)
tahvel.pack()

varvid = ["#0072CE", "black", "white"]

for i in range(3):
    y1 = i * TRIIBU_KORGUS
    y2 = y1 + TRIIBU_KORGUS
    tahvel.create_rectangle(0, y1, LAIUS, y2, fill=varvid[i], outline=varvid[i])

aken.mainloop()