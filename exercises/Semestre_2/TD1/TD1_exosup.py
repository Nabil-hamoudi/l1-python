import tkinter as tk


def affiche(nombre):
    """affiche nombre"""
    global text
    label_affichage.configure(text=str(nombre))


racine = tk.Tk()

text = tk.Entry(racine)
label_affichage = tk.Label(racine, text="affichage", bg="white")
button1 = tk.Button(racine, text="boutton 1", bg="blue", fg="green", command=lambda: affiche(1))
button2 = tk.Button(racine, text="boutton 2", bg="blue", fg="green", command=lambda: affiche(2))
button3 = tk.Button(racine, text="boutton 3", bg="blue", fg="green", command=lambda: affiche(text.get()))

label_affichage.grid(columnspan=1, column=1)
text.grid(row=1, column=1)
button1.grid(row=2, column=0, columnspan=1)
button2.grid(row=2, column=1, columnspan=1)
button3.grid(row=2, column=2, columnspan=1)

racine.mainloop()