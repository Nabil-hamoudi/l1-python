import tkinter as tk
import random


def get_color(r, g, b):
    """Retourne une couleur à partir de ses composantes RGB"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(RGB, x, y):
    """"""
    RGB = get_color(RGB[0], RGB[1], RGB[2])
    background.create_line(x, y, x + 1, y + 1, fill=RGB)


def ecran_aleatoire():
    """Cree un cran avec des couleurs de pixel aléatoire"""
    RGB = [0, 0, 0]

    for i in range(256):
        for n in range(256):
            RGB = [random.randint(0, 255) for _ in range(3)]
            draw_pixel(RGB, i, n)
    pass


def degrade_2D():
    """cree un degradé entre le bleu et le rouge"""
    RGB = [0, 0, 0]

    for i in range(256):
        for p in range(256):
            RGB = [i, 0, p]
            draw_pixel(RGB, i, p)
    pass


def degrade_gris():
    """cree un degrader de gris"""
    for i in range(256):
        RGB = [i, i, i]
        for p in range(256):
            draw_pixel(RGB, i, p)

    pass


racine = tk.Tk()

background = tk.Canvas(
    racine, width=256, height=256, bg="black", relief='ridge',
    borderwidth=0)

Aleatoire = tk.Button(
    racine, text="Aleatoire", font=("helvetica", "10"),
    command=ecran_aleatoire)

Degradergris = tk.Button(
    racine, text="Dégradé de gris", font=("helvetica", "10"),
    command=degrade_gris)

Degrader2D = tk.Button(
    racine, text="Dégradé 2D", font=("helvetica", "10"),
    command=degrade_2D)

Aleatoire.grid(column=0, row=0, rowspan=1)
Degradergris.grid(column=0, row=1, rowspan=1)
Degrader2D.grid(column=0, row=2, rowspan=1)
background.grid(column=1, row=0, rowspan=3)


racine.mainloop()
