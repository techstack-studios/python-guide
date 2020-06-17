import random
while True:
    while True:
        try:
            drop_times = int(input("Input drop times:"))
            break
        except ValueError:
            print("Error with input!")
    front = 0
    back = 0
    for x in range(drop_times):
        die = random.randint(0, 1)
        if die == 0:
            back += 1
        if die == 1:
            front += 1
    total = front + back
    print("Front Count: %s, Back Count: %s, Front Percent: %s, Back Percent: %s" % (str(front), str(back), str(front / total * 100) + "%", str(back / total * 100) + "%"))
    ask = input("Do you want to drop the die again?(Y/N)").upper()
    if ask == "N":
        break