import pygame, sys
from pygame.locals import *
from settings import *
from assets.level.level_one import level_one
from scripts.level_manager import LevelManager
from scripts.game_state import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Helium Planet")

        self.clock = pygame.time.Clock()

        self.level_manager = LevelManager(level_one)

        # Game states
        self.game_state_manager = GameStateManager("menu")

        self.menu = Menu(
            self.screen, self.game_state_manager, self.clock, self.level_manager
        )
        self.level = Level(
            self.screen, self.game_state_manager, self.clock, self.level_manager
        )

        self.level_transition = LevelTransition(
            self.screen, self.game_state_manager, self.clock, self.level_manager
        )

        self.game_states = {
            "menu": self.menu,
            "level": self.level,
            "level_transition": self.level_transition,
        }

    def run(self):
        self.clock.tick(60)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state_manager.set_state("level")
                        running = False

            self.game_states[self.game_state_manager.get_state()].run()

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
