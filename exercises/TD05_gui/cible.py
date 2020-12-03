import tkinter as tk

color = ["blue", "green", "black", "yellow", "magenta", "red"]

nbr = int(input("choississez le nombre de cercle"))

taille = []
for i in range(2):
    taille.append((int(input("choisissez votre résolution"))))

racine = tk.Tk()

background = tk.Canvas(
    racine, width=taille[0], height=taille[1], bg="black", relief='ridge',
    borderwidth=0)

background.grid(column=1, row=1, rowspan=1)

adj_coordone1 = taille[0] / (nbr * 2)
adj_coordone2 = taille[1] / (nbr * 2)


for i in range(nbr):

    x = taille[0] - (i * adj_coordone1)
    y = taille[1] - (i * adj_coordone2)

    if taille[0] >= taille[1]:
        background.create_oval(
            i * adj_coordone2, i * adj_coordone2, y, y,
            outline=color[0], fill=color[0])

    elif taille[1] <= taille[0]:
        background.create_oval(
            i * adj_coordone1, i * adj_coordone2, x, y,
            outline=color[0], fill=color[0])

    colorbis = color.pop(0)
    color.append(colorbis)


racine.mainloop()
