import pygame, sys
from pygame.locals import *
from settings import *
from scripts.button import Button
from assets.level.level_one import level_one
from scripts.level_manager import LevelManager
from scripts.sounds import bg_sound, game_over_sound


def draw_text(text, font, color, surface):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(
        center=(surface.get_width() // 2, surface.get_height() // 2)
    )
    surface.blit(textobj, textrect)


class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Helium Planet")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 32)

        self.clicked = False
        self.game_over = False

        self.level_manager = LevelManager(level_one)

        bg_sound.set_volume(0.5)

        self.level_manager.load_map(4)

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
                    self.game_over = False
                    # self.level_manager.load_map()

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
        bg_sound.play(loops=-1)
        while running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if not self.game_over:
                player_group.update(dt, self.level_manager)
                enemy_group.update(dt)
                laser_group.update(dt)
                tile_group.update(dt)

                self.level_manager.portal_management(player_group.sprite)

                self.display_surface.fill((0, 0, 0))

                tile_group.draw(self.display_surface)
                laser_group.draw(self.display_surface)
                enemy_group.draw(self.display_surface)
                portal_group.draw(self.display_surface)
                player_group.draw(self.display_surface)

                if player_group.sprite:
                    player_group.sprite.draw_health_text(self.display_surface)
                else:
                    self.game_over = True
                    game_over_sound.play()
                    bg_sound.stop()
                    draw_text(
                        "You died! Press Escape to go back to the main menu.",
                        self.font,
                        "red",
                        self.display_surface,
                    )

            pygame.display.update()


Game().menu()
