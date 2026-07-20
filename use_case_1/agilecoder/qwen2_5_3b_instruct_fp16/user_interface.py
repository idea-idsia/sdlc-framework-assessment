'''
User interface module.
Handles user input for arrow key controls,
renders the board, snake body and food using ASCII characters,
and updates game state in real-time.
'''
def render_board():
    """Render the game board."""
    print(' '.join([''.join(row) for row in gb.board]))
render_board()
snake.move_snake()
while True:
    user_input = input("Press 'q' to quit, or arrow keys (left, right, up, down) to move: ")
    if user_input == 'q': 
        break
    elif user_input == 'w':
        snake.direction = 'up'
    elif user_input == 'a':
        snake.direction = 'left'
    elif user_input == 's':
        snake.direction = 'down'
    elif user_input == 'd':
        snake.direction = 'right'
    render_board()
    snake.move_snake()
check_game_over()
update_score(snake)