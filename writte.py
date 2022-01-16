import pygame

def write(text, t_c, r_c, surfase):
    font = pygame.font.Font('assets/UI/AB.ttf', 20)
    text_coord = t_c
    string_rendered = font.render(text, True, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = r_c
    text_coord += intro_rect.height
    surfase.blit(string_rendered, intro_rect)
