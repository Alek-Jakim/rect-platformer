import pygame


class Button:
    def __init__(self, game, btn_size, btn_color, btn_pos, text, text_color):
        self.btn_rect = pygame.Rect(*btn_size)
        self.btn_rect.centerx = btn_pos[0]
        self.btn_rect.centery = btn_pos[1]

        self.btn_color = btn_color
        self.game = game

        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(text, True, text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.btn_rect.center

    def render(self, surface):
        pygame.draw.rect(surface, self.btn_color, self.btn_rect)
        surface.blit(self.text, self.text_rect)
