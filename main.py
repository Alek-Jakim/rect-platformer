import pygame, sys
from pygame.locals import *
from settings import *
from scripts.button import Button
from scripts.player import Player
from scripts.enemy import Enemy
from scripts.tile import Tile
from assets.level.level_one import map_one, map_one_enemies, map_two
from scripts.portal import Portal
from scripts.level_manager import LevelManager


def import_map(map):
    for tile in map:
        Tile(tile_group, map[tile][0], map[tile][1], map[tile][2])


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def import_enemies(enemies):
    for enemy in enemies:
        Enemy(enemy_group, enemies[enemy][0], enemies[enemy][1])


class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Helium Planet")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 20)

        self.clicked = False

        self.level_manager = LevelManager(
            tile_group, player_group, enemy_group, map_one, map_one_enemies
        )

        self.level_manager.load_map()

        # self.setup()

    # def setup(self):
    #     self.player = Player(player_group, (100, 500))
    #     self.portal = Portal(portal_group, (WIN_WIDTH - 150, 30))

    #     import_map(map_one)
    #     import_enemies(map_one_enemies)

    def menu(self):
        while True:
            self.display_surface.fill((0, 0, 0))

            start_btn = Button(
                self,
                [0, 0, 200, 100],
                "red",
                [WIN_WIDTH / 2, WIN_HEIGHT / 2 - 100],
                "Start Game",
                "white",
            )

            mx, my = pygame.mouse.get_pos()

            if start_btn.btn_rect.collidepoint((mx, my)):
                if self.clicked:
                    self.game()

            start_btn.render(self.display_surface)

            self.clicked = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicked = True

            pygame.display.update()
            self.clock.tick(60)

    def game(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            player_group.update(dt)
            enemy_group.update(dt)
            laser_group.update(dt)
            tile_group.update()

            self.display_surface.fill((0, 0, 0))

            tile_group.draw(self.display_surface)
            laser_group.draw(self.display_surface)
            enemy_group.draw(self.display_surface)
            portal_group.draw(self.display_surface)
            player_group.draw(self.display_surface)
            player_group.sprite.draw_health_text(self.display_surface)

            pygame.display.update()


Game().menu()
