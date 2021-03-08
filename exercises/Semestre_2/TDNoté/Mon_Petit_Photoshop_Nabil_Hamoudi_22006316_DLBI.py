import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

create=True
nomImgCourante=""


def nbrCol(matrice):
    return len(matrice[0])


def nbrLig(matrice):
    return len(matrice)


def saving(matPix, filename):
    toSave=pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)


def loading(filename):
    toLoad=pil.Image.open(filename)
    mat=[[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat


def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante=filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)
        create=False
        
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin=canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)


def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante="modif.png"


def filtre_vert():
    mat = loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=(0,mat[i][j][1],0,255)
    modify(mat)


def negatif():
    mat = loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=(255-mat[i][j][0],255-mat[i][j][1],255-mat[i][j][2],255)
    modify(mat)
            

def symetrique():
    mat = loading(nomImgCourante)
    matSym=[[(0,0,0,0)]*nbrCol(mat) for k in range(nbrLig(mat))]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            matSym[i][nbrCol(mat)-1-j]=mat[i][j]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=matSym[i][j]
    modify(mat)


def gris():
    #On utilisera la conversion CIE709 qui permet de calculer la teinte de gris qui va être affichée dans le pixel
    #La teinte affichée est : gris=0,2125*rouge + 0,0721*bleu + 0,7154*vert
    mat = loading(nomImgCourante)
    res = []
    for i in mat:
        for n in range(nbrCol(mat)):
            TeinteGris = int(i[n][0] * 0.2125 + i[n][1] * 0.0721 + 0.7154 * i[n][2])
            i[n] = (TeinteGris, TeinteGris, TeinteGris, 255)
        res.append(i)
    modify(mat)


def quitter():
    racine.destroy()
    pass

racine = tk.Tk()
racine.title("Mon petit photoshop")

Boutton_charger = tk.Button(racine, text="CHARGER", command=lambda: charger(racine))
Boutton_negatif = tk.Button(racine, text="NEGATIF", command=negatif)
Boutton_symetrique = tk.Button(racine, text="SYMETRIE", command=symetrique)
Boutton_gris = tk.Button(racine, text="GRIS", command=gris)
Boutton_quit = tk.Button(racine, text="QUITTER", command=quitter)
Boutton_vert = tk.Button(racine, text="FILTRE VERT", command=filtre_vert)
image = tk.Canvas(racine, height=300, width=300, bg="black")
texte = tk.Label(racine, text="HAMOUDI Nabil 22006316")

image.grid(column=1, rowspan=4)
Boutton_gris.grid(row=0)
Boutton_symetrique.grid(row=1)
Boutton_negatif.grid(row=2)
Boutton_charger.grid(row=4)
Boutton_vert.grid(row=3)
Boutton_quit.grid(row=4, column=2)
texte.grid(row=4, column=1)

racine.mainloop()
