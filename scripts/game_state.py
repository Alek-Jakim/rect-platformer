import pygame, sys
from pygame.locals import *
from settings import *
from scripts.button import Button
from scripts.sounds import bg_sound, game_over_sound, portal_sound
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

    def portal_management(self):
        new_level_index = self.level_index + 1
        if player_group.sprite:
            for tile in tile_group.sprites():
                key_pressed = pygame.key.get_just_pressed()
                if player_group.sprite.rect.colliderect(tile.rect):
                    if tile.color == "white":
                        if key_pressed[pygame.K_o] and new_level_index <= len(
                            self.level
                        ):
                            self.load_map(new_level_index)
                            portal_sound.play()

                    if tile.color == "purple":
                        if key_pressed[pygame.K_o]:
                            self.game_state_manager.set_state("level_transition")
                            running = False

    def run(self):
        bg_sound.play(loops=-1)
        bg_sound.set_volume(0.1)
        running = True
        while running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_state_manager.set_state("menu")
                        running = False

            if not self.game_state_manager.get_game_over():
                player_group.update(dt)
                enemy_group.update(dt)
                laser_group.update(dt)
                tile_group.update(dt)

                new_level_index = self.level_manager.level_index + 1
                if player_group.sprite:
                    for tile in tile_group.sprites():
                        key_pressed = pygame.key.get_just_pressed()
                        if player_group.sprite.rect.colliderect(tile.rect):
                            if tile.color == "white":
                                if key_pressed[pygame.K_o] and new_level_index <= len(
                                    self.level_manager.level
                                ):
                                    self.level_manager.load_map(new_level_index)
                                    portal_sound.play()

                            if tile.color == "purple":
                                if key_pressed[pygame.K_o]:
                                    self.game_state_manager.set_state(
                                        "level_transition"
                                    )
                                    running = False

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
                    self.level_manager.load_map()
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

            self.clock.tick(60)

            pygame.display.update()


class LevelTransition(Scene):
    def __init__(self, screen, game_state_manager, clock, level_manager):
        super().__init__(screen, game_state_manager, clock, level_manager)

        self.level_transition_font = pygame.font.Font(None, 40)

    def run(self):
        running = True
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

            self.clock.tick(60)

            pygame.display.update()


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
