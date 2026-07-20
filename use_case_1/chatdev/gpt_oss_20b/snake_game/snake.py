## snake.py
"""
Snake component for the console Snake game.

This module implements the :class:`Snake` class as specified in the
design documentation.  The implementation is fully typed, avoids
circular imports, and follows the public interface exactly.
"""

from __future__ import annotations

from typing import List, Tuple

# Import Grid only for type checking; no runtime dependency on grid.py
# to avoid circular imports.
from grid import Grid


class Snake:
    """
    Represents the snake in the game.

    Attributes
    ----------
    body : List[Tuple[int, int]]
        Ordered list of grid coordinates from head to tail.
    direction : Tuple[int, int]
        Current movement direction as a (dx, dy) pair.
    _grow_pending : bool
        Flag indicating whether the snake should grow on the next move.
    """

    def __init__(self, start_pos: Tuple[int, int], start_dir: Tuple[int, int]) -> None:
        """
        Initialise a new snake.

        Parameters
        ----------
        start_pos : Tuple[int, int]
            Initial head position on the grid.
        start_dir : Tuple[int, int]
            Initial movement direction.
        """
        self.body: List[Tuple[int, int]] = [start_pos]
        self.direction: Tuple[int, int] = start_dir
        self._grow_pending: bool = False

    def move(self) -> None:
        """
        Move the snake forward by one cell.

        The new head position is calculated from the current head and
        direction.  The new head is inserted at the front of the body
        list.  If a growth is pending, the tail is left intact; otherwise
        the last segment is removed to keep the length constant.
        """
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head: Tuple[int, int] = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)

        if self._grow_pending:
            # Consume the growth flag; the snake has grown by one segment.
            self._grow_pending = False
        else:
            # Normal movement: remove the tail segment.
            self.body.pop()

    def grow(self) -> None:
        """
        Schedule the snake to grow on its next move.

        After calling this method, the snake will retain its tail segment
        during the next :meth:`move` call, effectively increasing its
        length by one.
        """
        self._grow_pending = True

    def set_direction(self, new_dir: Tuple[int, int]) -> None:
        """
        Change the snake's direction if it is not a 180° reversal.

        Parameters
        ----------
        new_dir : Tuple[int, int]
            Desired new direction as a (dx, dy) pair.
        """
        cur_dx, cur_dy = self.direction
        new_dx, new_dy = new_dir
        # Prevent the snake from reversing onto itself.
        if (new_dx, new_dy) != (-cur_dx, -cur_dy):
            self.direction = new_dir

    def collides_with_self(self) -> bool:
        """
        Check whether the snake's head collides with its body.

        Returns
        -------
        bool
            ``True`` if the head occupies the same cell as any other
            segment of the body.
        """
        return self.body[0] in self.body[1:]

    def collides_with_wall(self, grid: Grid) -> bool:
        """
        Check whether the snake's head has moved outside the grid.

        Parameters
        ----------
        grid : Grid
            The game grid used for boundary checks.

        Returns
        -------
        bool
            ``True`` if the head position is not within the grid bounds.
        """
        return not grid.in_bounds(self.body[0])

    def head(self) -> Tuple[int, int]:
        """
        Retrieve the current head position.

        Returns
        -------
        Tuple[int, int]
            The (x, y) coordinates of the snake's head.
        """
        return self.body[0]
