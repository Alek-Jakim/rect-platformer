import pygame, sys
from pygame.locals import *
from settings import *
from scripts.button import Button
from scripts.sounds import bg_sound, game_over_sound
from scripts.game_state import *


class Scene:
    def __init__(self, screen, game_state_manager, clock, level_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager
        self.clock = clock
        self.level_manager = level_manager

    def run(self):
        pass


class Level(Scene):
    def __init__(self, screen, game_state_manager, clock, level_manager):
        super().__init__(screen, game_state_manager, clock, level_manager)

        self.font = pygame.font.Font(None, 40)

        self.level_manager.load_map()

        self.running = True

    def set_running(self, running):
        self.running = running

    def run(self):
        bg_sound.play(loops=-1)
        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_state_manager.set_state("menu")
                        self.running = False

            if not self.game_state_manager.get_game_over():
                player_group.update(dt)
                enemy_group.update(dt)
                laser_group.update(dt)
                tile_group.update(dt)

                self.level_manager.portal_management(
                    player_group.sprite, self.game_state_manager, self
                )

                self.screen.fill((0, 0, 0))

                tile_group.draw(self.screen)
                laser_group.draw(self.screen)
                enemy_group.draw(self.screen)
                portal_group.draw(self.screen)
                player_group.draw(self.screen)

                if player_group.sprite:
                    player_group.sprite.draw_health_text(self.screen)
                else:
                    self.game_state_manager.set_game_over(True)
                    game_over_sound.play()
                    bg_sound.stop()
                    draw_text(
                        "You died! Press Escape to go back to the main menu.",
                        self.font,
                        "red",
                        self.screen,
                    )

                pygame.display.update()


class Menu(Scene):
    def __init__(self, screen, game_state_manager, clock, level_manager):
        super().__init__(screen, game_state_manager, clock, level_manager)

        self.clicked = False

    def run(self):
        running = True
        bg_sound.stop()
        while running:
            self.screen.fill((0, 0, 0))

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
                    self.game_state_manager.set_state("level")
                    self.game_state_manager.set_game_over(False)
                    self.level_manager.load_map(4)
                    running = False

            start_btn.render(self.screen)

            self.clicked = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicked = True

            pygame.display.update()
            self.clock.tick(60)


class LevelTransition(Scene):
    def __init__(self, screen, game_state_manager, clock, level_manager):
        super().__init__(screen, game_state_manager, clock, level_manager)

        self.level_transition_font = pygame.font.Font(None, 40)

    def run(self):
        running = True
        self.clock.tick(60)
        bg_sound.stop()
        while running:
            self.screen.fill((0, 0, 0))

            draw_text(
                "Level one finished! Press Escape to go back to the main menu",
                self.level_transition_font,
                "white",
                self.screen,
            )

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_state_manager.set_state("menu")
                        running = False

            pygame.display.update()
            self.clock.tick(60)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state
        self.game_over = False

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state

    def get_game_over(self):
        return self.game_over

    def set_game_over(self, game_over):
        self.game_over = game_over
