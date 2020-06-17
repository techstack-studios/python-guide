from tkinter import *
import tkinter.messagebox
import sys
import random

title = "Article Summon"

tk = Tk()
tk.title(title)
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Input title of article.")
L.grid(row=0, column=1)
L1 = Label(tk, text="Output:")
L1.grid(row=1, column=0)
T = Text(tk, width=50, height=30)
T.grid(row=2, column=0)


def _quit():
    cmd = tkinter.messagebox.askyesno(title, "Are you sure you want to quit?")
    if cmd:
        tk.destroy()
        sys.exit()


def summon():
    text = ""
    a_title = E.get()
    man_list = "王塑，王小波，苏童，阿城，刘震云，三毛，张爱玲，金庸，冰心，钱钟书，杨绛".split("，")
    great_sentence_list = [
        "我的天空里没有太阳，总是%s，但并不暗，因为有东西代替了太阳。虽然没有太阳那么明亮，但对我来说已经足够。凭借着这份光，我便能把%s当成白天。我从来就没有太阳，所以不怕失去。" % (a_title, a_title),
        "世上有两样东西不可直视，一是%s，二是人心。 " % a_title, "究竟爱一个人，可以到什么程度？究竟什么样的邂逅，可以舍命不悔？逻辑的尽头不是理性和秩序的理想国，而是我用生命奉献的爱情！",
        "一天中，太阳会升起，同时还会落下。人生也一样，有%s和黑夜，只是不会像太阳那样，有定时的日出和日落。有些人一辈子都活在太阳的照耀下，也有些人不得不一直活在漆黑的深夜里。人害怕的，就是本来一直存在的太阳落下不再升起，也就是非常害怕原本照在身上的光芒消失。 " % a_title,
        "曾经拥有的%s被夺走，并不代表就会回到原来没有那种%s的时候。" % (a_title, a_title), "这个世上没有无用的%s，也只有%s本身能决定自己的用途。" % (a_title, a_title),
        "夕阳在西边的天空渐渐散开。那下面巨大的高楼大厦鳞次栉比，不仅如此，它们周边还伫立着大大小小的建筑物。这就是怀有过野心和希望的人建造的街道。但是，现实当中，累得精疲力尽的%s只是在这些建筑物的缝隙之间匍匐打转地苟且偷生而已。而%s，也只是其中的一个。" % (
            a_title, a_title),
        "那些%s的脆弱自尊，轻易不得触碰，那极有有可能成为对%s一生的打扰。我们都曾经历那样纯粹、易碎的青春，只是时光的磨砺已让我们懂得逃避与忍气吞声然后慢慢遗忘%s曾经的青春。" % (
            a_title, a_title, a_title),
        "我们只能走在幻夜的路上，即使四周明亮如白昼，那也仅是假象。就算与%s共度的每个夜晚都是幻夜，我也愿为你化身为影，至死不渝！" % a_title,
        "我们这种%s在面对胜负关键时，总需要找寻某种倚靠，但，在比赛中乃是孤独的，无法倚靠任何人，那么，该倚靠什么呢？我想，只有自己曾经努力过的事实。 " % a_title,
        '%s应该不虚度一生，应该能够说：“%s已经做了我能做的事。”' % (a_title, a_title),
        "从不浪费时间的%s没有工夫抱怨时间不够。" % a_title,
        "没有%s不爱惜他的生命，但很少%s珍视他的时间。" % (a_title, a_title),
        "生命最长久的%s并不是活得时间最多的%s。" % (a_title, a_title),
        "%s在碰到底处时才会释放活力。" % a_title,
        "真正的%s，只有在经过艰难卓绝的斗争之后才能实现。" % a_title,
        "真正的%s无论从正反看都应一样，不可能从前面看是蔷薇而从后面看是刺。" % a_title
    ]
    connect_sentence = ["因此，", "我想，", "经过了长时间的思考，", "很快，", "我们可以得知，", "经过缜密的分析，", "从中不难看出，"]
    if_sentence = ["因为", "所以"]
    speak_sentence = ["曾说：", "说过："]
    define_sentence = ["%s是很重要的", "%s往往能够取得决定性的作用", "%s是一种美好的东西", "%s是一种奇幻的存在", "%s可以说是最美好的东西", "%s使得我们的生活发生了改变", "%s的美妙程度，不是大家所能想象的", "%s能够使得我们的生活更美好", "%s是谷歌内部的一种管理方式", "%s给世界经济带来了不好的影响", "%s极大的影响了美国股市", "%s使得一些产业遭受重创"]
    for x in range(100):
        choice = random.choice(["man", "great", "connect"])
        if choice == "man":
            text = text + random.choice(man_list) + random.choice(speak_sentence) + random.choice(
                great_sentence_list)
        if choice == "great":
            text = text + random.choice(great_sentence_list)
        if choice == "connect":
            text = text + random.choice(connect_sentence) + random.choice(define_sentence) % a_title + "。"
    T.delete("0.0", "end")
    T.insert(INSERT, text)


B = Button(tk, text="Start", command=summon)
B.grid(row=3, column=0)
tk.protocol("WM_DELETE_WINDOW", _quit)
tk.mainloop()
