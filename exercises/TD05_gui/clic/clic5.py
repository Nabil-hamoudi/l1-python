import tkinter as tk

c = []
b = 1

def clic(event):
    """fais clignoter le carré"""
    global c
    global b

    if b < 9:
        a = background.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, outline="red")
        c.append(a)

    elif b == 9:
        a = background.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, outline="yellow")
        c.append(a)

    else:
        for i in c:
            background.delete(i)

    b += 1

    pass


racine = tk.Tk()

background = tk.Canvas(
    racine, width="500", height="500", bg="black", relief="ridge",
    borderwidth=12)

racine.bind("<Button-1>", clic)

background.grid(column=0, row=0, rowspan=1)

racine.mainloop()
