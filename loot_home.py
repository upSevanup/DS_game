import pygame

class Home(pygame.sprite.Sprite):
    def __init__(self, pos, surface, is_key=False):
        super().__init__()
        self.image = pygame.Surface((200, 180))
        self.image.fill((150, 75, 0))
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - 100))

        self.is_key = is_key
        self.player_near = False
        self.pos = pos
        self.screen = surface

    def get_input(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_e] and self.player_near:
            self.write('search E')
        if keys[pygame.K_e] and self.player_near:
            if self.is_key:
                self.write('key found')
                return True
            else:
                self.write('empty')

    def write(self, text):
        font = pygame.font.Font('assets/UI/AB.ttf', 20)
        text_coord = self.rect.y + 70
        string_rendered = font.render(text, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = self.rect.x + 60
        text_coord += intro_rect.height
        self.screen.blit(string_rendered, intro_rect)

    def update(self, x_shift):
        self.rect.x += x_shift
