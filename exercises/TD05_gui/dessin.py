import random
import tkinter as tk

color = "blue"
objets = []


def dessinCercle():
    """dessine un cercle"""
    taille = []
    global color
    global objets

    for i in range(4):
        taille.append(random.randint(0, 400))

    A = background.create_oval(taille, outline=color)

    objets.append(A)

    pass


def dessinCarre():
    """dessine un carre"""
    global color
    global objets

    taille = []
    for i in range(2):
        taille.append(random.randint(0, 400))

    A = background.create_rectangle(
        taille[0] + 100, taille[1] + 100, taille[0], taille[1], outline=color)

    objets.append(A)

    pass


def dessinCroix():
    """dessine une croix"""
    taille = []
    global color
    global objets

    for i in range(4):
        taille.append(random.randint(0, 400))

    taille2 = [taille[2], taille[1], taille[0], taille[3]]

    A = background.create_line(taille, fill=color)
    B = background.create_line(taille2, fill=color)

    objets.append(A)
    objets.append(B)

    pass


def ColorChange():
    global color
    color = str(input("choisisser une couleur"))

    pass


def undo():
    global objets
    if len(objets) == 0:
        pass
    elif background.type(objets[-1]) == "line":
        background.delete(objets[-1])
        del objets[-1]
        background.delete(objets[-1])
        del objets[-1]

    else:
        background.delete(objets[-1])
        del objets[-1]
    pass


racine = tk.Tk()

background = tk.Canvas(
    racine, width="400", height="400", bg="black", relief='ridge',
    borderwidth=12)

background.grid(column=1, row=1, rowspan=4)

Retour = tk.Button(
    racine, text="Undo", font=("helvetica", "10"),
    command=undo)
ChangeColor = tk.Button(
    racine, text="Changer la couleur", font=("helvetica", "10"),
    command=ColorChange)
Cercle = tk.Button(
    racine, text="Cercle", font=("helvetica", "10"), command=dessinCercle)
Carre = tk.Button(
    racine, text="Carre", font=("helvetica", "10"), command=dessinCarre)
Croix = tk.Button(
    racine, text="Croix", font=("helvetica", "10"), command=dessinCroix)

Cercle.grid(column=0, row=1, rowspan=1)
Carre.grid(column=0, row=2, rowspan=1)
Croix.grid(column=0, row=3, rowspan=1)
ChangeColor.grid(column=1, row=0, rowspan=1)
Retour.grid(column=1, row=5, rowspan=1)

racine.mainloop()
