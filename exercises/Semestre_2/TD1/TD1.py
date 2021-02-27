import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

def QUITTER():
    """ferme la fenetre"""
    racine.destroy()


def affiche(event):
    """"""
    color = event.widget["bg"]
    texte.configure(text=color)
    pass


count = 0


def compteur(event):
    """"""
    global count
    count += 1
    texte.configure(text=str(count))


create=True

def charger(widg):
    global create
    global photo
    global img
    global canvas
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    print(photo)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()
        create=False
        
    else:
        canvas.pack_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()


racine = tk.Tk()

canvas_red = tk.Canvas(racine, width="300", height="300", bg="red")
canvas_black = tk.Canvas(racine, width="300", height="300", bg="black")
racine.title("Rappel du premier semestre")
texte = tk.Label(racine, text="J'adore python")
bouton = tk.Button(racine, text="QUITTER", bg="blue", fg="green", command=QUITTER)
bouton_image = tk.Button(racine, text="choisir image", bg="blue", fg="green", command=lambda: charger(top))

canvas_red.bind('<Button-1>', compteur)
canvas_black.bind('<Double-Button-1>', affiche)
canvas_red.bind('<Double-Button-1>', affiche)

top = tk.Toplevel()

canvas_red.grid(column=1, row=0, rowspan=2)
canvas_black.grid(column=1, row=2, rowspan=2)
texte.grid(column=0, row=0)
bouton.grid(column=0, row=1, rowspan=2)
bouton_image.grid(column=0, row=3, rowspan=1)

racine.mainloop()
