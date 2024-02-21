import pygame


class Portal(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((80, 120))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
