import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

racine = tk.Tk()

racine.title("Rappel du premier semestre")
texte = tk.Label(racine, text="J'adore python")

texte.grid(column=0, row=0, rowspan=1)

racine.mainloop()