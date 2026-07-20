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


# Function to update the snake's position based on direction
def move_snake(direction):
    new_position = []
    if direction == "RIGHT":
        new_x = snake_position[-1][0] + 1
        new_y = snake_position[-1][1]
    elif direction == "LEFT":
        new_x = snake_position[-1][0] - 1
        new_y = snake_position[-1][1]
    elif direction == "UP":
        new_x = snake_position[-1][0]
        new_y = snake_position[-1][1] - 1
    elif direction == "DOWN":
        new_x = snake_position[-1][0]
        new_y = snake_position[-1][1] + 1

    if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
        new_position.append((new_x, new_y))

    return new_position


# Update the snake's position for one move
snake_position.extend(move_snake(snake_direction))