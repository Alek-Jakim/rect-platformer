from scripts.tile import Tile
from scripts.player import Player
from scripts.enemy import Enemy
from settings import *


class LevelManager:
    def __init__(self, level):
        self.level = level
        self.level_index = 1

    def load_map_assets(self):
        for idx, asset in enumerate(self.level[self.level_index]):
            if idx == 0:
                for tile in asset:
                    if not tile == "player":
                        Tile(
                            tile_group,
                            asset[tile][0],
                            asset[tile][1],
                            asset[tile][2],
                        )
                    else:
                        Player(player_group, asset[tile][0])
            else:
                for enemy in asset:
                    Enemy(enemy_group, asset[enemy][0], asset[enemy][1])

    def load_map(self):
        if not len(tile_group.sprites()) == 0:
            tile_group.empty()
        self.load_map_assets()

    def update_map(self, level_index):
        tile_group.empty()
        enemy_group.empty()
        self.level_index = level_index
        self.load_map_assets()

    def portal_management(self, player):
        for tile in tile_group.sprites():
            if player.rect.colliderect(tile.rect):
                if tile.color == "white":
                    key_pressed = pygame.key.get_just_pressed()
                    if key_pressed[pygame.K_o]:
                        self.update_map(self.level_index + 1)
