import pygame
import sys
import random
from pygame.locals import *

pygame.init()

width = 2048
height = 1152
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Drawing")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF.fill(WHITE)
# pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

color_li = [BLACK, WHITE, RED, GREEN, BLUE]
pixels = pygame.PixelArray(DISPLAYSURF)


def random_color():
    return random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)


def random_points():
    for _ in range(1000000):
        pixels[random.randint(0, width-1)][random.randint(0, height-1)] = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))


def points_summon1():
    x = 0
    y = 0
    while x < width and y < height:
        pixels[x][y] = random_color()
        x += 1
        y += 1


def points_summon2():
    x = 300
    y = 300
    for _ in range(5):
        for _ in range(500):
            pixels[x][y] = random_color()
            x += 1
        x -= 500
        y += 1
    y += 200
    for _ in range(5):
        for _ in range(500):
            pixels[x][y] = random_color()
            x += 1
        x -= 500
        y += 1
    y -= 205
    x += 250
    for _ in range(5):
        for _ in range(500):
            pixels[x][y] = random_color()
            y += 1
        y -= 500
        x += 1
    y += 200
    x -= 20
    y -= 20
    for _ in range(5):
        for _ in range(160):
            pixels[x][y] = random_color()
            x -= 1
            y -= 1
        x += 160
        y += 160
        y += 1
    x += 35
    y -= 5
    for _ in range(5):
        for _ in range(160):
            pixels[x][y] = random_color()
            x += 1
            y -= 1
        x -= 160
        y += 160
        y += 1


def points_summon3():
    x = 1000
    y = 300
    for _ in range(5):
        for _ in range(500):
            pixels[x][y] = random_color()
            x += 1
        x -= 500
        y += 1
    y += 200
    for _ in range(5):
        for _ in range(500):
            pixels[x][y] = random_color()
            x += 1
        x -= 500
        y += 1
    y -= 205
    x += 250
    for _ in range(5):
        for _ in range(500):
            pixels[x][y] = random_color()
            y += 1
        y -= 500
        x += 1
    y += 200
    x -= 20
    y -= 20
    for _ in range(5):
        for _ in range(160):
            pixels[x][y] = random_color()
            x -= 1
            y -= 1
        x += 160
        y += 160
        y += 1
    x += 35
    y -= 5
    for _ in range(5):
        for _ in range(160):
            pixels[x][y] = random_color()
            x += 1
            y -= 1
        x -= 160
        y += 160
        y += 1


points_summon2()
points_summon3()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
