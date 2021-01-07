import tkinter as tk

def clic(event):
    """met un cercle rouge ou bleu lors du clic"""

    if event.x > 262:
        background.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, outline="blue")
    else:
        background.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, outline="red")

    pass


racine = tk.Tk()

background = tk.Canvas(
    racine, width="500", height="500", bg="black", relief='ridge',
    borderwidth=12)

background.create_line(262, 512, 262, 12, fill="white")

racine.bind("<Button-1>", clic)

background.grid(column=0, row=0, rowspan=1)

racine.mainloop()
