import time
def animate_snake_movement(snake_body, direction):
    head_x, head_y = snake_body[0]
    if direction == 'left':
        new_head = (head_x - 1, head_y)
    elif direction == 'right':
        new_head = (head_x + 1, head_y)
    elif direction == 'up':
        new_head = (head_x, head_y - 1)
    else:  # down
        new_head = (head_x, head_y + 1)
    snake_body[0] = new_head
def animate_food_consumption():
    print("\n\n")