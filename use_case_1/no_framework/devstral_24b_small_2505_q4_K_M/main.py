import curses
import random

# Initialize screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Define dimensions and initial values
snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]
food = [sh//2, sw//2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Initial direction
key = curses.KEY_RIGHT

# Game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head position based on current direction
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head position at the start of snake list
    snake.insert(0, new_head)

    # Check for collisions with boundaries or self
    if (snake[0][0] in [0, sh] or
            snake[0][1] in [0, sw] or
            snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Check if food has been consumed
    if snake[0] == food:
        # Increase score
        w.addstr(0, 0, "Score: " + str(len(snake)-3))
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Remove the tail segment of the snake
        last = snake.pop()
        w.addch(last[0], last[1], ' ')

    # Draw new head position
    w.addch(snake[0][0], snake[0][1], '#')

# Exit program on game over
curses.endwin()