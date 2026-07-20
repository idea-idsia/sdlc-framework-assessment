'''
Main execution of the snake game.
'''
width, height = setup_game()
board = (width, height)
is_running = True
direction = (1, 0)  # Start moving right
food_position = generate_food(board)
snake_head, direction = initialize_snake(size=3)
place_snake(snake_head, direction)
while is_running:
    move_snake(snake_head, direction)
    handle_keys()
    check_collision(snake_head)
    check_snake_body_collision(snake_head)
    place_snake(snake_head, direction)
    if (snake_head[0] == food_position):
        update_score(1)
        food_position = generate_food(board)
    display_score()
    check_collision(snake_head)
    check_snake_body_collision(snake_head)
    handle_game_over(snake_head, board)