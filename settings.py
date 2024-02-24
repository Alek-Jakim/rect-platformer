import os, pygame


root_path = os.path.dirname(__file__).replace("\\", "/")
WIN_WIDTH, WIN_HEIGHT = 1280, 720


player_group = pygame.sprite.GroupSingle()
tile_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()


def draw_text(text, font, color, surface):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(
        center=(surface.get_width() // 2, surface.get_height() // 2)
    )
    surface.blit(textobj, textrect)
