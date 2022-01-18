import pygame


class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.bar_max_width = 192
        self.bar_height = 10

        # хп
        self.heal_bar = pygame.image.load("assets/UI/healandmanabar.png")
        self.heal_bar_top = (26, 19)

        # стамина
        self.st_bar = pygame.image.load("assets/UI/healandmanabar.png")
        self.st_bar_top = (26, 49)

        # души
        self.soul = pygame.image.load("assets/UI/soul.png")
        self.soul_rect = self.soul.get_rect(topleft=(70, 70))
        self.font = pygame.font.Font('assets/UI/AB.ttf', 50)

    # отображение полоски хп
    def show_heal(self, current, full):
        self.display_surface.blit(self.heal_bar, (20, 10))
        cur_heal_rat = current / full
        cur_bar_width = self.bar_max_width * cur_heal_rat
        heal_bar_rect = pygame.Rect(self.heal_bar_top, (cur_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, '#dc4949', heal_bar_rect)

    # отображение полоски стамины
    def show_stam(self, curren, ful):
        self.display_surface.blit(self.st_bar, (20, 40))
        cur_st_rat = curren / ful
        cur_bar_width1 = self.bar_max_width * cur_st_rat
        st_bar_rect = pygame.Rect(self.st_bar_top, (cur_bar_width1, self.bar_height))
        pygame.draw.rect(self.display_surface, 'blue', st_bar_rect)

    # отображение количества душ
    def show_soul(self, amout):
        self.display_surface.blit(self.soul, (20, 70))
        soul_am_surf = self.font.render(str(amout), False, 'white')
        soul_am_rect = soul_am_surf.get_rect(midleft=(self.soul_rect.right + 4, self.soul_rect.centery))
        self.display_surface.blit(soul_am_surf, soul_am_rect)
