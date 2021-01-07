import tkinter as tk

x1 = 0
y1 = 0
c = 0


def clic1(event1):
    """met une ligne lors de 2 clic"""
    global x1
    global y1
    global c

    if event1.x > 262:
        d = "left"
    else:
        d = "right"
    if c == d:
        color = "blue"
    else:
        color = "red"

    background.create_line(x1, y1, event1.x, event1.y, fill=color)

    racine.bind("<Button-1>", clic)

    pass


def clic(event):
    """met une ligne lors de 2 clic"""
    global x1
    global y1
    global c

    x1 = event.x
    y1 = event.y


    if event.x > 262:
        c = "left"
    else:
        c = "right"

    racine.bind("<Button-1>", clic1)

    pass


racine = tk.Tk()

background = tk.Canvas(
    racine, width="500", height="500", bg="black", relief='ridge',
    borderwidth=12)

background.create_line(262, 512, 262, 12, fill="white")

racine.bind("<Button-1>", clic)

background.grid(column=0, row=0, rowspan=1)

racine.mainloop()
