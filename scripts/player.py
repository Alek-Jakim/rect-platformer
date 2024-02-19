import pygame
from pygame.math import Vector2
from pygame.locals import *


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
        self.entity_gravity = 0
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
            self.entity_gravity = -900

    def move(self, delta, floor_rect, old_floor_rect):

        self.pos.x += self.dir.x * self.velocity * delta
        self.rect.x = round(self.pos.x)

        self.pos.y += self.dir.y * self.entity_gravity * delta
        self.rect.y = round(self.pos.y)
        self.floor_collision(floor_rect, old_floor_rect)

    def floor_collision(self, floor_rect, old_floor_rect):
        if self.rect.colliderect(floor_rect):

            if (
                self.rect.bottom >= floor_rect.top
                and self.old_rect.bottom <= old_floor_rect.top
            ):
                self.rect.bottom = floor_rect.top
                self.entity_gravity = 0
                self.is_jumping = False

            self.pos.y = self.rect.y
        else:
            self.entity_gravity += 30

    def update(self, delta, floor_rect, old_floor_rect):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(delta, floor_rect, old_floor_rect)
