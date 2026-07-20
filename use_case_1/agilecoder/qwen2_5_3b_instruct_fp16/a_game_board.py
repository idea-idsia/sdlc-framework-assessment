'''
This file defines the game board and its dimensions.
'''
def display_grid():
    '''Displays the grid on the screen.'''
    print("+---" * 10 + "+") # Top border
    for _ in range(10):
        row = "|   " * 10 + "|" # Horizontal line
        for _ in range(10):
            row += f"| {chr(ord('A') - 1)} " if (i, j) == (9, 9) else f'|   '
        print(row)
    print("+---" * 10 + "+")
display_grid()