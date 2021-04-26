import random
import threading
import os
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
cmd = raw_input("Which mode do you like to use?\n1 - Use system built in stress test\n2 - Use software stress test\n")
if cmd == "2":
    main()
if cmd == "1":
    command = ""
    cores = input("Input number of threads:")
    for x in range(cores):
        command = command + str("yes > /dev/null & ")
    print "Use killall yes to stop stress test."
    os.system(command)