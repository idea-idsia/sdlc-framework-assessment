#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Snake game implemented as a single, self‑contained module.
The design follows the specification exactly:
- Game, Snake, Food, Grid, Renderer, InputHandler classes.
- No external dependencies beyond the standard library.
- The game runs in a curses terminal window.
"""

from __future__ import annotations

import curses
import random
import time
from typing import List, Tuple


# ----------------------------------------------------------------------
# Data structures and interfaces
# ----------------------------------------------------------------------


class Grid:
    """Represents the game board."""

    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.width: int = width
        self.height: int = height

    def in_bounds(self, pos: Tuple[int, int]) -> bool:
        """Return True if pos is inside the grid."""
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def to_screen_coords(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Convert grid coordinates to curses screen coordinates.
        In curses, y is row, x is column.
        """
        x, y = pos
        return y, x


class Snake:
    """Represents the snake."""

    def __init__(self, start_pos: Tuple[int, int], start_dir: Tuple[int, int]) -> None:
        self.body: List[Tuple[int, int]] = [start_pos]
        self.direction: Tuple[int, int] = start_dir
        self._grow_pending: bool = False

    def move(self) -> None:
        """Move the snake forward by one cell."""
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head: Tuple[int, int] = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        if not self._grow_pending:
            self.body.pop()
        else:
            self._grow_pending = False

    def grow(self) -> None:
        """Set the snake to grow on the next move."""
        self._grow_pending = True

    def set_direction(self, new_dir: Tuple[int, int]) -> None:
        """Change the snake's direction if it is not a 180° reversal."""
        cur_dx, cur_dy = self.direction
        new_dx, new_dy = new_dir
        if (new_dx, new_dy) != (-cur_dx, -cur_dy):
            self.direction = new_dir

    def collides_with_self(self) -> bool:
        """Return True if the snake's head collides with its body."""
        return self.body[0] in self.body[1:]

    def collides_with_wall(self, grid: Grid) -> bool:
        """Return True if the snake's head is outside the grid."""
        return not grid.in_bounds(self.body[0])

    def head(self) -> Tuple[int, int]:
        """Return the current head position."""
        return self.body[0]


class Food:
    """Represents the food item."""

    def __init__(self, grid: Grid, snake: Snake) -> None:
        self.position: Tuple[int, int] = (0, 0)
        self.generate_new(grid, snake)

    def generate_new(self, grid: Grid, snake: Snake) -> None:
        """Place food on a random free cell."""
        free_cells: List[Tuple[int, int]] = [
            (x, y)
            for x in range(grid.width)
            for y in range(grid.height)
            if (x, y) not in snake.body
        ]
        if not free_cells:
            # No free space left; keep current position
            return
        self.position = random.choice(free_cells)

    def position(self) -> Tuple[int, int]:
        """Return the current food position."""
        return self.position


class Renderer:
    """Handles drawing the game state onto the curses window."""

    def __init__(self, window: curses.window) -> None:
        self.window: curses.window = window
        self.window.nodelay(True)  # Non-blocking input
        curses.curs_set(0)  # Hide cursor

    def clear(self) -> None:
        """Clear the window."""
        self.window.erase()

    def draw(
        self,
        grid: Grid,
        snake: Snake,
        food: Food,
        score: int,
        game_over: bool,
    ) -> None:
        """Render the entire game screen."""
        self.clear()

        # Draw border
        for x in range(grid.width):
            self.window.addch(0, x, curses.ACS_HLINE)
            self.window.addch(grid.height + 1, x, curses.ACS_HLINE)
        for y in range(grid.height + 2):
            self.window.addch(y, 0, curses.ACS_VLINE)
            self.window.addch(y, grid.width + 1, curses.ACS_VLINE)
        self.window.addch(0, 0, curses.ACS_ULCORNER)
        self.window.addch(0, grid.width + 1, curses.ACS_URCORNER)
        self.window.addch(grid.height + 1, 0, curses.ACS_LLCORNER)
        self.window.addch(grid.height + 1, grid.width + 1, curses.ACS_LRCORNER)

        # Draw food
        fx, fy = food.position
        fy_screen, fx_screen = grid.to_screen_coords((fx, fy))
        self.window.addch(fy_screen + 1, fx_screen + 1, curses.ACS_PI)

        # Draw snake
        for idx, (sx, sy) in enumerate(snake.body):
            sy_screen, sx_screen = grid.to_screen_coords((sx, sy))
            sy_screen += 1
            sx_screen += 1
            char: str = "@" if idx == 0 else "O"
            self.window.addch(sy_screen, sx_screen, char)

        # Draw score
        score_y: int = grid.height + 3
        score_x: int = 0
        score_text: str = f"Score: {score}"
        self.window.addstr(score_y, score_x, score_text)

        # Draw game over message if needed
        if game_over:
            msg: str = "GAME OVER! Press any key to exit."
            msg_y: int = grid.height // 2 + 1
            msg_x: int = (grid.width - len(msg)) // 2 + 1
            self.window.addstr(msg_y, msg_x, msg)

        self.window.refresh()


