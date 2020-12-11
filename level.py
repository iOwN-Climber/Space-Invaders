import pygame


class Level:

    def __init__(self):
        pass

    def levl1(self):
        # return tuple
        # wie viele enemy in dem level
        # wie viele rote
        # wie viele grüne usw
        # vllt eine liste mit reihenfolge der gegner [grün, rot, grün, gelb]
        pass

    def level2(self):
        pass

    def handle_level(self, level):
        if level == 1:
            return self.levl1()

        elif level == 2:
            return self.level2()
