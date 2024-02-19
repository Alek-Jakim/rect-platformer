import pygame
from pygame.math import Vector2
from pygame.locals import *
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.Surface((25, 75))
        self.image.fill("green")
        self.rect = self.image.get_rect(topright=pos)
        self.old_rect = self.rect.copy()

        # float based movement
        self.pos = Vector2(self.rect.topleft)
        self.dir = Vector2()

        self.velocity = 400
        self.gravity = 0
        self.dir.y = 1
        self.is_jumping = False

    def input(self):
        keys = pygame.key.get_pressed()
        jump_key = pygame.key.get_just_pressed()

        if keys[K_a]:
            self.dir.x = -1
        elif keys[K_d]:
            self.dir.x = 1
        else:
            self.dir.x = 0

        if jump_key[K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.gravity = -1900

    def move(self, delta):

        self.pos.x += self.dir.x * self.velocity * delta
        self.rect.x = round(self.pos.x)

        self.pos.y += self.dir.y * self.gravity * delta
        self.rect.y = round(self.pos.y)
        self.floor_collision()

    def floor_collision(self):
        for tile in tile_group.sprites():
            if self.rect.colliderect(tile.rect):
                if (
                    self.rect.bottom >= tile.rect.top
                    and self.old_rect.bottom <= tile.old_rect.top
                ):
                    self.rect.bottom = tile.rect.top
                    self.gravity = 0
                    self.is_jumping = False

                self.pos.y = self.rect.y
            else:
                self.gravity += 30

    def update(self, delta):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(delta)
        print(self.gravity)
