import pygame, sys
from pygame.locals import *
from scripts.button import Button
from settings import *
from scripts.player import Player


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Helium Planet")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 20)

        self.player_group = pygame.sprite.GroupSingle()

        self.floor = pygame.Surface((WIN_WIDTH, 75))
        self.floor.fill("red")
        self.floor_rect = self.floor.get_rect(topleft=(0, WIN_HEIGHT - 75))
        self.old_floor_rect = self.floor_rect.copy()

        self.clicked = False

        self.setup()

    def setup(self):
        self.player = Player(self.player_group, (100, 100))

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

            self.player_group.update(dt, self.floor_rect, self.old_floor_rect)

            self.display_surface.fill((0, 0, 0))

            self.display_surface.blit(self.floor, self.floor_rect)

            self.player_group.draw(self.display_surface)

            pygame.display.update()


Game().menu()
