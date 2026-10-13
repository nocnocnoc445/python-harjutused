import tkinter as tk

LAIUS = 600
KORGUS = 400
TAUST = "white"

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=LAIUS,
    height=KORGUS,
    bg=TAUST
)
tahvel.pack()

aken.mainloop()