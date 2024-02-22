from scripts.tile import Tile
from scripts.player import Player
from scripts.enemy import Enemy
from settings import enemy_group


class LevelManager:
    def __init__(self, tile_group, player_group, enemy_group, map, enemies):
        self.level = 1

        self.map = map
        self.enemies = enemies
        self.tile_group = tile_group
        self.player_group = player_group
        self.enemy_group = enemy_group

    def load_map_assets(self):
        for key, _ in self.map.items():
            if not key == "player":
                Tile(
                    self.tile_group,
                    self.map[key][0],
                    self.map[key][1],
                    self.map[key][2],
                )
            if key == "player":
                Player(self.player_group, self.map[key][0])
        for enemy in self.enemies:
            Enemy(enemy_group, self.enemies[enemy][0], self.enemies[enemy][1])

    def load_map(self):
        if not len(self.tile_group.sprites()) == 0:
            self.tile_group.empty()
        self.load_map_assets()

    def update_map(self, new_map):
        self.tile_group.empty()
        self.map = new_map
        self.load_map_assets()
