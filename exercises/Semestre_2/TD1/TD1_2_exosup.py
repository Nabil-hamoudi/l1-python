import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

def affichage(txt):
    affiche.configure(text=txt)

racine = tk.Tk()

text = tk.Entry(racine)
affiche = tk.Label(racine, text="affichage")
button1 = tk.Button(racine, text="Boutton 1", command=lambda: affichage(1))
button2 = tk.Button(racine, text="Boutton 2", command=lambda: affichage(2))
button3 = tk.Button(racine, text="Boutton 3", command=lambda: affichage(text.get()))

text.grid(row=1, column=1)
affiche.grid(column=1, row=0)
button1.grid(row=2)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
racine.mainloop()