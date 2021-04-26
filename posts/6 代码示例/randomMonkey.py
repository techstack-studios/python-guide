import random
import time
mode = input("File - Y, Sentences - N ").upper()
if mode == "N":
    sentences = input("Input a sentences or a word: ").lower()
if mode == "Y":
    filename = input("Filename: ")
    with open(filename, "r") as obj:
        sentences = obj.read().lower()
sentences = sentences.replace("?","").replace(" ","").replace("!", "").replace(".", "").replace(",", "").replace("/", "").replace("'","")
letters = list("abcdefghijklmnopqrstuvwxyz")
length = len(sentences)
count = 0
start = time.time()
while True:
    text = ""
    for x in range(length):
        text = text + random.choice(letters)
    print(text)
    count += 1
    if text == sentences:
        break
timeUse = time.time() - start
print("Oh Yeah You Got It!!! Used", count, "Times")
print("Time usage", timeUse, "Second")
