import tkinter as tk

c = 0
b = 0

def clic(event):
    """fais clignoter le carré"""
    global c
    global a
    global b

    if c == 10:
        racine.destroy()
    elif c%2 == 0:
        a = background.create_rectangle(112, 112, 412, 412, fill="red")
    else:
        background.delete(a)
        b = background.create_rectangle(112, 112, 412, 412, outline="red")
    c += 1

    pass


racine = tk.Tk()

background = tk.Canvas(
    racine, width="500", height="500", bg="black", relief="ridge",
    borderwidth=12)

a = background.create_rectangle(112, 112, 412, 412, outline="red")

racine.bind("<Button-1>", clic)

background.grid(column=0, row=0, rowspan=1)

racine.mainloop()
