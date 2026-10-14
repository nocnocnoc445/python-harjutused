import tkinter as tk

def joonista_ruut(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv)

aken = tk.Tk()
aken.title("Ruudud")
canvas = tk.Canvas(aken, width=500, height=300, bg="white")
canvas.pack()

joonista_ruut(canvas, 20, 20, 60, "red")
joonista_ruut(canvas, 110, 40, 90, "blue")
joonista_ruut(canvas, 230, 30, 40, "green")
joonista_ruut(canvas, 300, 100, 120, "yellow")
joonista_ruut(canvas, 60, 160, 100, "purple")

aken.mainloop()