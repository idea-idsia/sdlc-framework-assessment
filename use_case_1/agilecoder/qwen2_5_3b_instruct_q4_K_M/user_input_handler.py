# user_input_handler.py
import curses
def snake_input(snake: SnakeGameUIHandler):
    def move_snake(snake: SnakeGameUIHandler):
        try:
            direction = snake.current_direction
        except AttributeError:
            raise ValueError("No current direction set for the snake.")
        if (direction not in snake.snake_positions[1:] and 
                0 <= direction < 256 or 
                snake.board_size[0] - 1 <= direction < snake.board_size[0]):
            raise ValueError(f"Invalid input: No such move as {direction}.")
        new_head_x, new_head_y = snake.snake_positions[0][0] + direction[0], \
                                  snake.snake_positions[0][1] + direction[1]
        if (new_head_x, new_head_y) in snake.snake_positions:
            raise ValueError(f"Invalid move: Snake hit itself at ({new_head_x}, {new_head_y}).")
        if (not 0 <= new_head_x < snake.board_size[0] or 
                not 0 <= new_head_y < snake.board_size[1]):
            raise ValueError(f"Snake got out of the board at position ({new_head_x}, {new_head_y}).")
        snake.snake_positions.insert(0, (new_head_x, new_head_y))
    return move_snake
def handle_input(snake_positions: list):
    if not isinstance(snake_positions, list) or not all(isinstance(position, tuple) and len(position) == 2 for position in snake_positions):
        raise ValueError("Invalid input. The snake's positions should be a list of tuples.")
    if not (0 <= snake_positions[0][0] < snake_game.board_size[0] and 
            0 <= snake_positions[0][1] < snake_game.board_size[1]):
        raise ValueError(f"Snake got out of the board at position ({snake_positions[0][0]}, {snake_positions[0][1]}).")
    return move_snake(snake_positions)