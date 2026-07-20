## grid.py
"""
Grid component for the console Snake game.

This module implements the :class:`Grid` class as specified in the
design documentation.  It is intentionally lightweight and free of
runtime dependencies on other game modules to avoid circular imports.
"""

from __future__ import annotations

from typing import Tuple


class Grid:
    """
    Represents the game board.

    Attributes
    ----------
    width : int
        Number of columns in the grid.
    height : int
        Number of rows in the grid.
    """

    __slots__ = ("width", "height")

    def __init__(self, width: int = 10, height: int = 10) -> None:
        """
        Initialise a new grid.

        Parameters
        ----------
        width : int, optional
            Grid width (default 10).
        height : int, optional
            Grid height (default 10).
        """
        self.width = width
        self.height = height

    def in_bounds(self, pos: Tuple[int, int]) -> bool:
        """
        Check whether a position lies inside the grid boundaries.

        Parameters
        ----------
        pos : Tuple[int, int]
            (x, y) coordinates to test.

        Returns
        -------
        bool
            ``True`` if the position is within the grid, otherwise
            ``False``.
        """
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def to_screen_coords(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Convert a grid coordinate to screen coordinates used by
        :class:`curses` rendering.

        The screen coordinate system places the origin (0, 0) at the
        top‑left corner of the visible area.  The grid is drawn
        starting at (1, 1) to leave room for a border.

        Parameters
        ----------
        pos : Tuple[int, int]
            (x, y) grid coordinate.

        Returns
        -------
        Tuple[int, int]
            (screen_y, screen_x) coordinate suitable for
            :func:`curses.addch` or :func:`curses.addstr`.
        """
        x, y = pos
        # Return screen coordinates with y first (row), then x (column)
        return (y, x)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(width={self.width!r}, height={self.height!r})"
