import pygame
from pygame.math import Vector2
from settings import *


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos, shooting_direction):
        super().__init__(groups)

        self.image = pygame.Surface((20, 5))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=pos)

        self.pos = Vector2(self.rect.center)
        self.dir = Vector2()
        self.dir.x = -1 if shooting_direction == "left" else 1
        self.speed = 600

    def move(self, dt):
        self.pos.x += self.dir.x * dt * self.speed
        self.rect.x = round(self.pos.x)
        self.rect.y = round(self.pos.y)

    def collision(self):
        for tile in tile_group.sprites():
            if self.rect.colliderect(tile.rect):
                self.kill()

        for enemy in enemy_group.sprites():
            if self.rect.colliderect(enemy.rect):
                self.kill()
                enemy.take_damage()

    def update(self, dt):
        self.move(dt)
        self.collision()
