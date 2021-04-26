import os
import sys
import pickle
from subprocess import call

open_sound = True
# OS call debug enabled.
os_debug = True
voicedb = ""
foreverat = os.getcwd()


def can_be_save(local_path, filename):
    for name in os.listdir(local_path):
        if name == filename:
            return False
    return True


def say(text):
    if open_sound:
        # Check OS debug.
        if not os_debug:
            call(["say", text])
        if os_debug:
            os.system("say -v %s %s" % ("Kate", text))
    if not open_sound:
        pass




while True:
    rightlist = []
    wronglist = []
    words = {}
    cmd = input(
        "Which mode do you want to choice?\nW - Write Mode\nT - Test Mode\nS - Spell Check Mode\nL - Listening Mode\nC - Check Filename\nO - Open a file and check inside.\n").upper()

    if cmd == "W":                  # Write Mode
        while True:
            try:
                wordEn = input("Input English of this word: ")
                if wordEn == "EXIT":
                    cmd = input("Are you sure you want to EXIT?(Y/N)").upper()
                    if cmd == "Y":
                        break
                wordZh = input("Input Chinese of this word: ")
                if wordEn == "EXIT" or wordZh == "EXIT":
                    cmd = input("Are you sure you want to EXIT?(Y/N)").upper()
                    if cmd == "Y":
                        break
                print("")
                words[wordEn] = wordZh
            except KeyboardInterrupt:
                break
        asker = input("Do you want to save this?(Y/N)").upper()
        if asker == "Y":            # Test Mode
            while True:
                try:
                    path = input("Input path:")
                    if path != "":
                        os.chdir(path)
                    if path == "":
                        os.chdir("/Users/rice/Desktop/All/Normal_User/大米的工作站/学习/English/FCE/Words_file/FCEs") # if is "" go to homedir
                    break
                except:
                    print("Error with path!\nPlease re-input!\n")
            print("Now Working At:", os.getcwd())
            cmd = input("Go on(Y/N)").upper()
            if cmd == "N":
                sys.exit()
            if cmd == "Y":
                pass
            while True:
                filename = input("Input filename: ")
                if can_be_save(os.getcwd(), filename):
                    writefile = open(filename, "wb+")
                    pickle.dump(words, writefile)
                    writefile.close()
                    break
                if not can_be_save(os.getcwd(), filename):
                    print("Cannot be save!")
        if asker == "N":
            sys.exit()
    if cmd == "T":                  # Test Mode
        print("Please read the file first.")
        filename = input("Input filename: ").replace(" ", "")
        if "/" not in filename:
            filename = "/Users/rice/Desktop/All/Normal_User/大米的工作站/学习/English/FCE/Words_file/FCEs/" + filename # Check path input, if is "" go to homedir
        try:
            loadfile = open(filename, "rb")
            words = pickle.load(loadfile)
            loadfile.close()
        except FileNotFoundError:
            try:
                loadfile = open(filename, "rb")
                words = pickle.load(loadfile)
                loadfile.close()
            except FileNotFoundError:
                print("File not found!")
        except PermissionError:
            print("Not allowed read this file.")
        except:
            print("Unknown Error!")
        score = 0
        for name in words.keys():
            wordEn = name
            wordZh = words[wordEn]
            print(wordEn)
            try:
                say(wordEn)
            except:
                pass
            inputWordZh = input("Input Chinese of this word: ")
            if inputWordZh != "":
                if inputWordZh == wordZh or inputWordZh in wordZh:
                    score += 1
                    rightlist.append(inputWordZh)
                    print("You are right.")
                    print("")

                elif inputWordZh != wordZh:
                    wronglist.append(inputWordZh)
                    print("There are some wrong.")
                    print("")

            if inputWordZh == "":
                textwillappend = wordZh + "_IS_EMPTY"
                wronglist.append(textwillappend)
                print("There are some wrong.")
                print("")

        questions = len(words)
        ticks = score
        wrongs = questions - score
        if ticks / questions * 100 == int(ticks / questions * 100):
            ticks_percent = str(int(ticks / questions * 100)) + "%"
        if ticks / questions * 100 != int(ticks / questions * 100):
            ticks_percent = str(ticks / questions * 100) + "%"
        if wrongs / questions * 100 == int(wrongs / questions * 100):
            wrongs_percent = str(int(wrongs / questions * 100)) + "%"
        if wrongs / questions * 100 != int(wrongs / questions * 100):
            wrongs_percent = str(wrongs / questions * 100) + "%"
        print("Questions:", questions, "Ticks:", score, "Wrongs:", wrongs, "\nTicks percent:", ticks_percent,
              "\nWrongs percent:", wrongs_percent)
        print("Wrong List:")
        print(wronglist)
        print("Right List:")
        print(rightlist)
    if cmd == "S":
        filename = input("Input filename:")
        try:
            loadfile = open(filename, "rb")
            words = pickle.load(loadfile)
            loadfile.close()
        except FileNotFoundError:
            print("File Not Found.")
        except PermissionError:
            print("Not allowed read this file.")
        except:
            print("Unknown Error!")
        score = 0
        for name in words.keys():
            wordEn = name
            wordZh = words[wordEn]
            print(wordZh)
            try:
                say(wordEn)
            except:
                pass
            inputWordEn = input("Input English of this word: ")
            if inputWordEn != "":
                if inputWordEn == wordEn:
                    score += 1
                    rightlist.append(inputWordEn)
                    print("You are right.")
                    print("")

                elif inputWordEn != wordEn:
                    wronglist.append(inputWordEn)
                    print("There are some wrong.")
                    print("")

            if inputWordEn == "":
                textwillappend = wordEn + "_IS_EMPTY"
                wronglist.append(textwillappend)
                print("There are some wrong.")
                print("")

        print("Questions:", str(len(words)), "Ticks:", str(score), "Wrongs:", str(len(words) - score))
        print("Wrong List:")
        print(wronglist)
        print("Right List:")
        print(rightlist)
    if cmd == "L":
        filename = input("Input filename:")
        try:
            loadfile = open(filename, "rb")
            words = pickle.load(loadfile)
            loadfile.close()
        except FileNotFoundError:
            print("File Not Found.")
        except PermissionError:
            print("Not allowed read this file.")
        except:
            print("Unknown Error!")
        score = 0
        for name in words.keys():
            wordEn = name
            try:
                while True:
                    print(wordEn)
                    print(words[wordEn])
                    print("")
                    say(wordEn)
                    command = input("Repeat?(Y/N/clear)\n")
                    if command == "N":
                        break
                    if command == "clear":
                        os.system("clear")
            except:
                print("This is executable binary edition.\nCannot use this.\n")
                break
    if cmd == "O":
        filename = input("Filename: ")
        try:
            readfile = open(filename, "rb")
            words = pickle.load(readfile)
            readfile.close()
            for key in words.keys():
                print(key, words[key])
        except PermissionError:
            print("Permission Error!")
        except FileNotFoundError:
            print("File Not Found!")
        except:
            print("Unknown Error!")
    if cmd == "C":
        while True:
            path = input("Input path:")
            try:
                os.chdir(path)
                break
            except:
                print("Error with the path you want to find!")
        filename = input("Filename:")
        found = False
        for each in os.listdir(os.getcwd()):
            if each == filename:
                print("File find.")
                found = True
        if not found:
            print("File not found.")
    cmd1 = input("Stay in software?(Y/N)").upper()
    cmd2 = input("Clear?(Y/N)").upper()
    if cmd2 == "Y":
        os.system("clear")
    if cmd1 == "N":
        break
