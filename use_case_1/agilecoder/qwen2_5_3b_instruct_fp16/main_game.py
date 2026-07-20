import snake_init, food_generation, collision_handling, animations_effects, score_display, game_over_condition, growth, key_handler, graphics
from datetime import timedelta
snake_positions = snake_init.initialize_snake()
food_position = food_generation.generate_food(snake_positions)
game_over = False
direction = 'RIGHT'
total_score = 0
while not game_over:
    # Removed unnecessary time.sleep(0.5) for better control over speed
    if key_handler.handle_input():
        snake_positions = movement.handle_movement(snake_positions, direction)
        collision_handling.detect_collision(snake_positions)
        draw_snake(snake_positions)
        animations_effects.animate_snake_movement()
        score_display.update_score(total_score)
        if check_game_over(snake_positions):
            handle_game_over(total_score)
            game_over = True
    else:
        break
snake_init.move_snake(new_direction)
game_over_condition.check_game_over()