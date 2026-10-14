import tkinter as tk

def joonista_sein(canvas, x, y, laius, korgus, varv):
    canvas.create_rectangle(x, y - korgus, x + laius, y, fill=varv, outline="")

def joonista_katus(canvas, x, y, laius, korgus):
    ulatus = 15
    katuse_korgus = laius / 2
    vasak = x - ulatus
    parem = x + laius + ulatus
    alus = y - korgus
    tipp = alus - katuse_korgus
    canvas.create_polygon(vasak, alus, x + laius / 2, tipp, parem, alus, fill="#9b5f50")

def joonista_aken(canvas, x, y, suurus):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill="#eef6fc", outline="#5f6f7a", width=3)

def joonista_uks(canvas, x, y, laius, korgus):
    ukse_laius = laius * 0.2
    ukse_korgus = korgus * 0.4
    ux = x + laius / 2 - ukse_laius / 2
    canvas.create_rectangle(ux, y - ukse_korgus, ux + ukse_laius, y, fill="#8a6552", outline="")

def joonista_maja(canvas, x, y, laius, korgus, varv):
    joonista_sein(canvas, x, y, laius, korgus, varv)
    joonista_katus(canvas, x, y, laius, korgus)

    akna_suurus = laius * 0.22
    akna_y = y - korgus + korgus * 0.2
    joonista_aken(canvas, x + laius * 0.15, akna_y, akna_suurus)
    joonista_aken(canvas, x + laius * 0.85 - akna_suurus, akna_y, akna_suurus)

    joonista_uks(canvas, x, y, laius, korgus)

aken = tk.Tk()
aken.title("Majad")
canvas = tk.Canvas(aken, width=600, height=320, bg="#d6e9f5", highlightthickness=0)
canvas.pack()

maapind = 280
canvas.create_rectangle(0, maapind, 600, 320, fill="#a3c993", outline="")

joonista_maja(canvas, 40, maapind, 140, 120, "#ecbd85")
joonista_maja(canvas, 230, maapind, 130, 190, "#dea6a0")
joonista_maja(canvas, 420, maapind, 120, 105, "#a9b8de")

aken.mainloop()