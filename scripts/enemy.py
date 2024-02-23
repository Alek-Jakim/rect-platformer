import pygame
from pygame.math import Vector2
from pygame.locals import *
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, pos, movement_range):
        super().__init__(groups)

        self.image = pygame.Surface((50, 75))
        self.image.fill("orange")
        self.starting_pos = pos[0]
        self.rect = self.image.get_rect(topright=pos)
        self.old_rect = self.rect.copy()

        self.frame_index = 0
        self.hurt_timer = None
        self.is_hurt = False

        # float based movement
        self.pos = Vector2(self.rect.topleft)
        self.dir = Vector2()
        self.dir.x = 1
        self.velocity = 200

        self.gravity = 0
        self.dir.y = 1
        self.total_movement = 0
        self.movement_range = movement_range

        self.health = 2

    def move(self, delta):

        self.pos.x += self.dir.x * self.velocity * delta
        self.rect.x = round(self.pos.x)

        self.pos.y += self.dir.y * self.gravity * delta
        self.rect.y = round(self.pos.y)
        self.tile_collision()

    def take_damage(self):
        self.health -= 1

        if self.health == 0:
            self.kill()
        else:
            self.is_hurt = True
            self.hurt_timer = pygame.time.get_ticks()

    def animate(self, delta):
        self.frame_index += 4 * delta

        if self.is_hurt:
            if int(self.frame_index) % 2 == 0:
                self.image.fill("white")
            else:
                self.image.fill("orange")

    def damage_timer(self):
        if self.is_hurt:
            current_time = pygame.time.get_ticks()

            if current_time - self.hurt_timer >= 3000:
                self.is_hurt = False
                self.image.fill("orange")

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
        self.animate(delta)
        self.damage_timer()
        self.move(delta)
        self.increase_gravity()
        self.lateral_movement()
