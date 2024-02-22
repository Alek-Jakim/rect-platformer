import pygame
from settings import *
from scripts.tile import Tile


class Portal(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((80, 120))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)

    def change_map(self, map):
        for tile in tile_group.sprites():
            tile.kill()
        for tile in map:
            Tile(tile_group, map[tile][0], map[tile][1], map[tile][2])

    def update(self, player, map):
        if self.rect.colliderect(player.rect):
            key_pressed = pygame.key.get_just_pressed()
            if key_pressed[pygame.K_o]:
                self.change_map(map)
