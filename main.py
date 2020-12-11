import pygame

from enemys.red_enemy import RedEnemy
from Constants import WIDTH, HEIGHT, BLACK, WHITE, BG_IMG, FONT, RED
from SpaceInvaders.Player import Player
from SpaceInvaders.level import Level
from SpaceInvaders.collision import Collision
import random

pygame.init()
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# classes
level = 1
enemys = [RedEnemy(level, WIN, 200, 0)]
spaceshuttle = Player(750, 70, 70, 6, WIN)

level_handler = Level()


def redraw_gamewindow(win):
    win.blit(BG_IMG, (0, 0))
    spaceshuttle.draw()
    for enemy in enemys:
        enemy.draw()

    font = pygame.font.SysFont("comicsans", 50, True)
    level_text = font.render(f"Level: {level}", True, WHITE)
    win.blit(level_text, (10, 30))

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    count = 0
    shoot_loop = 0

    while run:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        shoot_loop += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_LEFT] and spaceshuttle.x > spaceshuttle.vel:
            spaceshuttle.x -= spaceshuttle.vel
        elif keys[pygame.K_RIGHT] and spaceshuttle.x + spaceshuttle.vel + spaceshuttle.width < WIDTH:
            spaceshuttle.x += spaceshuttle.vel
        if keys[pygame.K_SPACE] and len(spaceshuttle.bullets) < 4:
            spaceshuttle.shoot(space=True)

        if shoot_loop % 100 == 0 and len(enemys) < 10 and count < 15:
            enemys.append(RedEnemy(level, WIN, random.randint(0, 600), 0))
            count += 1

        if len(enemys) == 0 and count == 15:
            spaceshuttle.victory()
            run = False

        # enemy
        for enemy in enemys:
            if enemy.health <= 0:
                enemys.remove(enemy)
            if enemy.y + enemy.height > 900:
                enemy.game_over()
                run = False
            enemy.shoot()
            enemy.move()
            if Collision().collide(spaceshuttle.x, spaceshuttle.y, enemy.x, enemy.y, spaceshuttle.get_player_mask(),
                                   enemy.get_enemy_mask()):
                enemy.game_over()
                run = False
            for bullet in enemy.bullets:
                if Collision().collide(spaceshuttle.x, spaceshuttle.y, bullet.x, bullet.y,
                                       spaceshuttle.get_player_mask(), enemy.get_bullet_mask()):
                    spaceshuttle.health -= 1
                    enemy.bullets.remove(bullet)

        # Player
        for bullet in spaceshuttle.bullets:
            for enemy in enemys:
                if Collision().collide(enemy.x, enemy.y, bullet.x - bullet.width // 2, bullet.y - bullet.height,
                                       enemy.get_enemy_mask(), bullet.get_player_bullet_mask()):
                    enemy.health -= 1
                    spaceshuttle.bullets.remove(bullet)

        spaceshuttle.shoot()
        redraw_gamewindow(WIN)
        pygame.display.update()
        if spaceshuttle.game_over():
            run = False
    pygame.quit()


main()
