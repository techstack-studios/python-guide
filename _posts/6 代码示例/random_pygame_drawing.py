import pygame
import sys
import random
from pygame.locals import *

pygame.init()

width = 2048
height = 1152
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Drawing")

DISPLAYSURF.fill((255, 255, 255))

pixels = pygame.PixelArray(DISPLAYSURF)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_points():
    for _ in range(1000000):
        pixels[random.randint(0, width-1)][random.randint(0, height-1)] = random_color()


random_points()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
