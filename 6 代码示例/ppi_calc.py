from tkinter import *
import tkinter.messagebox
from math import sqrt
import sys
tk = Tk()
tk.title("PPI Calc")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Width of screen (Pixel)")
L.grid(row=0, column=1)
E1 = Entry(tk)
E1.grid(row=1, column=0)
L1 = Label(tk, text="Height of screen (Pixel)")
L1.grid(row=1, column=1)
E2 = Entry(tk)
E2.grid(row=2, column=0)
L2 = Label(tk, text="Screen size (Inch)")
L2.grid(row=2, column=1)


def main():
    width = int(E.get())
    height = int(E1.get())
    size = float(E2.get())
    ppi = sqrt(width ** 2 + height ** 2)/size
    ppi = str(ppi)
    tkinter.messagebox.showwarning("Result", "PPI: " + ppi)


def _quit():
    tk.destroy()
    sys.exit()


B = Button(tk, text="Calc", command=main)
B.grid(row=3, column=0)
tk.protocol("WM_DELETE_WINDOW")
tk.mainloop()
