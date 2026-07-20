"""
This module contains the Snake class with methods for moving the snake, checking collisions, and growing the snake.

Attributes:
    x (int): The initial x-coordinate of the snake.
    y (int): The initial y-coordinate of the snake.
    direction (str): The current direction of the snake ('up', 'down', 'left', or 'right').
    length (int): The current length of the snake.
"""

import pygame
from board import Board

class Snake:
    """
    A class representing the game's snake.

    Attributes:
        x (int): The initial x-coordinate of the snake.
        y (int): The initial y-coordinate of the snake.
        direction (str): The current direction of the snake ('up', 'down', 'left', or 'right').
        length (int): The current length of the snake.
    """

    def __init__(self, x: int = 100, y: int = 100):
        """
        Initializes a new Snake instance.

        Args:
            x (int, optional): The initial x-coordinate of the snake. Defaults to 100.
            y (int, optional): The initial y-coordinate of the snake. Defaults to 100.
        """
        self.x = x
        self.y = y
        self.direction = 'right'
        self.length = 1
        self.body = [(x, y)]

    def move(self) -> None:
        """
        Moves the snake in its current direction.

        This method updates the snake's position based on its current direction.
        """
        head_x, head_y = self.body[0]
        if self.direction == 'up':
            new_head_x, new_head_y = head_x, head_y - 20
        elif self.direction == 'down':
            new_head_x, new_head_y = head_x, head_y + 20
        elif self.direction == 'left':
            new_head_x, new_head_y = head_x - 20, head_y
        elif self.direction == 'right':
            new_head_x, new_head_y = head_x + 20, head_y

        self.body.insert(0, (new_head_x, new_head_y))
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self) -> None:
        """
        Increases the length of the snake.

        This method increments the snake's length by one unit.
        """
        self.length += 1

    def check_collision(self, board: Board) -> bool:
        """
        Checks if the snake collides with the board or itself.

        Args:
            board (Board): The game's board instance.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        head_x, head_y = self.body[0]
        # Check if the snake is outside the board
        if head_x < 0 or head_x >= board.width or head_y < 0 or head_y >= board.height:
            return True

        # Check if the snake collides with itself
        for body_part in self.body[1:]:
            if body_part == (head_x, head_y):
                return True

        return False

    def check_food_collision(self, food: 'Food') -> bool:
        """
        Checks if the snake collides with the food.

        Args:
            food (Food): The game's food instance.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        head_x, head_y = self.body[0]
        return (head_x, head_y) == (food.x, food.y)

    def update_direction(self, direction: str) -> None:
        """
        Updates the snake's direction.

        Args:
            direction (str): The new direction of the snake ('up', 'down', 'left', or 'right').
        """
        if direction in ['up', 'down', 'left', 'right'] and direction != self.get_opposite_direction():
            self.direction = direction

    def get_opposite_direction(self) -> str:
        """
        Gets the opposite direction of the snake's current direction.

        Returns:
            str: The opposite direction of the snake.
        """
        if self.direction == 'up':
            return 'down'
        elif self.direction == 'down':
            return 'up'
        elif self.direction == 'left':
            return 'right'
        elif self.direction == 'right':
            return 'left'

    def handle_user_input(self, event: pygame.event.Event) -> None:
        """
        Handles user input to change the snake's direction.

        Args:
            event (pygame.event.Event): The Pygame event object.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != 'down':
                self.update_direction('up')
            elif event.key == pygame.K_DOWN and self.direction != 'up':
                self.update_direction('down')
            elif event.key == pygame.K_LEFT and self.direction != 'right':
                self.update_direction('left')
            elif event.key == pygame.K_RIGHT and self.direction != 'left':
                self.update_direction('right')

# Example usage:
if __name__ == "__main__":
    import sys
    pygame.init()
    clock = pygame.time.Clock()

    board = Board()
    snake = Snake()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            snake.handle_user_input(event)

        # Move the snake
        snake.move()

        # Check for collisions
        if snake.check_collision(board):
            print("Game Over")
            running = False

        # Update the display
        board.update_display(snake.body)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()
