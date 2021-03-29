import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
TRAIT = HAUTEUR // 2
count = 0


###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global TRAIT
    x, y = LARGEUR // 2, (HAUTEUR / 1.5)
    dx, dy = 3, 5
    lx, ly = 0, 1
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    ligne = canvas.create_line(0, TRAIT, LARGEUR, TRAIT, fill="white")
    return [cercle, dx, dy], [ligne, lx, ly]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global balle, ligne, TRAIT
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.move(ligne[0], ligne[1], ligne[2])
    TRAIT += 1
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, TRAIT, HAUTEUR, LARGEUR, ligne, count
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= LARGEUR:
        balle[1] = -balle[1]
        count += 1
    if y1 >= HAUTEUR:
        balle[2] = -balle[2]
        count += 1
    elif y0 <= TRAIT:
        canvas.move(ligne[0], ligne[1], -50)
        balle[2] = -balle[2]
        TRAIT -= 50
        count += 1
    if count == 30:
        racine.destroy()



######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
balle, ligne = creer_balle()
mouvement()
racine.mainloop()
