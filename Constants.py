import pygame

pygame.init()
# game variables
WIDTH = 700
HEIGHT = 900
FONT = pygame.font.SysFont("comicsans", 100)


# assets
BG_IMG = pygame.image.load("assets/bg.png")
RED_ENEMY_IMG = pygame.image.load("assets/red_enemy.png")
BULLET_IMG = pygame.image.load("assets/bullet.png")
SPACESHUTTLE_IMG = pygame.image.load("assets/Spaceshuttle.png")
BULLET_SPACESHUTTLE_IMG = pygame.image.load("assets/bullet_player.png")


# colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREEN = (0, 150, 0)