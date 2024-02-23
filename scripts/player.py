import pygame
from pygame.math import Vector2
from pygame.locals import *
from settings import *
from scripts.laser import Laser


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

        # shooting
        self.is_shooting = False
        self.facing_dir = self.dir.x
        self.shoot_timer = None

        # take damage
        self.health = 3
        self.font = pygame.font.Font(None, 42)
        self.health_text = self.font.render(f"Health: {self.health}/3", True, "white")
        self.health_text_rect = self.health_text.get_rect()
        self.health_text_rect.topleft = (100, 20)

        self.frame_index = 0
        self.hurt_timer = None
        self.is_hurt = False

    def input(self):
        keys = pygame.key.get_pressed()
        key_press = pygame.key.get_just_pressed()

        if keys[K_a]:
            self.dir.x = -1
            self.facing_dir = "left"
        elif keys[K_d]:
            self.dir.x = 1
            self.facing_dir = "right"
        else:
            self.dir.x = 0

        if key_press[K_p] and not self.is_shooting:
            self.shoot_timer = pygame.time.get_ticks()
            self.is_shooting = True
            Laser(laser_group, (self.pos.x, self.pos.y), self.facing_dir)

        if key_press[K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.gravity = -900

    def damage_timer(self):
        if self.is_hurt:
            current_time = pygame.time.get_ticks()

            if current_time - self.hurt_timer >= 3000:
                self.is_hurt = False
                self.image.fill("green")

    def take_damage(self):
        if not self.is_hurt:
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
                self.image.fill("green")

    def move(self, delta):

        self.pos.x += self.dir.x * self.velocity * delta
        self.rect.x = round(self.pos.x)
        self.tile_collision("horizontal")

        self.pos.y += self.dir.y * self.gravity * delta
        self.rect.y = round(self.pos.y)
        self.tile_collision("vertical")

    def laser_timer(self):
        if self.is_shooting:
            current_time = pygame.time.get_ticks()

            if current_time - self.shoot_timer >= 1000:
                self.is_shooting = False

    def tile_collision(self, direction):
        for tile in tile_group.sprites():
            if self.rect.colliderect(tile.rect) and not tile.color == "white":
                if direction == "horizontal":
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
                else:
                    if (
                        self.rect.bottom >= tile.rect.top
                        and self.old_rect.bottom <= tile.old_rect.top
                    ):
                        self.rect.bottom = tile.rect.top
                        self.gravity = 0
                        self.is_jumping = False

                    self.pos.y = self.rect.y

    def enemy_collision(self):
        for enemy in enemy_group.sprites():
            if self.rect.colliderect(enemy.rect):
                self.take_damage()

    def increase_gravity(self):
        self.gravity += 30

    def draw_health_text(self, surface):
        self.health_text = self.font.render(f"Health: {self.health}/3", True, "white")
        surface.blit(self.health_text, self.health_text_rect)

    def update(self, delta, level_manager):
        self.old_rect = self.rect.copy()
        self.input()
        self.animate(delta)
        self.damage_timer()
        self.move(delta)
        self.increase_gravity()
        self.laser_timer()
        self.enemy_collision()
