#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Snake Game (ASCII) – Python + curses

Requirements:
- Python 3.6+
- Windows: pip install windows-curses (if needed)
"""

import curses
import random
import time
from collections import deque

# ----------- CONFIGURATION -----------
BOARD_HEIGHT = 10          # rows
BOARD_WIDTH  = 10          # columns
INITIAL_SNAKE_LENGTH = 3
SPEED_MS = 120             # delay between frames in milliseconds

# Directions as (dy, dx)
DIRS = {
    curses.KEY_UP:    (-1, 0),
    curses.KEY_DOWN:  (1, 0),
    curses.KEY_LEFT:  (0, -1),
    curses.KEY_RIGHT: (0, 1),
}

# Reverse direction map to prevent 180° turns
REVERSE_DIR = {
    curses.KEY_UP:    curses.KEY_DOWN,
    curses.KEY_DOWN:  curses.KEY_UP,
    curses.KEY_LEFT:  curses.KEY_RIGHT,
    curses.KEY_RIGHT: curses.KEY_LEFT,
}

# ------------------------------------


def main(stdscr):
    curses.curs_set(0)                # Hide cursor
    stdscr.nodelay(True)              # Non‑blocking input
    stdscr.keypad(True)               # Enable arrow keys

    # ---- color pairs ----
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   # snake normal
    curses.init_pair(2, curses.COLOR_RED,   curses.COLOR_BLACK)   # food
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # snake head
    curses.init_pair(4, curses.COLOR_CYAN,  curses.COLOR_BLACK)  # score / text
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # game over

    # ---- calculate window size ----
    # Add 2 for borders, +1 for 0‑based coordinates
    win_height = BOARD_HEIGHT + 2
    win_width  = BOARD_WIDTH  + 2

    # create a new window for the board
    win = curses.newwin(win_height, win_width, 1, 1)
    win.box()

    while True:
        game_over = play_game(win)
        if not game_over:  # player chose to quit
            break
        # otherwise, restart loop


def play_game(win):
    """Run a single game session.  Returns False if the user wants to quit."""
    # ---- init snake ----
    mid_y = BOARD_HEIGHT // 2
    mid_x = BOARD_WIDTH  // 2

    snake = deque()  # holds (y, x) tuples
    for i in range(INITIAL_SNAKE_LENGTH):
        snake.append((mid_y, mid_x - i))

    direction = curses.KEY_RIGHT          # start moving right
    next_dir = direction                  # buffered direction from key press

    # ---- init food ----
    food = generate_food(snake)

    score = 0
    last_eat_time = 0  # timestamp for the flash effect

    # ---- game loop ----
    while True:
        win.clear()
        win.box()

        # --- input ---
        key = win.getch()
        if key in DIRS:
            # don't allow reverse
            if REVERSE_DIR[key] != direction:
                next_dir = key
        elif key in (ord('q'), ord('Q')):
            return False   # quit

        # --- move snake ---
        direction = next_dir
        dy, dx = DIRS[direction]
        new_head = (snake[0][0] + dy, snake[0][1] + dx)

        # --- collision with walls ---
        if (new_head[0] <= 0 or new_head[0] >= BOARD_HEIGHT + 1 or
                new_head[1] <= 0 or new_head[1] >= BOARD_WIDTH + 1):
            return game_over_screen(win, score, False)  # hit boundary

        # --- collision with self ---
        if new_head in snake:
            return game_over_screen(win, score, False)  # hit body

        # --- food consumption ---
        if new_head == food:
            snake.appendleft(new_head)   # grow
            score += 1
            food = generate_food(snake)
            last_eat_time = time.time()
        else:
            snake.appendleft(new_head)
            snake.pop()  # normal move, remove tail

        # --- drawing ---
        # draw food
        win.addch(food[0], food[1], '*', curses.color_pair(2))

        # draw snake
        for idx, pos in enumerate(snake):
            char = 'O' if idx == 0 else 'o'
            color = curses.color_pair(3) if idx == 0 else curses.color_pair(1)
            # flash effect: head turns green for 0.1 sec after eating
            if idx == 0 and time.time() - last_eat_time < 0.1:
                color = curses.color_pair(1)
            win.addch(pos[0], pos[1], char, color)

        # draw score
        win.addstr(0, 2, f" Score: {score} ", curses.color_pair(4))

        win.refresh()
        curses.napms(SPEED_MS)


def generate_food(snake):
    """Return a random position (y, x) not occupied by the snake."""
    empty_cells = [
        (y, x)
        for y in range(1, BOARD_HEIGHT + 1)
        for x in range(1, BOARD_WIDTH + 1)
        if (y, x) not in snake
    ]
    return random.choice(empty_cells)


def game_over_screen(win, score, quit_requested):
    """Display Game Over screen.  Return False if player wants to quit."""
    win.clear()
    win.box()
    msg1 = " GAME OVER "
    msg2 = f" Final Score: {score} "
    msg3 = " Press R to restart or Q to quit "
    win.addstr(BOARD_HEIGHT // 2 - 1, (BOARD_WIDTH + 2 - len(msg1)) // 2, msg1, curses.color_pair(5) | curses.A_BOLD)
    win.addstr(BOARD_HEIGHT // 2,     (BOARD_WIDTH + 2 - len(msg2)) // 2, msg2, curses.color_pair(5))
    win.addstr(BOARD_HEIGHT // 2 + 1, (BOARD_WIDTH + 2 - len(msg3)) // 2, msg3, curses.color_pair(5))
    win.refresh()

    while True:
        key = win.getch()
        if key in (ord('q'), ord('Q')):
            return False  # quit
        if key in (ord('r'), ord('R')):
            return True   # restart


if __name__ == "__main__":
    curses.wrapper(main)