class InputHandler:
    """Processes user input and translates it into direction changes."""

    def __init__(self) -> None:
        self.last_direction: Tuple[int, int] = (1, 0)  # Default to moving right

    def get_direction(self, key: int) -> Tuple[int, int]:
        """Return the new direction based on the pressed key."""
        mapping: dict[int, Tuple[int, int]] = {
            curses.KEY_UP: (0, -1),
            curses.KEY_DOWN: (0, 1),
            curses.KEY_LEFT: (-1, 0),
            curses.KEY_RIGHT: (1, 0),
        }
        new_dir: Tuple[int, int] = mapping.get(key, self.last_direction)
        # Prevent 180° reversal
        cur_dx, cur_dy = self.last_direction
        new_dx, new_dy = new_dir
        if (new_dx, new_dy) != (-cur_dx, -cur_dy):
            self.last_direction = new_dir
        return self.last_direction


class Game:
    """Main game controller."""

    TICK_RATE: float = 0.1  # Seconds per frame

    def __init__(self, window: curses.window) -> None:
        self.window: curses.window = window

        # Initialize components
        self.grid: Grid = Grid(width=10, height=10)
        start_pos: Tuple[int, int] = (
            self.grid.width // 2,
            self.grid.height // 2,
        )
        start_dir: Tuple[int, int] = (1, 0)  # Moving right
        self.snake: Snake = Snake(start_pos, start_dir)
        self.food: Food = Food(self.grid, self.snake)
        self.renderer: Renderer = Renderer(self.window)
        self.input_handler: InputHandler = InputHandler()

        # Game state
        self.score: int = 0
        self.running: bool = True
        self.game_over_flag: bool = False

    # ------------------------------------------------------------------
    # Game loop helpers
    # ------------------------------------------------------------------

    def handle_input(self) -> None:
        """Read user input and update snake direction."""
        key: int = self.window.getch()
        if key != -1:
            new_dir: Tuple[int, int] = self.input_handler.get_direction(key)
            self.snake.set_direction(new_dir)

    def update(self) -> None:
        """Advance game state: move snake, check collisions, handle food."""
        self.snake.move()

        # Collision detection
        if self.snake.collides_with_wall(self.grid) or self.snake.collides_with_self():
            self.game_over()
            return

        # Food consumption
        if self.snake.head() == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.generate_new(self.grid, self.snake)

    def render(self) -> None:
        """Render the current game state."""
        self.renderer.draw(
            self.grid,
            self.snake,
            self.food,
            self.score,
            self.game_over_flag,
        )

    def game_over(self) -> None:
        """Handle game over state."""
        self.running = False
        self.game_over_flag = True

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    def start(self) -> None:
        """Run the main game loop."""
        while self.running:
            frame_start: float = time.time()

            self.handle_input()
            self.update()
            self.render()

            if self.game_over_flag:
                # Wait for a key press before exiting
                self.window.nodelay(False)
                self.window.getch()
                break

            elapsed: float = time.time() - frame_start
            if elapsed < self.TICK_RATE:
                time.sleep(self.TICK_RATE - elapsed)


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------


def main(stdscr: curses.window) -> None:
    """Curses wrapper entry point."""
    game: Game = Game(stdscr)
    game.start()


if __name__ == "__main__":
    curses.wrapper(main)
