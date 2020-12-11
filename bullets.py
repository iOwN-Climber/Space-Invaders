import pygame


class Bullet:
    def __init__(self, win, x, y, image, vel):
        self.win = win
        self.y = y
        self.x = x
        self.image = image
        self.vel = vel

    def move(self):
        self. y += self.vel

    def draw(self):
        self.win.blit(self.image, (self.x, self.y))


