import pygame
import time


def snake_movement(ls, s_x, s_y, j):
    global destination, snake_x_change, snake_y_change
    axis, change, x, y = ls
    if s_x == x and s_y == y:
        if axis == 'x':
            snake_x_change[j] = change
            snake_y_change[j] = 0
        if axis == 'y':
            snake_x_change[j] = 0
            snake_y_change[j] = change
        destination[j].pop(0)


window = pygame.display.set_mode((800, 600))

# snake
snake_x = [390, 390, 390]
snake_y = [530, 550, 570]
snake_x_change = [0, 0, 0]
snake_y_change = [-20, -20, -20]
snake_length = 3
destination = [[['x', -20, 390, 490], ['y', 20, 330, 490]], [['x', -20, 390, 490], ['y', 20, 350, 490]], [['x', -20, 390, 490], ['y', 20, 350, 490]]]

sec = time.time()
run = True
while run:
    window.fill((0, 0, 0))
    difference = time.time()-sec

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if difference >= 0.5:
        for i in range(snake_length):
            if destination[i]:
                snake_movement(destination[i][0], snake_x[i], snake_y[i], i)
            snake_y[i] += snake_y_change[i]
            snake_x[i] += snake_x_change[i]
            sec += difference
        if 0 >= snake_x[0] or snake_x[0] >= 800:
            run = False

    for i in range(snake_length):
        pygame.draw.rect(window, (0, 255, 0), (snake_x[i], snake_y[i], 20, 20))

    pygame.display.update()
