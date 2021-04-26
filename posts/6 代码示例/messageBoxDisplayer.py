from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Message Box Display")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Message Box Title")
L.grid(row=0, column=1)
E1 = Entry(tk)
E1.grid(row=1, column=0)
L1 = Label(tk, text="Message Box Body")
L1.grid(row=1, column=1)
E2 = Entry(tk)
E2.grid(row=2, column=0)
L2 = Label(tk, text="Message Box Type")
L2.grid(row=2, column=1)


def main_act():
    title = E.get()
    body = E1.get()
    Type = E2.get()
    if Type == "showerror":
        tkinter.messagebox.showerror(title, body)
    if Type == "showwarning":
        tkinter.messagebox.showwarning(title, body)
    if Type == "showinfo":
        tkinter.messagebox.showinfo(title, body)


B = Button(tk, text="Start", command=main_act)
B.grid(row=3, column=0)
tk.mainloop()