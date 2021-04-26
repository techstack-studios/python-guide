import random
import threading
from Tkinter import *
import os
tk = Tk()
tk.title("Machine stress test")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Number of cores")
L.grid(row=0, column=1)
def func1():
    count = 0
    li = []
    while True:
        for a in range(1000000):
            for b in range(1000000):
                if(a > b):
                    li.append(random.randint(b,a))
                if(b > a):
                    li.append(random.randint(a,b))
                if(a == b):
                    li.append(random.choice([a,a,a,a,b,b,b,b]))
                if count >= 1000:
                    count = 0
                    li = []
                count += 1
def func2():
    count = 0
    num = 2
    while True:
        count += 1
        num = num ** 2
        if count >= 100:
            num = 2
            count = 0
def main():
    thread1 = threading.Thread(target=func1)
    thread1.start()
    thread2 = threading.Thread(target=func1)
    thread2.start()
    thread3 = threading.Thread(target=func1)
    thread3.start()
    thread4 = threading.Thread(target=func1)
    thread4.start()
    thread5 = threading.Thread(target=func2)
    thread5.start()
    thread6 = threading.Thread(target=func2)
    thread6.start()
    thread7 = threading.Thread(target=func2)
    thread7.start()
    thread8 = threading.Thread(target=func2)
    thread8.start()
    thread11 = threading.Thread(target=func1)
    thread11.start()
    thread21 = threading.Thread(target=func1)
    thread21.start()
    thread31 = threading.Thread(target=func1)
    thread31.start()
    thread41 = threading.Thread(target=func1)
    thread41.start()
    thread51 = threading.Thread(target=func2)
    thread51.start()
    thread61 = threading.Thread(target=func2)
    thread61.start()
    thread71 = threading.Thread(target=func2)
    thread71.start()
    thread81 = threading.Thread(target=func2)
    thread81.start()
def cmdst():
    command = ""
    for x in range(int(E.get())):
        command = command + "yes > /dev/null & "
    print command
    os.system(command)
B = Button(tk, text="Stress test with software function", command=main)
B.grid(row=1, column=0)
B1 = Button(tk, text="Stress test with macOS function", command=main)
B1.grid(row=1, column=1)
tk.mainloop()
