import curses
import random


# Initialize the game window
def init_game(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)
    sh, sw = stdscr.getmaxyx()

    # Define game board dimensions and initialize snake position
    board_height = min(sh - 2, sw - 2)
    board_width = board_height
    start_x = (sw // 2) - (board_width // 2)
    start_y = (sh // 2) - (board_height // 2)

    # Initialize snake and food positions
    snake = [(start_y + i, start_x) for i in range(board_height)]
    food = generate_food(snake, board_height, board_width)

    # Define initial direction (right)
    direction = curses.KEY_RIGHT

    while True:
        stdscr.clear()

        # Display the snake and food
        for y, x in snake + [food]:
            if (y, x) == food:
                stdscr.addch(y, x, '*')  # Food
            else:
                stdscr.addch(y, x, '#')  # Snake body

        # Display the game over message if necessary
        if game_over(snake):
            stdscr.addstr(0, 0, "Game Over! Score: " + str(len(snake) - board_height), curses.color_pair(1))
            stdscr.refresh()
            # Wait for user to restart the game
            while True:
                key = stdscr.getch()
                if key == ord('r'):
                    return start_game(stdscr)

        # Get user input and update direction
        next_key = stdscr.getch()
        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = next_key

        # Move the snake
        new_head = move_snake(direction, snake[0])

        # Check for collisions
        if collision(new_head, food):
            snake.insert(0, new_head)
            food = generate_food(snake, board_height, board_width)
        elif not is_valid_position(new_head, snake):
            break
        else:
            tail = snake.pop()
            snake.insert(0, new_head)

        stdscr.refresh()


# Generate food at a random position on the board
def generate_food(snake, board_height, board_width):
    while True:
        y = random.randint(1, board_height - 2)
        x = random.randint(1, board_width - 2)
        if (y, x) not in snake:
            return (y, x)


# Check for collision between the snake's head and food
def collision(head, food):
    return head == food


# Move the snake based on direction
def move_snake(direction, old_head):
    if direction == curses.KEY_UP:
        return (old_head[0] - 1, old_head[1])
    elif direction == curses.KEY_DOWN:
        return (old_head[0] + 1, old_head[1])
    elif direction == curses.KEY_LEFT:
        return (old_head[0], old_head[1] - 1)
    elif direction == curses.KEY_RIGHT:
        return (old_head[0], old_head[1] + 1)


# Check if the snake is out of bounds or has collided with itself
def game_over(snake):
    sh, sw = stdscr.getmaxyx()
    board_height = min(sh - 2, sw - 2)
    board_width = board_height

    if (not 0 <= snake[0][0] < board_height or not 0 <= snake[0][1] < board_width):
        return True
    for segment in snake[1:]:
        if segment == snake[0]:
            return True
    return False


# Check if the new head position is valid (not outside the board and not on the snake body)
def is_valid_position(new_head, snake):
    sh, sw = stdscr.getmaxyx()
    board_height = min(sh - 2, sw - 2)
    board_width = board_height

    if not (0 <= new_head[0] < board_height and 0 <= new_head[1] < board_width):
        return False
    for segment in snake:
        if new_head == segment:
            return False
    return True


# Start the game
def start_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)

    # Initialize snake and food positions
    sh, sw = stdscr.getmaxyx()
    board_height = min(sh - 2, sw - 2)
    board_width = board_height
    start_x = (sw // 2) - (board_height // 2)
    start_y = (sh // 2) - (board_height // 2)

    snake = [(start_y + i, start_x) for i in range(board_height)]
    food = generate_food(snake, board_height, board_width)

    # Define initial direction (right)
    direction = curses.KEY_RIGHT

    while True:
        stdscr.clear()

        # Display the snake and food
        for y, x in snake + [food]:
            if (y, x) == food:
                stdscr.addch(y, x, '*')  # Food
            else:
                stdscr.addch(y, x, '#')  # Snake body

        # Display the game over message if necessary
        if game_over(snake):
            stdscr.addstr(0, 0, "Game Over! Score: " + str(len(snake) - board_height), curses.color_pair(1))
            stdscr.refresh()
            # Wait for user to restart the game
            while True:
                key = stdscr.getch()
                if key == ord('r'):
                    return start_game(stdscr)

        # Get user input and update direction
        next_key = stdscr.getch()
        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = next_key

        # Move the snake
        new_head = move_snake(direction, snake[0])

        # Check for collisions
        if collision(new_head, food):
            snake.insert(0, new_head)
            food = generate_food(snake, board_height, board_width)
        elif not is_valid_position(new_head, snake):
            break
        else:
            tail = snake.pop()
            snake.insert(0, new_head)

        stdscr.refresh()


curses.wrapper(start_game)