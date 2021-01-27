import tkinter as tk

color = []


def undo():
    """"""
    global color
    if len(color) == 0:
        pass
    else:
        background.delete(color[-1])
        del color[-1]
    pass


def clic(event):
    """"""
    global color

    if event.x >= 5 and event.x <= 55 and event.y <= 55 and event.y >= 5:
        Green_cercle = background.create_oval(200, 200, 400, 400, fill="green")
        color.append(Green_cercle)
    elif event.x >= 60 and event.x <= 110 and event.y <= 55 and event.y >= 5:
        Blue_cercle = background.create_oval(200, 200, 400, 400, fill="blue")
        color.append(Blue_cercle)
    elif event.x >= 115 and event.x <= 165 and event.y <= 55 and event.y >= 5:
        White_cercle = background.create_oval(
            200, 200, 400, 400, outline="light grey", fill="white")
        color.append(White_cercle)
    else:
        cercle = background.create_oval(200, 200, 400, 400, fill="red")
        color.append(cercle)

    pass


racine = tk.Tk()  # Création de la fenêtre racine

background = tk.Canvas(
    racine, width="600", height="600", bg="white", relief="ridge")

cercle = background.create_oval(200, 200, 400, 400, fill="red")

Green_carre = background.create_rectangle(
        5, 5, 55, 55, fill="green")

Blue_carre = background.create_rectangle(
        60, 5, 110, 55, fill="blue")

White_carre = background.create_rectangle(
        115, 5, 165, 55, outline="light grey")

racine.bind("<Button-1>", clic)

Annuler = tk.Button(
    racine, text="Annuler", font=("helvetica", "10"),
    command=undo)

background.grid(column=0, row=1, rowspan=1)
Annuler.grid(column=0, row=0, rowspan=1)

racine.mainloop()  # Lancement de la boucle principale
