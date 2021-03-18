import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
RAYON_BALLE = 20
COLOR_BALLE = "red"

###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global HAUTEUR, LARGEUR, RAYON_BALLE, COLOR_BALLE
    dx, dy = LARGEUR / 100, HAUTEUR / 100
    x, y = LARGEUR / 2, HAUTEUR / 2
    cercle = canvas.create_oval(x - RAYON_BALLE, y - RAYON_BALLE, x + RAYON_BALLE, y + RAYON_BALLE, fill= COLOR_BALLE)
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global balle
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, HAUTEUR, LARGEUR
    x1, y1, x2, y2 = canvas.coords(balle[0])
    if x1 <= 0 or x2 >= LARGEUR:
        balle[1] *= -1
    elif y1 <= 0 or y2 >= HAUTEUR:
        balle[2] *= -1
    

######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
balle = creer_balle()
mouvement()
racine.mainloop()
