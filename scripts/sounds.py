from settings import root_path
import pygame

pygame.mixer.init()


laser_sound = pygame.mixer.Sound(root_path + "/assets/sound/laser.mp3")
hit_sound = pygame.mixer.Sound(root_path + "/assets/sound/hit.mp3")
portal_sound = pygame.mixer.Sound(root_path + "/assets/sound/teleport.mp3")
