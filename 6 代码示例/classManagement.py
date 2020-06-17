import datetime
import time
from tkinter import *
import tkinter.messagebox
import os

weekday = datetime.datetime.now().weekday()
breakstr = "课间休息啦！！！"
havelaunch = "吃午饭啦！！！"
classli = [[[8, 0, "英语"], [8, 40, breakstr], [8, 55, "地理"], [9, 35, breakstr], [9, 50, "体育"], [10, 30, breakstr],
            [10, 45, "语文"], [11, 25, havelaunch], [12, 30, "政治"], [13, 10, breakstr], [13, 25, "数学"],
            [14, 5, breakstr], [14, 20, "劳技"], [15, 0, breakstr],
            [15, 15, "random in 语数英"]]]  # TODO: Finish other lists!!!
count = 0
li = classli[weekday - 1]
warned = False
while True:
    print("Started running!")
    hour = li[count][0]
    minute = li[count][1]
    classname = li[count][2]
    print("Got!")
    now = datetime.datetime.now()
    checkernow = now.replace(hour=hour).replace(minute=minute)
    if now + datetime.timedelta(minutes=-2) < checkernow < now + datetime.timedelta(minutes=2):
        if not warned:
            # tkinter.messagebox.showwarning("Alert", classname)
            os.system("say %s" % classname)
            warned = True
    if now.minute > minute and now.hour >= hour:
        count += 1
        warned = False
    time.sleep(3)

