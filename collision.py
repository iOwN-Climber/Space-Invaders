import pygame


class Collision:

    def __init__(self):
        pass

    def collide(self, x, y, x2, y2, mask, mask2):
        x_offset = x2 - x
        y_offset = y2 - y
        return mask.overlap(mask2, (x_offset, y_offset))