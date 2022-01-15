import pygame
import sys
from map import *
from lvl import Lvl
from inter import Game

# создание окна
pygame.init()
pygame.display.set_caption('ECLIPSE: Curse of the Dark Sun')
size = (size_width, size_height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
lvl = Lvl(level_map, screen)
game = Game(screen)
bg = pygame.image.load('assets/BG/bg.png')

def start_screen():
    intro_text = [
        'START GAME',
        '  CONTINUE',
        '        EXIT']

    fon = pygame.image.load('assets/BG/menu_bg.jpg')
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('assets/UI/AB.ttf', 50)
    text_coord = 500
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 60
        intro_rect.top = text_coord
        intro_rect.x = 650
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


start_screen()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(bg, (0, 0))
    lvl.run()
    game.run()

    pygame.display.update()
    clock.tick(60)