"""
This module contains the Food class, which represents the food object in the game.
"""

import pygame
import random

class Food:
    """
    Represents the food with its position on the board.
    
    Attributes:
        x (int): The x-coordinate of the food's position.
        y (int): The y-coordinate of the food's position.
        board_width (int): The width of the board.
        board_height (int): The height of the board.
    """

    def __init__(self, board_width: int = 20, board_height: int = 20):
        """
        Initializes a new Food instance with a random position on the board.

        Args:
            board_width (int, optional): The width of the board. Defaults to 20.
            board_height (int, optional): The height of the board. Defaults to 20.
        """
        self.board_width: int = board_width
        self.board_height: int = board_height
        self.x: int = random.randint(0, board_width - 1)
        self.y: int = random.randint(0, board_height - 1)

    def generate_new_position(self, snake_body):
        """
        Generates a new random position for the food on the board.

        Args:
            snake_body (list): The body of the snake.
        """
        while True:
            self.x = random.randint(0, self.board_width - 1)
            self.y = random.randint(0, self.board_height - 1)
            if (0 <= self.x < self.board_width and 
                0 <= self.y < self.board_height and 
                not self.check_overlap(snake_body)):
                break

    def check_overlap(self, snake_body):
        """
        Checks if the food position overlaps with the snake's body.

        Args:
            snake_body (list): The body of the snake.

        Returns:
            bool: True if the food position overlaps with the snake's body, False otherwise.
        """
        for x, y in snake_body:
            if x == self.x and y == self.y:
                return True
        return False

    def draw_food(self, screen: pygame.Surface):
        """
        Draws the food on the given Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame screen to draw the food on.
        """
        cell_size = 20  # Default cell size
        rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), rect)

# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    food = Food(20, 20)
    snake_body = [[5, 5], [4, 5], [3, 5]]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black color
        food.draw_food(screen)  # Draw the food on the screen

        # Regenerate food position every second
        if random.random() < 0.01:
            food.generate_new_position(snake_body)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
