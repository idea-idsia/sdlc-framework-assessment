def grow_snake(board):
    head_x, head_y = snake_body[0]
    for segment in snake_body[1:]:
        if (head_x - 1, head_y) == segment or (head_x + 1, head_y) == segment or (head_x, head_y - 1) == segment or (head_x, head_y + 1) == segment:
            return False
    new_segment = (head_x - 1 if direction == 'LEFT' else head_x + 1 if direction == 'RIGHT' else head_y + 1 if direction == 'UP' else head_y - 1)
    board[head_y][head_x] = ' '
    snake_body.append(new_segment)
    return True