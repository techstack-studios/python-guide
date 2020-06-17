from tkinter import *
import tkinter.messagebox
import webbrowser
import sys

gbps = 0
title = "Display Gbps Calc"
ok_msg = "%s OK!"
not_enough_msg = "%s is not enough!"

tk = Tk()
tk.title(title)
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Resolution Width")
L.grid(row=0, column=1)
E1 = Entry(tk)
E1.grid(row=1, column=0)
L1 = Label(tk, text="Resolution Height")
L1.grid(row=1, column=1)
E2 = Entry(tk)
E2.grid(row=2, column=0)
L2 = Label(tk, text="Color Number (RGB: 3)")
L2.grid(row=2, column=1)
E3 = Entry(tk)
E3.grid(row=3, column=0)
L3 = Label(tk, text="Color Depth")
L3.grid(row=3, column=1)
E4 = Entry(tk)
E4.grid(row=4, column=0)
L4 = Label(tk, text="Refresh Rate")
L4.grid(row=4, column=1)


def get_gbps():
    global gbps
    width = float(E.get())
    height = float(E1.get())
    color_number = float(E2.get())
    color_depth = float(E3.get())
    refresh_rate = float(E4.get())
    gbps = width * height * color_number * color_depth * refresh_rate / 1000000000


def show_gbps():
    get_gbps()
    tkinter.messagebox.showwarning(title, "Gbps Required: %s" % str(gbps))


def hdmi14_ok():
    if gbps <= 10.8:
        tkinter.messagebox.showwarning(title, ok_msg % "HDMI1.4")
    if gbps > 10.8:
        tkinter.messagebox.showwarning(title, not_enough_msg % "HDMI1.4")


def hdmi20_ok():
    if gbps <= 18:
        tkinter.messagebox.showwarning(title, ok_msg % "HDMI2.0")
    if gbps > 18:
        tkinter.messagebox.showwarning(title, not_enough_msg % "HDMI2.0")


def hdmi21_ok():
    if gbps <= 48:
        tkinter.messagebox.showwarning(title, ok_msg % "HDMI2.1")
    if gbps> 48:
        tkinter.messagebox.showwarning(title, not_enough_msg % "HDMI2.1")


def dp12_ok():
    if gbps <= 21.6:
        tkinter.messagebox.showwarning(title, ok_msg % "Display Port 1.2")
    if gbps > 21.6:
        tkinter.messagebox.showwarning(title, not_enough_msg % "Display Port 1.2")


def dp14_ok():
    if gbps <= 32.4:
        tkinter.messagebox.showwarning(title, ok_msg % "Display Port 1.4")
    if gbps > 32.4:
        tkinter.messagebox.showwarning(title, not_enough_msg % "Display Port 1.4")


def dp15_ok():
    if gbps <= 40:
        tkinter.messagebox.showwarning(title, ok_msg % "Display Port 1.5" + " NOTE: NOT RELEASED")
    if gbps > 40:
        tkinter.messagebox.showwarning(title, not_enough_msg % "Display Port 1.5" + " NOTE: NOT RELEASED")


def thunderbolt2_ok():
    if gbps <= 20:
        tkinter.messagebox.showwarning(title, ok_msg % "ThunderBolt 2")
    if gbps > 20:
        tkinter.messagebox.showwarning(title, not_enough_msg % "ThunderBolt 2")


def thunderbolt3_ok():
    if gbps <= 40:
        tkinter.messagebox.showwarning(title, ok_msg % "ThunderBolt 3")
    if gbps > 40:
        tkinter.messagebox.showwarning(title, not_enough_msg % "ThunderBolt 3")


def go_to_shop():
    webbrowser.open("https://search.jd.com/Search?keyword=" + E5.get() + "&enc=utf-8&wq=xian%20shi%20qi&pvid=5149f302a4bf46a0a26a8982a34b1ecf")


def _quit():
    cmd = tkinter.messagebox.askyesno(title, "Are you sure you want to quit?")
    if cmd:
        tk.destroy()
        sys.exit()


B = Button(tk, text="Show Gbps", command=show_gbps)
B.grid(row=5, column=0)
B1 = Button(tk, text="Check HDMI1.4", command=hdmi14_ok)
B1.grid(row=6, column=0)
B2 = Button(tk, text="Check HDMI2.0", command=hdmi20_ok)
B2.grid(row=7, column=0)
B3 = Button(tk, text="Check HDMI2.1", command=hdmi21_ok)
B3.grid(row=8, column=0)
B4 = Button(tk, text="Check Display Port 1.2", command=dp12_ok)
B4.grid(row=9, column=0)
B5 = Button(tk, text="Check Display Port 1.4", command=dp14_ok)
B5.grid(row=10, column=0)
B6 = Button(tk, text="Check Display Port 1.5", command=dp15_ok)
B6.grid(row=11, column=0)
B7 = Button(tk, text="Check ThunderBolt 2", command=thunderbolt2_ok)
B7.grid(row=12, column=0)
B8 = Button(tk, text="Check ThunderBolt 3", command=thunderbolt3_ok)
B8.grid(row=13, column=0)
E5 = Entry(tk)
E5.grid(row=14, column=0)
L5 = Label(tk, text="Display Name")
L5.grid(row=14, column=1)
B9 = Button(tk, text="Go To Shopping Mall", command=go_to_shop)
B9.grid(row=15, column=0)
tk.protocol("WM_DELETE_WINDOW", _quit)
tk.mainloop()
