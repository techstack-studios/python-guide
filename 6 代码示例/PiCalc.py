from random import random #导入random随机库
from math import sqrt #导入sqrt开跟函数
import time #导入time时间库
imported = False #tqdm是否被导入了
try: #尝试导入tqdm库
	from tqdm import tqdm #导入tqdm
    #假如没有报错，运行下面的代码：
	imported = True #标记tqdm成功导入
except ImportError: #如果导入失败（没有tqdm库）
	pass #什么都不做
if imported: #如果导入tqdm了
    start = time.time() #获取获取时间戳
    darts = input("输入运行次数（直接敲回车使用默认）") 
    if darts == "":
        darts = 1000000000 
    if darts != "": 
        darts = int(darts) #将字符串编程整型
    hits = 0
    for x in tqdm(range(1, darts)): #循环darts次
        x, y = random(), random() #随机两个数x和y
        dist = sqrt(x ** 2 + y ** 2) #dist=根号（x的二次方+x的二次方）
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits / darts)
    print("PI: %s" % str(pi))
    print("Time Use:", str(time.time() - start))
else:
    start = time.time() #获取获取时间戳
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
