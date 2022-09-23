import pygame
import time

window = pygame.display.set_mode((800, 600))

# snake
snake_x = [390, 390]
snake_y = [530, 551]
snake_x_change = [0, 0]
snake_y_change = [-20, -20]
snake_length = 2
destination_x = [[], []]
destination_y = [[], []]

sec = time.time()
run = True
while run:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                for i in range(snake_length):
                    if snake_x_change[i] == 0:
                        snake_x_change[i] -= 20
                        snake_y_change[i] = 0

            if event.key == pygame.K_RIGHT:
                for i in range(snake_length):
                    if snake_x_change[i] == 0:
                        snake_x_change[i] += 20
                        snake_y_change[i] = 0

            if event.key == pygame.K_DOWN:
                for i in range(snake_length):
                    if snake_y_change[i] == 0:
                        snake_y_change[i] += 20
                        snake_x_change[i] = 0

            if event.key == pygame.K_UP:
                for i in range(snake_length):
                    if snake_y_change[i] == 0:
                        snake_y_change[i] -= 20
                        snake_x_change[i] = 0

    difference = time.time() - sec
    if difference >= 0.5:
        for i in range(snake_length):
            snake_y[i] += snake_y_change[i]
            snake_x[i] += snake_x_change[i]
            sec += difference
        if 0 >= snake_x[0] or snake_x[0] >= 800:
            run = False
        if 0 >= snake_y[0] or snake_y[0] >= 600:
            run = False

    for i in range(snake_length):
        pygame.draw.rect(window, (0, 255, 0), (snake_x[i], snake_y[i], 20, 20))

    pygame.display.update()
