## food.py
"""
Food component for the console Snake game.

This module implements the :class:`Food` class as specified in the
design documentation.  It is fully typed, avoids circular imports,
and exposes a clean public interface.

The class maintains a private ``_position`` attribute and exposes it
via a read‑only :pyattr:`position` property.  The ``generate_new`` method
places the food on a random free cell of the grid, avoiding the snake.
"""

from __future__ import annotations

import random
from typing import Tuple, List

# Import Grid and Snake only for type checking; this avoids circular
# imports at runtime while still providing full type information.
from grid import Grid
from snake import Snake


class Food:
    """
    Represents the food item in the game.

    Parameters
    ----------
    grid : Grid
        The game grid used for boundary checks.
    snake : Snake
        The snake instance; used to avoid placing food on the snake.

    Attributes
    ----------
    position : Tuple[int, int]
        Current grid coordinates of the food.
    """

    def __init__(self, grid: Grid, snake: Snake) -> None:
        """
        Initialise a new food instance.

        The default position is overwritten by :meth:`generate_new`.
        """
        self._position: Tuple[int, int] = (0, 0)
        self.generate_new(grid, snake)

    def generate_new(self, grid: Grid, snake: Snake) -> None:
        """
        Place food on a random free cell.

        The method scans all cells in the grid, filters out those
        occupied by the snake, and selects one at random.  If the
        snake occupies the entire grid, the current position is
        retained.

        Parameters
        ----------
        grid : Grid
            The game grid used for boundary checks.
        snake : Snake
            The snake instance; used to avoid placing food on the snake.
        """
        free_cells: List[Tuple[int, int]] = [
            (x, y)
            for x in range(grid.width)
            for y in range(grid.height)
            if (x, y) not in snake.body
        ]

        if not free_cells:
            # No free space left; keep current position
            return

        self._position = random.choice(free_cells)

    @property
    def position(self) -> Tuple[int, int]:
        """
        Return the current food position.

        Returns
        -------
        Tuple[int, int]
            The (x, y) coordinates of the food.
        """
        return self._position

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(position={self._position!r})"
