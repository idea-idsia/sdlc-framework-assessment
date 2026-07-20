"""
Snake Game Implementation
==========================

This module contains the implementation of the SnakeGame class and Direction enum.
"""

import pygame
from typing import List, Tuple

# Constants
WIDTH: int = 800
HEIGHT: int = 600
SNAKE_SIZE: int = 10
FOOD_SIZE: int = 10

class Direction:
    """
    Enum for snake direction.

    Attributes:
        UP (str): Up direction.
        DOWN (str): Down direction.
        LEFT (str): Left direction.
        RIGHT (str): Right direction.
    """

    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

class SnakeGame:
    """
    Represents the snake game.

    Attributes:
        width (int): Width of the game board.
        height (int): Height of the game board.
        snake (List[Tuple[int, int]]): Initial snake positions.
        direction (str): Initial snake direction.
        food (Tuple[int, int]): Food position.
    """

    def __init__(self, width: int = WIDTH, height: int = HEIGHT):
        """
        Initializes the SnakeGame instance.

        Args:
            width (int): Width of the game board. Defaults to 800.
            height (int): Height of the game board. Defaults to 600.
        """
        self.width = width
        self.height = height
        self.snake: List[Tuple[int, int]] = [(200, 200), (220, 200), (240, 200)]
        self.direction: str = Direction.RIGHT
        self.food: Tuple[int, int] = None

    def update(self) -> None:
        """
        Updates the snake game state.
        """

        # Move the snake based on the current direction
        head_x, head_y = self.snake[-1]
        if self.direction == Direction.UP:
            new_head = (head_x, head_y - SNAKE_SIZE)
        elif self.direction == Direction.DOWN:
            new_head = (head_x, head_y + SNAKE_SIZE)
        elif self.direction == Direction.LEFT:
            new_head = (head_x - SNAKE_SIZE, head_y)
        elif self.direction == Direction.RIGHT:
            new_head = (head_x + SNAKE_SIZE, head_y)

        # Check for collision with the wall or itself
        if (new_head[0] < 0 or new_head[0] >= self.width or
                new_head[1] < 0 or new_head[1] >= self.height or
                new_head in self.snake[:-1]):
            raise ValueError("Game over")

        # Update the snake positions
        self.snake.append(new_head)

        # Check if food is eaten
        if (self.food and self.snake[-1] == self.food):
            # Remove the food from the game board
            self.food = None
        else:
            # Remove the first element of the snake
            self.snake.pop(0)

    def change_direction(self, direction: Direction) -> None:
        """
        Changes the snake direction.

        Args:
            direction (Direction): New direction.
        """
        if direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = direction
        elif direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = direction
        elif direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = direction
        elif direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = direction

    def get_current_direction(self) -> Direction:
        """
        Returns the current snake direction.

        Returns:
            Direction: Current direction.
        """
        return self.direction
