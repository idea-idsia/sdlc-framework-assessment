'''
Snake Game in Python
This is a basic implementation of a Snake game using ASCII characters for graphics.
'''
import time
import random
def main():
    # Define game dimensions and initialize variables
    grid_width = 20
    grid_height = 15
    snake_size = 3
    snake_pos = [(grid_width // 2, grid_height // 2), 
                 (grid_width // 2 - 1, grid_height // 2), 
                 (grid_width // 2 - 2, grid_height // 2)]
    direction = 'RIGHT'
    while True:
        food_pos = (random.randint(0 + 1, grid_width - 2), random.randint(0 + 1, grid_height - 2))
        if food_pos not in snake_pos:
            break
    display_game_board(grid_width, grid_height, snake_pos, direction, food_pos)
    while True:
        display_game_board(grid_width, grid_height, snake_pos, direction, food_pos)
        if check_collision(snake_pos):
            break
        move_snake(snake_pos, direction, food_pos)
        time.sleep(0.2)  # Adjust speed as needed
def display_game_board(width, height, snake_pos, direction, food_pos):
    print(" " * width)
    for y in range(height - 1, -1, -1):
        row = []
        for x in range(width):
            if (x, y) == food_pos:
                row.append('@')
            elif (x, y) in snake_pos:
                row.append('o')
            else:
                row.append('.')
        print("".join(row))
    print(" " * width)
def check_collision(snake_pos):
    head = snake_pos[0]
    return head[0] < 0 or head[0] >= len(grid_width) - 1 or \
           head[1] < 0 or head[1] >= len(grid_height) - 1 or \
           head in snake_pos[:-1]
def move_snake(snake_pos, direction, food_pos):
    new_head = list(snake_pos[0])
    if direction == 'UP':
        new_head[1] -= 1
    elif direction == 'DOWN':
        new_head[1] += 1
    elif direction == 'LEFT':
        new_head[0] -= 1
    elif direction == 'RIGHT':
        new_head[0] += 1
    snake_pos.insert(0, tuple(new_head))
    if (new_head == food_pos):
        # Increase the length of the snake by adding a new segment
        snake_pos.append(snake_pos[-1])
    else:
        snake_pos.pop()
if __name__ == "__main__":
    main()