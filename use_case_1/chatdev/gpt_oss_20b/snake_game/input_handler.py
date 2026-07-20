## input_handler.py
"""
InputHandler component for the console Snake game.

This module implements the :class:`InputHandler` class as specified in
the design documentation.  The implementation is fully typed, avoids
circular imports, and follows the public interface exactly.
"""

from __future__ import annotations

import curses
from typing import Any, Tuple

# No runtime imports from other game modules to avoid circular dependencies.
# The InputHandler only needs the curses module for key mapping constants.

class InputHandler:
    """
    Handles user input and translates it into snake movement directions.

    Attributes
    ----------
    last_direction : Tuple[int, int]
        The most recent direction chosen by the player.  This value
        is updated only when a valid key press is received and the
        direction does not reverse the snake.
    """

    __slots__ = ("last_direction",)

    def __init__(self) -> None:
        """
        Initialise a new InputHandler instance.

        The default direction is set to (0, 0) which represents no
        movement.  This value is overwritten as soon as a valid key
        is pressed.
        """
        self.last_direction: Tuple[int, int] = (0, 0)

    def get_direction(self, key: int) -> Tuple[int, int]:
        """
        Translate a key press into a movement direction.

        Parameters
        ----------
        key : int
            The key code returned by :func:`curses.getch`.

        Returns
        -------
        Tuple[int, int]
            The new direction as a (dx, dy) pair.  If the key press
            does not correspond to a recognised arrow key, the
            previous direction is returned unchanged.
        """
        # Mapping of key codes to direction vectors.
        # The values are defined as (dx, dy) where dx is horizontal
        # movement and dy is vertical movement.
        mapping: dict[int, Tuple[int, int]] = {
            curses.KEY_UP: (0, -1),
            curses.KEY_DOWN: (0, 1),
            curses.KEY_LEFT: (-1, 0),
            curses.KEY_RIGHT: (1, 0),
        }

        # Retrieve the new direction from the mapping; if the key is
        # not present, keep the current direction.
        new_direction: Tuple[int, int] = mapping.get(key, self.last_direction)

        # Prevent the snake from reversing onto itself.  A 180°
        # reversal would be indicated by the new direction being the
        # negative of the current direction.
        cur_dx: int = self.last_direction[0]
        cur_dy: int = self.last_direction[1]
        new_dx: int = new_direction[0]
        new_dy: int = new_direction[1]

        if (new_dx, new_dy) != (-cur_dx, -cur_dy):
            self.last_direction = new_direction

        return self.last_direction
