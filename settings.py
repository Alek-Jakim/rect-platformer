import os, pygame


root_path = os.path.dirname(__file__).replace("\\", "/")
WIN_WIDTH, WIN_HEIGHT = 1280, 720


player_group = pygame.sprite.GroupSingle()
tile_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
