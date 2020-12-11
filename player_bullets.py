import pygame
from Constants import GREEN, BULLET_SPACESHUTTLE_IMG


class PlayerBullets:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 11
        self.radius = 5
        self.width = 30
        self.height = 28

    def draw(self, win):
        win.blit(BULLET_SPACESHUTTLE_IMG, (self.x - self.width // 2, self.y - self.height))

    def get_player_bullet_mask(self):
        return pygame.mask.from_surface(BULLET_SPACESHUTTLE_IMG)
