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
game = Game(screen)
music = pygame.mixer.Sound('assets/music/secunda.mp3')
music.set_volume(0.3)
nachalo = pygame.mixer.Sound('assets/music/dragon.mp3')
nachalo.set_volume(0.3)
# BG
bg_lvl_1 = pygame.image.load('assets/BG/bg1.png')
# мб проще будет передавать в функцию сразу путь, чем кучу переменных делать но пока хз

def start_screen():
    new_game = ['START GAME']
    cn_exit = ['        EXIT']

    fon = pygame.image.load('assets/BG/menu_bg.jpg')
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('assets/UI/AB.ttf', 50)
    text_new_game = 500
    text_exit = 650
    x, y = 0, 0
    for line in new_game:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_new_game += 60
        intro_rect.top = text_new_game
        intro_rect.x = 650
        text_new_game += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in cn_exit:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_exit += 60
        intro_rect.top = text_exit
        intro_rect.x = 650
        text_exit += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    nachalo.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x + 620 < event.pos[0] < x + 1000 and y + 550 < event.pos[1] < y + 620:
                    nachalo.stop()
                    return
                if x + 740 < event.pos[0] < x + 850 and y + 700 < event.pos[1] < y + 780:
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()

def game_loop(bg):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == LVL_COMPITED:
                return 'C'
            if event.type == PLAYER_DEAD:
                return 'D'

        screen.blit(bg, (0, 0))
        lvl.run()
        game.run()

        pygame.display.update()
        clock.tick(60)

# игра
start_screen()
level_map = load_level('lvls/lvl_1.map')
lvl = Lvl(level_map, screen)
check = game_loop(bg_lvl_1)
# проверка работоспособности
print("That's right! I win!!!")