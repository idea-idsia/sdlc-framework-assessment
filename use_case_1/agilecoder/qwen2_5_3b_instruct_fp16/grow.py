'''
This module handles snake growth when it consumes food.
It increases the length of the snake by adding a new segment to its body.
'''
from collision import detect_collisions
from gamedisplay import display_grid
def grow_snake(snake_body):
    if not detect_collisions(snake_body):  # Add logic for actual game conditions
        x, y = snake_body[-1]  # Get the last position of the snake's head
        head_x, head_y = get_next_position(x, y, 'right')  # Calculate the new head position
        def set_new_segment(board):
            nonlocal head_x, head_y
            board[head_y][head_x] = 'O'
        set_new_segment(display_grid(width, height))
# Example usage:
snake_body = initialize_snake(board)
grow_snake(snake_body)