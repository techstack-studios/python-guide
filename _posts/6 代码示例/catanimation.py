import pygame
import sys
from pygame.locals import *
import random
from tkinter import *

mode = "fixed"
min_FPS = 40
max_FPS = 60

pygame.init()
fps_clock = pygame.time.Clock()


if mode == "random":
    FPS = random.randint(min_FPS, max_FPS)
if mode == "fixed":
    FPS = 60

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
font_obj = pygame.font.Font(None, 32)
cat_img = pygame.image.load("cat.png")
cat_x = 10
cat_y = 10
direction = "right"
count = 0
while True:
    if mode == "random":
        if count >= 10:
            FPS = random.randint(min_FPS, max_FPS)
            count = 0
        if count < 10:
            count += 1
    text_surface_obj = font_obj.render("FPS: " + str(FPS), True, GREEN, BLUE)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (200, 150)
    DISPLAYSURF.fill(WHITE)

    if direction == "right":
        cat_x += 5
        if cat_x == 280:
            direction = "down"
    if direction == "down":
        cat_y += 5
        if cat_y == 220:
            direction = "left"
    if direction == "left":
        cat_x -= 5
        if cat_x == 10:
            direction = "up"
    if direction == "up":
        cat_y -= 5
        if cat_y == 10:
            direction = "right"

    DISPLAYSURF.blit(cat_img, (cat_x, cat_y))
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps_clock.tick(FPS)

