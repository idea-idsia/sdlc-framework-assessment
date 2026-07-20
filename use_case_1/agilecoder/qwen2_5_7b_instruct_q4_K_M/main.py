"""
Main Application Entry Point
"""
import pygame
from game_board import GameBoard
from snake import Snake
# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")
# Create a game board and snake
game_board = GameBoard(screen)
snake = Snake(game_board)
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.set_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.set_direction("down")
            elif event.key == pygame.K_LEFT:
                snake.set_direction("left")
            elif event.key == pygame.K_RIGHT:
                snake.set_direction("right")
    # Update the game state
    try:
        snake.update()
        game_board.generate_food()  # Generate new food if not consumed yet
    except ValueError as e:
        print(e)
    # Draw the game board and snake
    game_board.draw()
    snake.draw()
    pygame.display.flip()
# Quit Pygame
pygame.quit()