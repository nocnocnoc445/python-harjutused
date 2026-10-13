import tkinter as tk

aken = tk.Tk()
aken.title("Geomeetrilised kujundid")

tahvel = tk.Canvas(aken, width=600, height=400, bg="white")
tahvel.pack()

tahvel.create_rectangle(50, 80, 200, 180, fill="red")
tahvel.create_oval(250, 80, 350, 180, fill="blue")
tahvel.create_line(400, 80, 550, 180, fill="green", width=4)
tahvel.create_oval(150, 230, 400, 330, fill="yellow")
tahvel.create_text(300, 40, text="Minu kujundid", font=("Arial", 20, "bold"))

aken.mainloop()