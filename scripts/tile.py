import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, color):
        super().__init__(groups)
        self.image = pygame.Surface(surf)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy()

    def update(self):
        self.old_rect = self.rect.copy()
