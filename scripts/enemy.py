import pygame
from pygame.math import Vector2
from pygame.locals import *
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, pos, movement_range):
        super().__init__(groups)

        self.image = pygame.Surface((50, 50))
        self.image.fill("orange")
        self.starting_pos = pos[0]
        self.rect = self.image.get_rect(topright=pos)
        self.old_rect = self.rect.copy()

        # float based movement
        self.pos = Vector2(self.rect.topleft)
        self.dir = Vector2()
        self.dir.x = 1
        self.velocity = 50

        self.gravity = 0
        self.dir.y = 1
        self.total_movement = 0
        self.movement_range = movement_range

    def move(self, delta):

        self.pos.x += self.dir.x * self.velocity * delta
        self.rect.x = round(self.pos.x)

        self.pos.y += self.dir.y * self.gravity * delta
        self.rect.y = round(self.pos.y)
        self.tile_collision()

    def lateral_movement(self):
        if self.total_movement >= self.movement_range:
            if self.dir.x == 1:
                self.dir.x = -1
            else:
                self.dir.x = 1
            self.total_movement = 0

        self.total_movement += 1

    def tile_collision(self):
        for tile in tile_group.sprites():
            if self.rect.colliderect(tile.rect):
                if (
                    self.rect.left <= tile.rect.right
                    and self.old_rect.left >= tile.old_rect.right
                ):
                    self.rect.left = tile.rect.right
                if (
                    self.rect.right >= tile.rect.left
                    and self.old_rect.right <= tile.old_rect.left
                ):
                    self.rect.right = tile.rect.left

                self.pos.x = self.rect.x

                if (
                    self.rect.bottom >= tile.rect.top
                    and self.old_rect.bottom <= tile.old_rect.top
                ):
                    self.rect.bottom = tile.rect.top
                    self.gravity = 0
                    self.is_jumping = False

                self.pos.y = self.rect.y

    def increase_gravity(self):
        self.gravity += 30

    def update(self, delta):
        self.old_rect = self.rect.copy()
        self.move(delta)
        self.increase_gravity()
        self.lateral_movement()
