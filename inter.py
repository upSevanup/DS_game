import time
from ui import UI
import random

class Game():
    def __init__(self, surface):
        # атрибуты игры
        self.hp_max = 100
        self.cur_hp = 100
        self.st_max = 100
        self.cur_st = 0
        self.st = 100
        self.souls = 10
        self.regen_st = 0.2
        self.regenf = 0.4

        # пользовательский интерфейс
        self.ui = UI(surface)

        if self.cur_hp == 0 and self.souls <= 5 and self.souls != 1:
            self.souls -= 1
            self.cur_hp = 100
        elif self.cur_hp == 0 and self.souls >= 5:
            self.souls -= random.randint(2, 4)
            self.cur_hp = 100

    def change_hp(self):
        self.cur_hp -= 1

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
        if self.cur_hp == 0 and self.souls <= 5 and self.souls != 1:
            self.souls -= 1
            self.cur_hp = 100
        elif self.cur_hp == 0 and self.souls >= 5:
            self.souls -= random.randint(2, 4)
            self.cur_hp = 100




