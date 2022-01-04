import pygame
import sys
from map import *
from lvl import Lvl

# создание окна
pygame.init()
pygame.display.set_caption('Dark Souls 4.0')
size = (size_width, size_height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
lvl = Lvl(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('cyan')
    lvl.run()

    pygame.display.update()
    clock.tick(60)
