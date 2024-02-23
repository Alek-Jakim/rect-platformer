import pygame
from pygame.math import Vector2


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, color, moving=False, range=0):
        super().__init__(groups)
        self.image = pygame.Surface(surf)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy()

        self.moving = moving
        self.movement_range = range
        self.total_movement = 0
        self.pos = Vector2(self.rect.topleft)
        self.dir = Vector2()
        self.dir.x = -1
        self.speed = 200

    def move(self, delta):
        if self.moving:
            self.pos.x += self.dir.x * delta * self.speed
            self.rect.x = round(self.pos.x)

    def lateral_movement(self):
        if self.moving:
            if self.total_movement >= self.movement_range:
                if self.dir.x == 1:
                    self.dir.x = -1
                else:
                    self.dir.x = 1
                self.total_movement = 0

            self.total_movement += 1

    def update(self, delta):
        self.old_rect = self.rect.copy()
        self.move(delta)
        self.lateral_movement()
