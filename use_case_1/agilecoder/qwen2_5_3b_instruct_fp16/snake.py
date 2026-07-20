'''
This module initializes the snake on the game board.
It defines the initial length and starting position of the snake,
and chooses a direction for the snake to start moving immediately.
'''
from gamedisplay import display_grid
def initialize_snake(board, length=5):
    # Initialize the snake's head at (0, 0)
    x, y = 4, 4
    snake_body = [(x, y)]
    def get_next_position(x, y, direction):
        if direction == 'right':
            return x + 1, y
        elif direction == 'left':
            return x - 1, y
        elif direction == 'up':
            return x, y - 1
        elif direction == 'down':
            return x, y + 1
    # Move the snake in a right direction initially
    head_x, head_y = get_next_position(x, y, 'right')
    snake_body.append((head_x, head_y))
    def set_head(board, length):
        nonlocal x, y
        board[y][x] = 'O'
    # Set the initial head position on the game board
    set_head(board, length)
    return snake_body
# Example usage:
board = display_grid(width, height)
snake_body = initialize_snake(board)