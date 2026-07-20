def detect_collision(board):
    """
    Detects collisions with boundaries or snake body.
    :param board: The current state of the game board (list).
    :return: True if a collision is detected, False otherwise.
    """
    head_x, head_y = next(iter(board[0]))
    tail_x, tail_y = board[-1][-1]
    # Check boundaries
    if not 0 < head_x < board.grid_size or not 0 < head_y < board.grid_size:
        return True
    # Check collision with the snake body
    for segment in reversed(board[1:]):
        if (tail_x, tail_y) == (head_x, head_y):
            return True
    return False
def detect_food_collision(board):
    """
    Detects collisions between the snake and food.
    :param board: The current state of the game board (list).
    :return: True if a collision is detected, False otherwise.
    """
    x, y = next(iter(board[0]))
    for segment in board:
        if 'o' in segment[x:x+1]:
            return True
        elif 'o' in segment[y:y+1]:
            return True
    return False