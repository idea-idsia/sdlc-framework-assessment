game_board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# NEW SECTION

WIDTH, HEIGHT = 10, 10

# NEW SECTION

def display_board(game_board):
    output = ""
    for row in game_board:
        for col in row:
            if col == 0:
                output += "  "
            elif col == 1:
                output += "X "
            else:
                output += "O "
        output += "\n"
    return output

# NEW SECTION

snake = [starting_position]

# NEW SECTION

starting_position = (0, 0)
length = 1

# NEW SECTION

direction = "right"

# NEW SECTION

import curses

def move_snake(snake, direction):
    if direction == "up":
        new_position = (snake[0][0] - 1, snake[0][1])
    elif direction == "down":
        new_position = (snake[0][0] + 1, snake[0][1])
    elif direction == "left":
        new_position = (snake[0][0], snake[0][1] - 1)
    else:
        new_position = (snake[0][0], snake[0][1] + 1)
    return new_position

# NEW SECTION

while True:
    new_position = move_snake(snake, direction)
    if check_collision(new_position, game_board):
        break
    else:
        snake.append(new_position)

# NEW SECTION

def update_position(snake, new_position):
    for i in range(len(snake)):
        if snake[i] == new_position:
            return False
        else:
            snake[i] = new_position
    return True

# NEW SECTION

def generate_food(game_board):
    while True:
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        if check_collision((x, y), game_board):
            continue
        else:
            return (x, y)

# NEW SECTION

def check_collision(position, game_board):
    if position in snake:
        return True
    else:
        return False

# NEW SECTION

def eat_food(snake, food):
    if food in snake:
        snake.append(food)
        return True
    else:
        return False

# NEW SECTION

score = 0
def update_score():
    global score
    score += 1

# NEW SECTION

def display_score(score):
    return f"Score: {score}"

# NEW SECTION

def check_game_over(snake):
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        return True
    else:
        return False

# NEW SECTION

def check_self_collision(snake):
    for i in range(len(snake) - 1):
        if snake[i] == snake[i + 1]:
            return True
    else:
        return False

# NEW SECTION

def display_game_over(message):
    return f"{message}\n\nPress 'Enter' to restart."

# NEW SECTION

def restart_game():
    global game_board, snake, length, score
    game_board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    snake = [starting_position]
    length = 1
    score = 0
    display_starting_screen()

# NEW SECTION

def handle_input(direction):
    global direction
    if direction == "up":
        new_position = (snake[0][0] - 1, snake[0][1])
    elif direction == "down":
        new_position = (snake[0][0] + 1, snake[0][1])
    elif direction == "left":
        new_position = (snake[0][0], snake[0][1] - 1)
    else:
        new_position = (snake[0][0], snake[0][1] + 1)
    return new_position

# NEW SECTION

def draw_game_board():
    global game_board, snake, direction, length, score
    output = display_board(game_board)
    for i in range(len(snake)):
        output += "X " if (i == 0 and direction == "left") or (i > 0 and snake[i][1] - 1 == snake[i - 1][1] and snake[i - 1][0] == snake[i][0]) else "O "
    output += "\nScore: {}\n".format(score)
    return output

# NEW SECTION

def update_game_state():
    global game_board, snake, direction, length, score
    new_position = handle_input(direction)
    if check_collision(new_position, game_board):
        return False
    else:
        snake.append(new_position)
        food = generate_food(game_board)
        eat_food(snake, food)
        update_score()
        return True

# NEW SECTION

def game_loop():
    global game_board, snake, direction, length, score
    while True:
        new_position = handle_input(direction)
        if check_collision(new_position, game_board):
            display_game_over("Game Over")
            restart_game()
            break
        else:
            snake.append(new_position)
            food = generate_food(game_board)
            eat_food(snake, food)
            update_score()
    return True

# NEW SECTION

def display_starting_screen():
    global game_board, snake, direction, length, score
    output = "\n\nSNAKE GAME\n"
    output += "==========\n\n"
    output += "Use arrow keys to move the snake.\n"
    output += "Press 'Enter' to start.\n\n"
    output += display_board(game_board)
    return output

# NEW SECTION

def handle_input(direction):
    global direction
    if direction == "up":
        new_position = (snake[0][0] - 1, snake[0][1])
    elif direction == "down":
        new_position = (snake[0][0] + 1, snake[0][1])
    elif direction == "left":
        new_position = (snake[0][0], snake[0][1] - 1)
    else:
        new_position = (snake[0][0], snake[0][1] + 1)
    return new_position
