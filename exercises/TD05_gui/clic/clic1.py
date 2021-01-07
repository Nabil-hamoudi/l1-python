import tkinter as tk


def clic(event):
    """met un pixel rouge lors du clic"""

    background.create_line(event.x, event.y, event.x + 1, event.y + 1, fill="red")

    pass


racine = tk.Tk()


background = tk.Canvas(
    racine, width="500", height="500", bg="black", relief='ridge',
    borderwidth=12)

racine.bind("<Button-1>", clic)

background.grid(column=0, row=0, rowspan=1)

racine.mainloop()
