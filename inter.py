import pygame
from ui import UI
import random
from map import pl_d

class Game():
    def __init__(self, surface):
        # атрибуты игры
        self.hp_max = 100
        self.cur_hp = 100
        self.st_max = 100
        self.cur_st = 0
        self.souls = 10
        self.regen_st = 0.2
        self.regenf = 0.4
        self.regen_hp = 0.05

        # пользовательский интерфейс
        self.ui = UI(surface)

    def change_hp(self):
        self.cur_hp -= 0.8

    def regen(self):
        if self.cur_st <= 100 and self.cur_st > 0:
            self.cur_st -= self.regenf
            self.regen_st = 0
        else:
            self.regen_st = 0.2

    def run(self):
        if self.cur_st < 100:
            self.cur_st += self.regen_st
        if self.cur_st > 100:
            izl = self.cur_st - self.st_max
            self.cur_st -= izl
        if self.cur_hp > 0 and self.cur_hp < 1 and self.souls <= 3 and self.souls != 0:
            self.souls -= 1
            self.cur_hp = 100
        elif self.cur_hp > 0 and self.cur_hp < 1 and self.souls >= 3:
            self.souls -= random.randint(1, 2)
            self.cur_hp = 100
        if self.cur_hp < 100:
            self.cur_hp += self.regen_hp
        if self.cur_st > 100:
            izl1 = self.cur_hp - self.hp_max
            self.cur_hp -= izl1
        if self.souls == 0:
            pygame.event.post(pl_d)
