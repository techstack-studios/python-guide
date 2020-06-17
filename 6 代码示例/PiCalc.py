from random import random
from math import sqrt
import time
imported = False
try:
	from tqdm import tqdm
	imported = True
except ImportError:
	pass
if imported:
    start = time.time()
    darts = input("输入运行次数（直接敲回车使用默认）")
    if darts == "":
        darts = 1000000000
    if darts != "":
        darts = int(darts)
    hits = 0
    for x in tqdm(range(1, darts)):
        x, y = random(), random()
        dist = sqrt(x ** 2 + y ** 2)
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits / darts)
    print("PI: %s" % str(pi))
    print("Time Use:", str(time.time() - start))
if not imported:
    start = time.time()
    print("Started bench!!!")
    darts = 1000000000
    hits = 0
    for x in range(1, darts):
        x, y = random(), random()
        dist = sqrt(x ** 2 + y ** 2)
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits / darts)
    print("PI: %s" % str(pi))
    print("Time Use:", str(time.time() - start))
