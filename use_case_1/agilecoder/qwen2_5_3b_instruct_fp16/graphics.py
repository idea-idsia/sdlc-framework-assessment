'''
This module uses ASCII characters to design the game interface.
'''
def draw_snake(snake_body):
    for y, row in enumerate(gamedisplay.board):
        for x, cell in enumerate(row):
            if (x, y) in snake_body:
                print('O', end='')
            elif (x, y) == gamedisplay.food_position:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def draw_board(board):
    for row in board:
        print('|'.join(row))
    print()
# Example usage:
gamedisplay.board = display_grid(width, height)
draw_board(gamedisplay.board)
draw_snake(snake_body)