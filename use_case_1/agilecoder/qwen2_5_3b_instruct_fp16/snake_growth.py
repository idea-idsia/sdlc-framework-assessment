import game_board
class SnakeGrowthManager:
    @staticmethod
    def grow_snake(game_board, new_food_position):
        if not game_board.food_position == new_food_position:
            return
        x, y = game_board.snake.body[0]
        if (x - 1, y) in game_board.food_position or (x + 1, y) in game_board.food_position or (x, y - 1) in game_board.food_position or (x, y + 1) in game_board.food_position:
            return
        snake_head = game_board.snake.body[0]
        new_snake_body = []
        for segment in range(len(game_board.snake.body)):
            if segment == 0:
                new_snake_body.append(snake_head)
            else:
                new_snake_body.append((snake_head[0] + (x - snake_head[0]) // abs(x-snake_head[0]), snake_head[1] + (y - snake_head[1]) // abs(y-snake_head[1])))
        game_board.snake.body = new_snake_body