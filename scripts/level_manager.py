from scripts.tile import Tile
from scripts.player import Player
from scripts.enemy import Enemy
from settings import *
from scripts.sounds import portal_sound


class LevelManager:
    def __init__(self, level):
        self.level = level
        self.level_index = 1

    def load_map_assets(self):
        for idx, asset in enumerate(self.level[self.level_index]):
            if idx == 0:
                for tile in asset:
                    if not tile == "player":
                        if len(asset[tile]) > 3:
                            Tile(
                                tile_group,
                                asset[tile][0],
                                asset[tile][1],
                                asset[tile][2],
                                asset[tile][3],
                                asset[tile][4],
                            )
                        else:
                            Tile(
                                tile_group,
                                asset[tile][0],
                                asset[tile][1],
                                asset[tile][2],
                            )
                    else:
                        if not player_group.sprite:
                            Player(player_group, asset[tile][0])
                        else:
                            player_group.sprite.pos.x = asset[tile][0][0]
                            player_group.sprite.pos.y = asset[tile][0][1]

            else:
                for enemy in asset:
                    Enemy(enemy_group, asset[enemy][0], asset[enemy][1])

    def load_map(self, level_index=1):
        tile_group.empty()
        enemy_group.empty()
        self.level_index = level_index
        self.load_map_assets()
