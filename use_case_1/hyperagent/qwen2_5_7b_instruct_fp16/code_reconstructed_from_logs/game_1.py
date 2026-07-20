import numpy as np

# Define grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Initialize the snake
snake_position = [(5, 5)]  # Starting position at the center of the grid
snake_direction = "RIGHT"  # Initial direction to move right

# Function to display the game board (using ASCII for simplicity)
def display_game_board():
    board = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=str)
    for x, y in snake_position:
        board[y][x] = "S"
    print(board)

display_game_board()