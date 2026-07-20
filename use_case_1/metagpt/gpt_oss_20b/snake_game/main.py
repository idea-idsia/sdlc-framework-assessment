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
from typing import List, Tuple, Optional

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
        """Render the entire game state."""
        self.clear()

        # Draw border
        for x in range(grid.width + 2):
            self.window.addch(0, x, '#')
            self.window.addch(grid.height + 1, x, '#')
        for y in range(1, grid.height + 1):
            self.window.addch(y, 0, '#')
            self.window.addch(y, grid.width + 1, '#')

        # Draw food
        fx, fy = food.position
        sy, sx = grid.to_screen_coords((fx, fy))
        self.window.addch(sy + 1, sx + 1, '*')

        # Draw snake
        for idx, (sx, sy) in enumerate(snake.body):
            cy, cx = grid.to_screen_coords((sx, sy))
            char = '@' if idx == 0 else 'O'
            self.window.addch(cy + 1, cx + 1, char)

        # Draw score
        score_text = f"Score: {score}"
        self.window.addstr(grid.height + 3, 0, score_text)

        # Draw game over message
        if game_over:
            msg = "GAME OVER! Press any key to exit."
            self.window.addstr(grid.height // 2, (grid.width - len(msg)) // 2, msg)

        self.window.refresh()


class InputHandler:
    """Translates key presses into direction changes."""

    def __init__(self) -> None:
        self.last_direction: Tuple[int, int] = (1, 0)  # Default right

    def get_direction(self, key: int) -> Tuple[int, int]:
        """Return a new direction based on the key, or keep current."""
        mapping = {
            curses.KEY_UP: (0, -1),
            curses.KEY_DOWN: (0, 1),
            curses.KEY_LEFT: (-1, 0),
            curses.KEY_RIGHT: (1, 0),
        }
        new_dir = mapping.get(key, self.last_direction)
        # Prevent 180° reversal
        if new_dir != (-self.last_direction[0], -self.last_direction[1]):
            self.last_direction = new_dir
        return self.last_direction


class Game:
    """Main game controller."""

    TICK_RATE: float = 0.1  # Seconds per tick (10 FPS)

    def __init__(self, window: curses.window) -> None:
        self.window: curses.window = window
        self.grid: Grid = Grid(width=10, height=10)
        start_pos: Tuple[int, int] = (self.grid.width // 2, self.grid.height // 2)
        start_dir: Tuple[int, int] = (1, 0)  # Right
        self.snake: Snake = Snake(start_pos, start_dir)
        self.food: Food = Food(self.grid, self.snake)
        self.renderer: Renderer = Renderer(self.window)
        self.input_handler: InputHandler = InputHandler()
        self.score: int = 0
        self.running: bool = True
        self.game_over_flag: bool = False

    def start(self) -> None:
        """Run the main game loop."""
        while self.running:
            start_time = time.time()

            # Handle input
            key = self.window.getch()
            if key != -1:
                new_dir = self.input_handler.get_direction(key)
                self.snake.set_direction(new_dir)

            # Update game state
            self.snake.move()

            # Collision checks
            if self.snake.collides_with_wall(self.grid) or self.snake.collides_with_self():
                self.game_over()
            else:
                # Check food consumption
                if self.snake.head() == self.food.position:
                    self.snake.grow()
                    self.score += 1
                    self.food.generate_new(self.grid, self.snake)

            # Render
            self.renderer.draw(
                self.grid,
                self.snake,
                self.food,
                self.score,
                self.game_over_flag,
            )

            # If game over, wait for key press to exit
            if self.game_over_flag:
                self.window.nodelay(False)
                self.window.getch()
                break

            # Maintain tick rate
            elapsed = time.time() - start_time
            if elapsed < self.TICK_RATE:
                time.sleep(self.TICK_RATE - elapsed)

    def game_over(self) -> None:
        """Handle game over state."""
        self.running = False
        self.game_over_flag = True


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------


def main(stdscr: curses.window) -> None:
    """Initialize and start the game."""
    game = Game(stdscr)
    game.start()


if __name__ == "__main__":
    curses.wrapper(main)
