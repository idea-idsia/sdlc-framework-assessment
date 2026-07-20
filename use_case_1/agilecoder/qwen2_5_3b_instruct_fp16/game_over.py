'''
This module triggers a game over scenario based on collisions.
It displays a game over message and allows the player to restart the game.
'''
def display_gameover_message():
    print("Game Over!")
def reset_board(board):
    board.clear()
    snake_body = initialize_snake(board)
# Example usage:
board = display_grid(width, height)
display_gameover_message()
reset_board(board)