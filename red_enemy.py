import pygame
from Constants import RED_ENEMY_IMG, BULLET_IMG, GREEN, RED, FONT, HEIGHT, WIDTH
from enemys.bullets import Bullet


class RedEnemy:
    WIDTH = 30
    HEIGHT = 40
    VEL = 1

    def __init__(self, level, win, x, y):
        self.level = level
        self.win = win
        self.y = y
        self.x = x

        self.shootloop = 0
        self.bullets = []
        self.reloading_time = 130
        self.health = 3
        self.health_maximum = 3
        self.height = RED_ENEMY_IMG.get_height()

    def healthbar(self):
        img_width = RED_ENEMY_IMG.get_width()
        pygame.draw.rect(self.win, RED, (self.x, self.y - 10, img_width, 10))
        pygame.draw.rect(self.win, GREEN, (self.x, self.y - 10, round(img_width / self.health_maximum * self.health), 10))
        self.get_hit()

    def move(self):
        self.y += self.VEL

    def get_hit(self):
        pass

    def get_bullet_mask(self):
        return pygame.mask.from_surface(BULLET_IMG)

    def get_enemy_mask(self):
        return pygame.mask.from_surface(RED_ENEMY_IMG)

    def shoot(self):
        if self.shootloop == 0:
            self.bullets.append(Bullet(self.win, self.x + 30, self.y + 50, BULLET_IMG, 3))
            self.shootloop = 1
        else:
            self.shootloop += 1
            if self.shootloop > self.reloading_time:
                self.shootloop = 0

    def draw(self):
        self.win.blit(RED_ENEMY_IMG, (self.x, self.y))

        for bullet in self.bullets:
            bullet.draw()
            bullet.move()
            if bullet.y > HEIGHT:
                self.bullets.remove(bullet)
        self.healthbar()

    def game_over(self):
        victory = FONT.render("Game Over", True, RED)
        self.win.blit(victory, (WIDTH // 2 - victory.get_width() // 2, HEIGHT // 2 - victory.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)

