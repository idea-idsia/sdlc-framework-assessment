'''
main.py - Main file for running the snake game
'''
import pygame
from game_board import GameBoard
from constants import *
from snake import Snake
from food import Food
# Initialize pygame
pygame.init()
# Create game board, snake, and food objects
board = GameBoard(10, 10)
snake = Snake(board, [5, 5], 'right')
food = Food(board, [7, 7])
# Set up the screen
screen = pygame.display.set_mode((board.width * board.block_size, board.height * board.block_size))
pygame.display.set_caption('Snake Game')
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Main game loop
while True:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move('left')
            elif event.key == pygame.K_RIGHT:
                snake.move('right')
            elif event.key == pygame.K_UP:
                snake.move('up')
            elif event.key == pygame.K_DOWN:
                snake.move('down')
    # Update game objects and display the game board
    snake.update()
    food.spawn()
    screen.fill(BLACK)
    board.draw(screen, WHITE)
    pygame.display.flip()