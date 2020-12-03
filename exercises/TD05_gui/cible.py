import tkinter as tk

color = ["blue", "green", "black", "yellow", "magenta", "red"]

nbr = int(input("choississez le nombre de cercle"))

taille = ((int(input("choisissez votre résolution"))))

racine = tk.Tk()

background = tk.Canvas(
    racine, width=taille, height=taille, bg="black", relief='ridge',
    borderwidth=0)

background.grid(column=1, row=1, rowspan=1)

adj = taille / (nbr * 2)

for i in range(nbr):

    x = taille - (i * adj)
    y = i * adj

    background.create_oval(y, y, x, x, outline=color[0], fill=color[0])
    colorbis = color.pop(0)
    color.append(colorbis)


racine.mainloop()
