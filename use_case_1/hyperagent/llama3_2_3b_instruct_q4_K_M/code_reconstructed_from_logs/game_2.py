import random

# Game dimensions
rows = 10
columns = 10

# Initialize the game board with empty spaces and '#'
board = [[' ' for _ in range(columns)] for _ in range(rows)]

# Add walls around the board
for i in range(rows):
    board[i][0] = '#'
    board[i][columns-1] = '#'
for j in range(columns):
    board[0][j] = '#'
    board[rows-1][j] = '#'

def print_board(board):
    for row in board:
        print(' '.join(row))

print_board(board)

def get_user_input():
    direction = input("Enter a direction (W/A/S/D): ")
    return direction

direction = get_user_input()

# Generate food at random position
food_pos = (random.randint(0, rows-1), random.randint(0, columns-1))
while food_pos in old_snake_pos:
    food_pos = (random.randint(0, rows-1), random.randint(0, columns-1))

def move_snake(board, direction):
    # Define the possible movements based on the input direction
    if direction == 'W':
        new_position = [(i, j) for i in range(rows) for j in range(columns) if board[i][j] != '#']
    elif direction == 'A':
        new_position = [(i, j-1) for i in range(rows) for j in range(columns) if 0 <= j-1 < columns and board[i][j] != '#']
    elif direction == 'S':
        new_position = [(i, j+1) for i in range(rows) for j in range(columns) if 0 <= j+1 < columns and board[i][j] != '#']
    elif direction == 'D':
        new_position = [(i, j+1) for i in range(rows) for j in range(columns) if 0 <= j+1 < columns and board[i][j] != '#']

    # Update the game state with the new snake position
    for pos in old_snake_pos:
        board[pos[0]][pos[1]] = ' '
    for pos in new_position:
        board[pos[0]][pos[1]] = 'S'
    old_snake_pos, new_snake_pos = new_position, list(old_snake_pos)

# Update the game state with the new food position
board[food_pos[0]][food_pos[1]] = '*'

print_board(board)