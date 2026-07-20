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

# Update the game state based on the user input
if direction == 'W':
    # Move the snake up
    pass
elif direction == 'A':
    # Move the snake left
    pass
elif direction == 'S':
    # Move the snake down
    pass
elif direction == 'D':
    # Move the snake right
    pass

# Update the game board with the new snake position