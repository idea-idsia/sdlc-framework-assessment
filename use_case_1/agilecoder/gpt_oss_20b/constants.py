'''
Module defining global constants used throughout the Snake game.
'''
import pygame  # Needed for pygame.USEREVENT
# Grid configuration
GRID_SIZE = 10          # 10x10 grid
CELL_SIZE = 40          # pixels per cell
# Screen dimensions
SCREEN_WIDTH = GRID_SIZE * CELL_SIZE
SCREEN_HEIGHT = GRID_SIZE * CELL_SIZE
# Game configuration
FPS = 10                # frames per second
MOVE_EVENT = pygame.USEREVENT + 1  # custom event for snake movement
MOVE_DELAY = 150        # milliseconds between automatic moves
# Colors (R, G, B)
COLOR_BG = (0, 0, 0)          # black background
COLOR_SNAKE = (0, 255, 0)     # green snake
COLOR_FOOD = (255, 0, 0)      # red food
COLOR_TEXT = (255, 255, 255)  # white text