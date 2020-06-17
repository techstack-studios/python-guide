import time
import os
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import pickle
import sys
import win32com.client
import turtle


blocked_software_list = []
enable_temp_software_list = []
launched = False
blocked_software_list_filename = "file_list.dll"
blocked_software_password_filename = "password.dll"
if os.path.isdir("D:"):
    home_path = "D:/Software_Lock_Home"
    try:
        os.mkdir(home_path)
        os.chdir(home_path)
    except FileExistsError:
        os.chdir(home_path)
elif os.path.isdir("C:"):
    home_path = "C:/Software_Lock_Home"
    try:
        os.mkdir(home_path)
        os.chdir(home_path)
    except FileExistsError:
        os.chdir(home_path)
    except:
        tkinter.messagebox.showerror("Software Lock", "Please quit application and re-run using Administrator.")
        sys.exit()


def get_all_process_name():
    all_running_process = []
    wmi = win32com.client.GetObject('winmgmts:')
    for p in wmi.InstancesOf('win32_process'):
        all_running_process.append(p.Name)
        children = wmi.ExecQuery('Select * from win32_process where ParentProcessId=%s' % p.Properties_('ProcessId'))
        for child in children:
            all_running_process.append(p.Name)
    return all_running_process


def file_exist_check():
    global launched
    try:
        file_opr = open(blocked_software_list_filename, "rb+")
        file_opr.read()
        file_opr.close()
        launched = True
    except FileNotFoundError:
        launched = False


file_exist_check()
print("Check file exist!")


if not launched:
    tk = Tk()
    tk.title("Configure Password And List")
    E = Entry(tk, show="*")
    E.grid(row=0, column=0)
    L = Label(tk, text="Password")
    L.grid(row=0, column=1)
    T = Text(tk, width=40, height=40)
    T.grid(row=1, column=0)


    def add_to_software_list():
        global blocked_software_list
        filename = tkinter.filedialog.askopenfilename(title="Add a software to blocked software list", type=[("Executable File", "*.exe")])
        blocked_software_list.append(filename)
        print(blocked_software_list)
        T.delete("0.0", "end")
        text = ""
        for each in blocked_software_list:
            text = text + each + ", "
        T.insert(INSERT, text)
        tkinter.messagebox.showwarning("Locker", "Added!")


    def save_software_list():
        file = open(blocked_software_list_filename, "wb+")
        pickle.dump(blocked_software_list, file)
        file.close()
        print("saved!")
        tkinter.messagebox.showwarning("Locker", "Saved!")


    def save_password():
        print(os.getcwd())
        with open(blocked_software_password_filename, "w+") as obj:
            obj.write(E.get())
        tkinter.messagebox.showwarning("Locker", "Saved!")


    def _quit():
        tk.destroy()
        sys.exit()


    B = Button(tk, text="Add to list", command=add_to_software_list)
    B.grid(row=2, column=0)
    B1 = Button(tk, text="Save this as file", command=save_software_list)
    B1.grid(row=2, column=1)
    B2 = Button(tk, text="Save password as file", command=save_password)
    B2.grid(row=2, column=2)
    tk.protocol("WM_DELETE_WINDOW", _quit)
    tk.mainloop()


if launched:
    print(os.getcwd())
    with open(blocked_software_password_filename, "r") as obj:
        password = obj.read()
    cmd = tkinter.messagebox.askyesno("Launch!" ,"What are you going to do?\nRun the locker - Yes\nConfigure the Locker - No")
    if not cmd:
        tk = Tk()
        tk.title("Configure Password And List")
        E = Entry(tk, textvariable=password, show="*")
        E.grid(row=0, column=0)
        L = Label(tk, text="Password")
        L.grid(row=0, column=1)
        T = Text(tk, width=40, height=40)
        T.grid(row=1, column=0)


        def add_to_software_list():
            global blocked_software_list
            filename = tkinter.filedialog.askopenfilename(title="Add a software to blocked software list",
                                                          type=[("Executable File", "*.exe")])
            blocked_software_list.append(filename)
            T.delete("0.0", "end")
            text = ""
            for each in blocked_software_list:
                text = text + each + ", "
            T.insert(INSERT, text)
            tkinter.messagebox.showwarning("Locker", "Added!")


        def save_software_list():
            file = open(blocked_software_list_filename, "wb+")
            pickle.dump(blocked_software_list, file)
            file.close()
            tkinter.messagebox.showwarning("Locker", "Saved!")


        def save_password():
            with open(blocked_software_password_filename, "w+") as obj:
                obj.write(E.get())
            tkinter.messagebox.showwarning("Locker", "Saved!")


        def _quit():
            tk.destroy()
            sys.exit()


        B = Button(tk, text="Add to list", command=add_to_software_list)
        B.grid(row=2, column=0)
        B1 = Button(tk, text="Save this as file", command=save_software_list)
        B1.grid(row=2, column=1)
        tk.protocol("WM_DELETE_WINDOW", _quit)
        tk.mainloop()
    if cmd:
        file_opr = open(blocked_software_list_filename, "rb")
        blocked_software_list = pickle.load(file_opr)
        file_opr.close()
        print("got into main while!")
        while True:
            running_list = get_all_process_name()
            if running_list:
                print("got running process!")
            for each in running_list:
                print(blocked_software_list)
                for block_software_name in blocked_software_list:
                    if each in block_software_name:
                        if each not in enable_temp_software_list:
                            print("Try to kill!")
                            os.system("taskkill /IM %s /F" % each)
                            """
                            tkk = Tk()
                            tkk.title("Input Password To Use It")
                            E = Entry(tkk)
                            E.grid(row=0, column=0)
                            L = Label(tk, text="Input Password")
                            L.grid(row=0, column=1)
    
                            def check_pwd():
                                if E.get() == password:
                                    global enable_temp_software_list
                                    enable_temp_software_list.append(each)
                                tkk.destroy()
    
    
                            B = Button(tk, text="Check Password", command=check_pwd)
                            B.grid(row=1, column=0)
                            tkk.mainloop()
                            """
                            pwd = turtle.textinput("Input Password To Use It", "Password: ")
                            if pwd == password:
                                enable_temp_software_list.append(each)

            time.sleep(10)


            





