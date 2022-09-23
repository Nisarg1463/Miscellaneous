import pygame
import random


class enemy:
    enemy_img = pygame.image.load('enemy.png')
    x_change = 5

    def __init__(self, x, y, heal):
        self.x = x
        self.y = y
        self.health = heal

    def show_enemy(self):
        win.blit(self.enemy_img, (self.x, self.y))
        if (self.x + self.x_change) < 0:
            self.x_change = 5
            self.y += 1
        if (self.x + self.x_change) > 736:
            self.x_change = -5
            self.y += 1
        self.x += self.x_change

    def collision_check(self, x, y):
        if ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5 < 50:
            return True


def show_score():
    global level, enemy_remaining, score
    win.blit(text.render(f"Score = {score}", True, (0, 255, 0)), (100, 0))
    win.blit(text.render(f'level = {level}', True, (0, 255, 0)), (300, 0))
    win.blit(text.render(f'enemy count = {enemy_remaining}', True, (0, 255, 0)), (500, 0))


pygame.init()

win = pygame.display.set_mode((800, 600))

background_img = pygame.image.load('background.jpg')

player_x = 378
player_y = 530
player_x_change = 0
player_img = pygame.image.load('character.png')

bullet = pygame.image.load('bullet.png')
bullet_x = player_x + 16
bullet_y = player_y
bullet_y_change = 1

text = pygame.font.Font('Sketch 3D.otf', 26)

enemy_count = 6
level = 1
score = 0
bullet_increase = 0
health = 5

run = True
while run:

    level_run = True

    enemies = []
    for i in range(enemy_count):
        enemies.append(enemy(random.randint(0, 736), random.randint(50, 150), health))

    enemy_remaining = enemy_count

    while level_run:
        win.fill((0, 0, 0))
        win.blit(background_img, (0, 0))
        win.blit(player_img, (player_x, player_y))
        win.blit(bullet, (bullet_x, bullet_y))

        for i in range(len(enemies)):
            enemies[i].show_enemy()

        for i in enemies:
            if i.collision_check(bullet_x, bullet_y):
                score += 100
                bullet_x = player_x
                bullet_y = player_y
                i.health -= 5
                if i.health <= 0:
                    enemy_remaining -= 1
                    enemies.remove(i)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                level_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                if event.key == pygame.K_b:
                    if score > 1000 and bullet_increase <= 5:
                        score -= 1000
                        bullet_y_change += 5
                        bullet_increase += 1
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    player_x_change = 0

        if 0 < (bullet_y - bullet_y_change):
            bullet_y -= bullet_y_change
        else:
            bullet_y = player_y
            bullet_x = player_x + 16

        if 736 > (player_x + player_x_change) > 0:
            player_x += player_x_change

        if len(enemies) == 0:
            level_run = False
            level += 1

        show_score()
        pygame.display.update()

    if level % 5 == 0:
        enemy_count += 1
        if level % 10 == 0:
            health += 5
