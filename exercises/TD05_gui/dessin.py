import random
import tkinter as tk

color = "red"

def dessinCercle():
    """dessine un cercle"""
    taille = []
    global color

    for i in range(4):
        taille.append(random.randint(0, 400))

    Cercle = background.create_oval(taille[0], taille[1], taille[2], taille[3], outline=color)

    pass


def dessinCarre():
    """dessine un carre"""
    global color
    taille = []
    for i in range(4):
        taille.append(random.randint(0, 400))

    Carre = background.create_rectangle(taille[0], taille[1], taille[2], taille[3], outline=color)

    pass


def dessinCroix():
    """dessine une croix"""
    taille = []
    global color

    for i in range(4):
        taille.append(random.randint(0, 400))

    taille2 = [taille[2], taille[1], taille[0], taille[3]]

    Croix = (background.create_line(taille, fill=color), background.create_line(taille2, fill=color))

    pass


def ColorChange():
    global color
    color = str(input("choisisser une couleur"))

    pass


racine = tk.Tk()

background = tk.Canvas(racine, width="400", height="400", bg="black",
    relief='ridge', borderwidth=12)

background.grid(column=1, row=1, rowspan=4)


ChangeColor = tk.Button(racine, text="Changer la couleur", font=("helvetica", "10"), command=ColorChange)
Cercle = tk.Button(racine, text="Cercle", font=("helvetica", "10"), command=dessinCercle)
Carre = tk.Button(racine, text="Carre", font=("helvetica", "10"), command=dessinCarre)
Croix = tk.Button(racine, text="Croix", font=("helvetica", "10"), command=dessinCroix)

Cercle.grid(column=0, row=1, rowspan=1)
Carre.grid(column=0, row=2, rowspan=1)
Croix.grid(column=0, row=3, rowspan=1)
ChangeColor.grid(column=1, row=0, rowspan=1)

racine.mainloop()
