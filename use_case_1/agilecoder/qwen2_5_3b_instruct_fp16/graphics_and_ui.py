'''
This file uses ASCII characters to represent the snake and food.
'''
ASCII_CHARS = [' ', '.', '-', '=', '+', '*', '@']
def draw_snake(snake_positions):
    """Draw the snake using ASCII characters."""
    for x, y in snake_positions:
        print(ASCII_CHARS[1], end="")  # Snake body
    print('S', end="")  # Snake head
snake_head_position = snake_positions[0]
draw_snake(snake_positions)
def draw_food(food_position):
    """Draw food at the given position using ASCII characters."""
    x, y = food_position
    if (x, y) == snake_head_position:
        print(ASCII_CHARS[4], end='')  # Food eaten
    else:
        print(ASCII_CHARS[2], end='')  # Food
draw_food(food_position)