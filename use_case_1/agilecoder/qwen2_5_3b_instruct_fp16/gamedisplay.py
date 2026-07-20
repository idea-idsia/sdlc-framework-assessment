'''
This module creates a grid-based game board.
It defines the dimensions of the grid and displays it on the screen.
'''
def display_grid(width, height):
    game_board = []
    for y in range(height):
        row = [' '] * width
        game_board.append(row)
    return game_board
# Example usage:
width = 10
height = 10
board = display_grid(width, height)