"""
This module contains the Food class with methods for generating food, checking food collisions, and updating its position.

Attributes:
    x (int): The initial x-coordinate of the food.
    y (int): The initial y-coordinate of the food.
    board (Board): The game's board instance.
"""

import random
from board import Board

class Food:
    """
    A class representing the game's food.

    Attributes:
        x (int): The initial x-coordinate of the food.
        y (int): The initial y-coordinate of the food.
        board (Board): The game's board instance.
    """

    def __init__(self, board: Board):
        """
        Initializes a new Food instance.

        Args:
            board (Board): The game's board instance.
        """
        self.board = board
        self.x = 0
        self.y = 0
        self.generate()

    def generate(self, snake_body: list) -> None:
        """
        Generates a new food position on the board.

        This method randomly selects an empty space on the board as the new food position, ensuring it does not overlap with the snake's body.

        Args:
            snake_body (list): A list of tuples representing the x and y coordinates of the snake's body parts.
        """
        while True:
            self.x = random.randint(0, self.board.width - 20) // 20 * 20
            self.y = random.randint(0, self.board.height - 20) // 20 * 20
            # Check if the generated position overlaps with the snake's body
            if (self.x, self.y) not in snake_body:
                break

    def check_collision(self, snake_head: tuple) -> bool:
        """
        Checks if the food collides with the snake.

        Args:
            snake_head (tuple): The x and y coordinates of the snake's head.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        return (self.x, self.y) == snake_head

    def draw(self) -> None:
        """
        Draws the food on the board.

        This method uses Pygame to draw a red square representing the food.
        """
        pygame.draw.rect(self.board.screen, (255, 0, 0), (self.x, self.y, 20, 20))

    def update_position(self, snake_body: list) -> None:
        """
        Updates the food's position after being consumed by the snake.

        Args:
            snake_body (list): A list of tuples representing the x and y coordinates of the snake's body parts.
        """
        self.generate(snake_body)

# Example usage:
if __name__ == "__main__":
    import pygame
    from board import Board

    pygame.init()
    clock = pygame.time.Clock()

    board = Board()
    food = Food(board)
    snake_body = [(100, 100), (120, 100), (140, 100)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the board and food
        board.draw()
        food.draw()

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
