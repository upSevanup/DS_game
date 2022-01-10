import pygame
import sys
import random
import time
from map import *
from lvl import Lvl
from ui import UI

class Game:
    def __init__(self):
        # атрибуты игры
        self.hp_max = 100
        self.cur_hp = 0
        self.st_max = 100
        self.cur_st = 0
        self.st = 100
        self.souls = 3

        # пользовательский интерфейс
        self.ui = UI(screen)

    def run(self):
        self.ui.show_heal(self.cur_hp, self.hp_max)
        self.ui.show_stam(self.cur_st, self.st_max)
        self.ui.show_soul(self.souls)

        if self.cur_st < 100:
            self.cur_st += 0.2
            time.sleep(0.001)
        if self.cur_st > 100:
            izl = self.cur_st - self.st_max
            self.cur_st -= izl

        if self.cur_hp == 0 and self.souls <= 5 and self.souls != 1:
            self.souls -= 1
            self.cur_hp = 100
        elif self.cur_hp == 0 and self.souls >= 5:
            self.souls -= random.randint(2, 4)
            self.cur_hp = 100

# создание окна
pygame.init()
pygame.display.set_caption('ECLIPSE: Curse of the Dark Sun')
size = (size_width, size_height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
lvl = Lvl(level_map, screen)
game = Game()

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
        string_rendered = font.render(line, 1, pygame.Color('white'))
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

    screen.fill('cyan')
    lvl.run()
    game.run()

    pygame.display.update()
    clock.tick(60)
