import pygame

from Constants import WIDTH, RED, DARKGREEN, SPACESHUTTLE_IMG, FONT, HEIGHT

from SpaceInvaders.player_bullets import PlayerBullets


class Player:
    def __init__(self, y, width, height, vel, win):
        self.y = y
        self.x = WIDTH // 2 - width // 2
        self.height = height
        self.width = width
        self.vel = vel
        self.shootloop = 0
        self.bullets = []
        self.win = win
        self.reloading_time = 30
        self.health = 10
        self.maximum_health = 10

    def draw(self):
        self.win.blit(SPACESHUTTLE_IMG, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(self.win)
            bullet.y -= bullet.vel
            if bullet.y < 0:
                self.bullets.remove(bullet)

        pygame.draw.rect(self.win, RED, (self.x, self.y + self.height + 10, self.width, 10))
        pygame.draw.rect(self.win, DARKGREEN,
                         (self.x, self.y + self.height + 10, round(self.width / self.maximum_health) * self.health, 10))

    def shoot(self, space=False):
        if space and self.shootloop == 0:
            self.create_bullet()
            self.shootloop = 1
        elif self.shootloop != 0:
            self.shootloop += 1
            if self.shootloop > self.reloading_time:
                self.shootloop = 0

    def create_bullet(self):
        self.bullets.append(PlayerBullets(self.x + self.width // 2, self.y))

    def get_player_mask(self):
        return pygame.mask.from_surface(SPACESHUTTLE_IMG)

    def game_over(self):
        if self.health <= 0:
            victory = FONT.render("Game Over", True, RED)
            self.win.blit(victory, (WIDTH // 2 - victory.get_width() // 2, HEIGHT // 2 - victory.get_height()))
            pygame.display.update()
            pygame.time.delay(2000)
            return True

    def victory(self):
        victory = FONT.render("Victory", True, RED)
        self.win.blit(victory, (WIDTH // 2 - victory.get_width() // 2, HEIGHT // 2 - victory.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)


