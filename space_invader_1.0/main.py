import pygame
import random
import math


def player(x, y):
    win.blit(character, (x, y))


def enemy(enemy_characters, x, y):
    win.blit(enemy_characters, (x, y))


def bullet(x, y):
    global bullet_img
    win.blit(bullet_img, (x + 16, y + 16))


def enemy_bullet(x, y):
    global bullet_img
    win.blit(bullet_img, (x + 16, y + 16))


def collision_check_enemy(b_x, b_y, e_x, e_y):
    global enemy_x, enemy_y, score, bullet_x, bullet_y, player_y, player_x
    if 50 >= math.sqrt(math.pow(b_x - e_x, 2) + math.pow(b_y - e_y, 2)) and b_x - e_x <= 0:
        enemy_x[i] = random.randint(0, 578)
        enemy_y[i] = random.randint(50, 150)
        bullet_y = player_y
        bullet_x = bullet_x
        score += 1


def collision_check_player(b_x, b_y, e_x, e_y):
    global player_x, player_y, death, number_of_enemy, enemy_bullet_x, enemy_bullet_y, enemy_x, enemy_y
    if 32 >= math.sqrt(math.pow(b_x - e_x, 2) + math.pow(b_y - e_y, 2)):
        player_x = 378
        player_y = 478
        death += 1
        for j in range(number_of_enemy):
            enemy_bullet_x[j] = enemy_x[j]
            enemy_bullet_y[j] = enemy_y[j]


def show_score(x, y):
    global score, death
    score_shown = font.render(f"score : {score}", True, (0, 0, 255))
    death_shown = font.render(f'death : {death}', True, (0, 0, 255))
    win.blit(score_shown, (x, y))
    win.blit(death_shown, (x, y+32))


pygame.init()

background = pygame.image.load('background.jpg')

win = pygame.display.set_mode((800, 600))

pygame.display.set_caption('space invaders')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# score
score = 0
death = 0
font = pygame.font.Font('Sketch 3D.otf', 32)
text_x = 10
text_y = 10

# player
player_x = 378
player_y = 478
player_x_change = 0
player_y_change = 0
character = pygame.image.load('character.png')

# enemy
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_character = []
number_of_enemy = 6
for i in range(number_of_enemy):
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(2)
    enemy_character.append(pygame.image.load('enemy.png'))

# bullet
bullet_x = 0
bullet_y = 0
bullet_y_change = 10
bullet_img = pygame.image.load('bullet.png')

# enemy bullet
enemy_bullet_x = []
enemy_bullet_y = []
enemy_bullet_y_change = 5
enemy_bullet_img = pygame.image.load('enemy_bullet.png')
for i in range(number_of_enemy):
    enemy_bullet_x.append(enemy_x[i])
    enemy_bullet_y.append(enemy_y[i])

run = True
while run:
    # RGB = RED GREEN BLUE
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))

    if death >= 3:
        run = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # player movement
    total_x = player_x + player_x_change
    if 736 >= total_x >= 0:
        player_x += player_x_change

    # enemy movement
    for i in range(number_of_enemy):
        total_x = enemy_x[i] + enemy_x_change[i]
        if 0 >= total_x:
            enemy_x_change[i] = 4
            enemy_y[i] += 5
        elif 736 <= total_x:
            enemy_x_change[i] = -4
            enemy_y[i] += 5
        enemy_x[i] += enemy_x_change[i]
        collision_check_enemy(bullet_x, bullet_y, enemy_x[i], enemy_y[i])
        collision_check_player(enemy_bullet_x[i], enemy_bullet_y[i], player_x, player_y)
        enemy(enemy_character[i], enemy_x[i], enemy_y[i])

        # enemy bullet movement
        if 800 <= enemy_bullet_y[i]:
            enemy_bullet_y[i] = enemy_y[i]
            enemy_bullet_x[i] = enemy_x[i]
        enemy_bullet(enemy_bullet_x[i], enemy_bullet_y[i])
        enemy_bullet_y[i] += enemy_bullet_y_change

    # bullet movement
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_x = player_x
    bullet(bullet_x, bullet_y)
    bullet_y -= 100

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
print(score)