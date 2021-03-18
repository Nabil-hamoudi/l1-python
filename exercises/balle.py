import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400


###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(100, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, HAUTEUR, LARGEUR
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= LARGEUR:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= HAUTEUR:
        balle[2] = -balle[2]


######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
balle = creer_balle()
mouvement()
racine.mainloop()
