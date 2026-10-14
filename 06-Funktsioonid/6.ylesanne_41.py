import tkinter as tk

def joonista_ring(canvas, x, y, raadius, varv):
    canvas.create_oval(x - raadius, y - raadius, x + raadius, y + raadius, fill=varv)

aken = tk.Tk()
aken.title("Ringid")
canvas = tk.Canvas(aken, width=600, height=300, bg="white")
canvas.pack()

varvid = ["red", "orange", "yellow", "green", "blue"]

for i in range(10):
    x = 40 + i * 55
    raadius = 10 + i * 3
    varv = varvid[i % len(varvid)]
    joonista_ring(canvas, x, 150, raadius, varv)

aken.mainloop()