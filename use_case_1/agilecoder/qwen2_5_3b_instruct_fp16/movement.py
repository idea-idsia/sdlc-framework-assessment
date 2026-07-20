'''
This module handles arrow key controls for the snake's movement.
It ensures the snake moves continuously in the chosen direction.
'''
from gamedisplay import display_grid
from snake import initialize_snake
def move_snake(snake_body, board):
    # Get user input (for simplicity, hardcoded to 'right')
    direction = 'right'
    def update_position(x, y, direction):
        if direction == 'right':
            return x + 1, y
        elif direction == 'left':
            return x - 1, y
        elif direction == 'up':
            return x, y - 1
        elif direction == 'down':
            return x, y + 1
    # Update snake's position based on the current and new directions
    updated_snake = []
    for i in range(len(snake_body)):
        x, y = update_position(snake_body[i][0], snake_body[i][1], direction)
        updated_snake.append((x, y))
    # Display the updated board with the new snake position
    display_grid(width, height)
    return updated_snake
# Example usage:
snake_body = initialize_snake(board)
move_snake(snake_body, board)