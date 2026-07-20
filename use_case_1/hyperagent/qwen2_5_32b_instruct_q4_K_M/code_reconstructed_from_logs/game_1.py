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

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255)) # Fill the background with white color
    draw_grid(screen, 800, 600)  # Draw the grid on top of it

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()  # Update the display

pygame.quit()