import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

compt = 0

def quitter():
    racine.destroy()

def compteur(event):
    global compt, titre
    compt += 1
    titre.configure(text=str(compt))

def affiche(event):
    color = event.widget["bg"]
    titre.configure(text=color)
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
racine.title("Rappel du premier Semestre")
titre = tk.Label(racine, text="J'adore python")
quitbutton = tk.Button(racine, text="quitter", command=quitter)
imagebutton = tk.Button(racine, text="charge une image", command=lambda: charger(top))
redcanvas = tk.Canvas(racine, width="300", height="300", bg="red")
blackcanvas = tk.Canvas(racine, width="300", height="300", bg="black")
redcanvas.bind("<Button-1>", compteur)
redcanvas.bind("<Double-Button-1>", affiche)
blackcanvas.bind("<Double-Button-1>", affiche)

top = tk.Toplevel()

titre.grid(row=2)
quitbutton.grid(row=4)
redcanvas.grid(row=0, column=1, rowspan=4)
blackcanvas.grid(row=4, column=1, rowspan=4)
imagebutton.grid(row=6)

racine.mainloop()
