import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')

# Define the size of each cell in the grid
cell_size = 20

def draw_grid(screen, width, height):
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, (100, 100, 100), (0, y), (width, y))

def draw_snake(snake_body):
    for segment in snake_body:
        x, y = segment
        pygame.draw.rect(screen, (0, 255, 0), (x * cell_size, y * cell_size, cell_size, cell_size))

# Snake initialization
snake_x, snake_y = 10, 10
snake_length = 3
snake_body = [(snake_x + i, snake_y) for i in range(snake_length)]
direction = "RIGHT"  # Initial direction

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255)) # Fill the background with white color
    draw_grid(screen, 800, 600)  # Draw the grid on top of it
    draw_snake(snake_body)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == K_DOWN and direction != "UP":
                direction = "DOWN"

    # Snake movement
    if direction == "RIGHT":
        snake_x += 1
    elif direction == "LEFT":
        snake_x -= 1
    elif direction == "UP":
        snake_y -= 1
    elif direction == "DOWN":
        snake_y += 1

    snake_body.insert(0, (snake_x, snake_y))
    snake_body.pop()

    pygame.display.flip()  # Update the display

pygame.quit()