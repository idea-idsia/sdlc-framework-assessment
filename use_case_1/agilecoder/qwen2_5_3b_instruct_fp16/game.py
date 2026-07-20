'''
This program simulates a snake game.
The goal is to guide the snake through a grid while avoiding collisions and eating food.
'''
import random
GRID_SIZE = 20
def render_board(board):
    for row in board:
        print(' '.join(row))
def init_snake(snake_position, board_size):
    snake = [snake_position]
    return snake
def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == 'UP':
        new_head = (head_x, head_y - 1)
    elif direction == 'DOWN':
        new_head = (head_x, head_y + 1)
    elif direction == 'LEFT':
        new_head = (head_x - 1, head_y)
    elif direction == 'RIGHT':
        new_head = (head_x + 1, head_y)
    snake.insert(0, new_head)
    return snake
def place_food(board, food_position):
    x, y = random.randint(0, board_size[0] - 1), random.randint(0, board_size[1] - 1)
    if (x, y) not in snake:
        return (x, y)
    else: 
        return place_food(board, food_position)
def is_collision(head, tail):
    for body_segment in tail:
        if head == body_segment:
            return True
    return False
def is_grid_out_of_boundaries(head, board_size):
    x, y = head
    size_x, size_y = board_size
    return not (0 <= x < size_x and 0 <= y < size_y)
# Game setup
snake_position = (10, 10) 
direction = 'RIGHT'
food_position = place_food((GRID_SIZE, GRID_SIZE), food_position=None)
score = 0
def game_over(snake):
    if is_grid_out_of_boundaries(snake[0], (GRID_SIZE, GRID_SIZE)) or is_collision(snake[0], snake[:-1]):
        print("Game Over")
        display_score(score)
snake = Snake()
while True:
    render_board([[i for i in range(0, GRID_SIZE)] for _ in range(GRID_SIZE)])
    print(f"Score: {score}")
    if is_collision(snake[0], snake[:-1]) or is_grid_out_of_boundaries(snake[0], (GRID_SIZE, GRID_SIZE)):
        break
    input_direction = ''
    while not (input_direction == 'UP' or input_direction == 'DOWN' or input_direction == 'LEFT' or input_direction == 'RIGHT'):
        input_direction = input("Press arrow keys to move: ")
    snake = move_snake(snake, input_direction)
    food_position = place_food((GRID_SIZE, GRID_SIZE), food_position)
    if snake[0] == food_position:
        score += 1
        food_position = place_food((GRID_SIZE, GRID_SIZE), food_position)
grow_snake(snake)
game_over(snake)
update_score(snake)