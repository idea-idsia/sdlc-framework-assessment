'''
This module generates food at random positions on the game board.
It ensures that food doesn’t appear on the snake’s body.
'''
from gamedisplay import display_grid
from random import randint
import copy
def generate_food(board):
    # Generate a list of available coordinates by excluding snake's body positions
    snake_body = [cell for sublist in board for cell in sublist]
    available_positions = [(x, y) for x in range(width) for y in range(height) if (x, y) not in snake_body]
    # Choose a random position to place the food
    x_food, y_food = available_positions[randint(0, len(available_positions)-1)]
    def set_food(board, food_position):
        nonlocal x_food, y_food
        board[y_food][x_food] = '*'
    # Set the new food position on the game board
    set_food(board, food_position)
    return (x_food, y_food)
# Example usage:
board = display_grid(width, height)
food_position = generate_food(board)