## renderer.py
"""
Renderer component for the console Snake game.

This module implements the :class:`Renderer` class as specified in the
design documentation.  The implementation is fully typed, avoids
circular imports, and follows the public interface exactly.
"""

from __future__ import annotations

import curses
from typing import Any

# Import type hints for Grid, Snake, and Food.  No circular imports
# are created because these modules do not import renderer.
from grid import Grid
from snake import Snake
from food import Food


class Renderer:
    """
    Handles drawing the game state onto the curses window.

    Parameters
    ----------
    window : curses.window
        The curses window used for rendering.
    """

    __slots__ = ("window",)

    def __init__(self, window: curses.window) -> None:
        """
        Initialise a new renderer.

        Parameters
        ----------
        window : curses.window
            The curses window used for rendering.
        """
        self.window: curses.window = window
        # Non‑blocking input so that getch() does not block the game loop.
        self.window.nodelay(True)
        # Hide the cursor for a cleaner look.
        curses.curs_set(0)

    # ------------------------------------------------------------------
    # Utility methods
    # ------------------------------------------------------------------
    def clear(self) -> None:
        """
        Clear the window before drawing a new frame.
        """
        self.window.erase()

    # ------------------------------------------------------------------
    # Rendering logic
    # ------------------------------------------------------------------
    def draw(
        self,
        grid: Grid,
        snake: Snake,
        food: Food,
        score: int,
        game_over: bool,
    ) -> None:
        """
        Render the entire game screen.

        Parameters
        ----------
        grid : Grid
            The game grid.
        snake : Snake
            The snake instance.
        food : Food
            The food instance.
        score : int
            Current score.
        game_over : bool
            Flag indicating whether the game is over.
        """
        # Clear the window for a fresh frame.
        self.clear()

        # ------------------------------------------------------------------
        # Draw the border
        # ------------------------------------------------------------------
        # Horizontal lines
        hline: Any = curses.ACS_HLINE
        # Vertical lines
        vline: Any = curses.ACS_VLINE
        # Corners
        ulcorner: Any = curses.ACS_ULCORNER
        urcorner: Any = curses.ACS_URCORNER
        llcorner: Any = curses.ACS_LLCORNER
        lrcorner: Any = curses.ACS_LRCORNER

        # Top and bottom horizontal borders
        for x in range(grid.width):
            self.window.addch(0, x, hline)
            self.window.addch(grid.height + 1, x, hline)

        # Left and right vertical borders
        for y in range(grid.height + 2):
            self.window.addch(y, 0, vline)
            self.window.addch(y, grid.width + 1, vline)

        # Corners
        self.window.addch(0, 0, ulcorner)
        self.window.addch(0, grid.width + 1, urcorner)
        self.window.addch(grid.height + 1, 0, llcorner)
        self.window.addch(grid.height + 1, grid.width + 1, lrcorner)

        # ------------------------------------------------------------------
        # Draw the food
        # ------------------------------------------------------------------
        food_pos: tuple[int, int] = food.position
        food_screen_y: int = grid.to_screen_coords(food_pos)[0] + 1
        food_screen_x: int = grid.to_screen_coords(food_pos)[1] + 1
        # Use a distinct character for food.
        food_char: Any = curses.ACS_PI
        self.window.addch(food_screen_y, food_screen_x, food_char)

        # ------------------------------------------------------------------
        # Draw the snake
        # ------------------------------------------------------------------
        for idx, segment in enumerate(snake.body):
            segment_screen_y: int = grid.to_screen_coords(segment)[0] + 1
            segment_screen_x: int = grid.to_screen_coords(segment)[1] + 1
            # Head uses '@', body uses 'O'.
            segment_char: str = "@" if idx == 0 else "O"
            self.window.addch(segment_screen_y, segment_screen_x, segment_char)

        # ------------------------------------------------------------------
        # Draw the score
        # ------------------------------------------------------------------
        score_y: int = grid.height + 3
        score_x: int = 0
        score_text: str = f"Score: {score}"
        self.window.addstr(score_y, score_x, score_text)

        # ------------------------------------------------------------------
        # Draw the game over message if needed
        # ------------------------------------------------------------------
        if game_over:
            msg: str = "GAME OVER! Press any key to exit."
            msg_y: int = grid.height // 2 + 1
            msg_x: int = (grid.width - len(msg)) // 2 + 1
            self.window.addstr(msg_y, msg_x, msg)

        # Refresh the window to display all changes.
        self.window.refresh()
