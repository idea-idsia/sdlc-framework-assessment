import curses
import random
from time import sleep

# Game settings
GRID_SIZE = 10
SNAKE_CHAR = 'O'
BODY_CHAR = 'o'
FOOD_CHAR = '*'


def initialize_game():
    # Initialize screen
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.nodelay(True)
    return stdscr


def draw_grid(stdscr, snake, food):
    stdscr.clear()

    # Draw top border
    stdscr.addstr(0, 0, '+' + ('-' * GRID_SIZE) + '+')

    for y in range(GRID_SIZE):
        stdscr.addstr(y + 1, 0, '|')  # Left border

        for x in range(GRID_SIZE):
            if (y, x) == snake[0]:
                stdscr.addch(y + 1, x + 1, SNAKE_CHAR)
            elif (y, x) in snake[1:]:
                stdscr.addch(y + 1, x + 1, BODY_CHAR)
            elif (y, x) == food:
                stdscr.addch(y + 1, x + 1, FOOD_CHAR)
            else:
                stdscr.addstr(y + 1, x + 1, ' ')

        stdscr.addstr(y + 1, GRID_SIZE + 2, '|')  # Right border

    # Draw bottom border
    stdscr.addstr(GRID_SIZE + 1, 0, '+' + ('-' * GRID_SIZE) + '+')

    # Display score and instructions
    stdscr.addstr(2, GRID_SIZE + 4, f"Score: {len(snake) - 1}")
    stdscr.addstr(3, GRID_SIZE + 4, "Use arrow keys to control the snake")
    stdscr.addstr(4, GRID_SIZE + 4, "Press 'P' to pause")
    stdscr.addstr(5, GRID_SIZE + 4, "Press 'Q' to quit")


def generate_food(snake):
    while True:
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if food not in snake:
            return food


def main(stdscr):
    # Initialize game state
    snake = [(5, 5)]  # Starting position at the center
    direction = (0, 1)  # Start moving right
    food = generate_food(snake)

    while True:
        draw_grid(stdscr, snake, food)

        # Get user input
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('p'):
            stdscr.addstr(GRID_SIZE + 3, GRID_SIZE + 4, "Game paused. Press any key to resume.")
            stdscr.refresh()
            while True:
                pause_key = stdscr.getch()
                if pause_key != -1:
                    break

        # Change direction based on arrow keys
        if key == curses.KEY_UP and direction != (1, 0):
            direction = (-1, 0)
        elif key == curses.KEY_DOWN and direction != (-1, 0):
            direction = (1, 0)
        elif key == curses.KEY_LEFT and direction != (0, 1):
            direction = (0, -1)
        elif key == curses.KEY_RIGHT and direction != (0, -1):
            direction = (0, 1)

        # Move snake
        head_y, head_x = snake[0]
        dy, dx = direction
        new_head = ((head_y + dy) % GRID_SIZE, (head_x + dx) % GRID_SIZE)

        # Check for collisions with self
        if new_head in snake:
            stdscr.addstr(GRID_SIZE // 2, GRID_SIZE // 2, "Game Over! Press 'R' to restart.")
            stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord('r'):
                    main(stdscr)
                elif key == ord('q'):
                    return

        # Check for collision with food
        snake.insert(0, new_head)
        if new_head != food:
            snake.pop()
        else:
            food = generate_food(snake)

        sleep(0.1)


if __name__ == "__main__":
    stdscr = initialize_game()
    try:
        main(stdscr)
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()