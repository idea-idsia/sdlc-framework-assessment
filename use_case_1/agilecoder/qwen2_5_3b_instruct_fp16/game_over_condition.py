def check_game_over(snake_positions, food_position):
    head = snake_positions[-1]
    if detect_collision(head, snake_positions + [snake_positions[0]]):
        return True
    if detect_food_collision(head, food_position):
        grow_snake(board)
        total_score += 10
        return False