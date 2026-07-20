"""
This module contains the Board class with methods for drawing the board and checking collisions.

Attributes:
    width (int): The width of the board.
    height (int): The height of the board.
    screen (pygame.display.set_mode): The Pygame screen object.
"""

import pygame

class Board:
    """
    A class representing the game board.

    Attributes:
        width (int): The width of the board.
        height (int): The height of the board.
        screen (pygame.display.set_mode): The Pygame screen object.
    """

    def __init__(self, width: int = 800, height: int = 600):
        """
        Initializes a new Board instance.

        Args:
            width (int, optional): The width of the board. Defaults to 800.
            height (int, optional): The height of the board. Defaults to 600.
        """
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        """
        Draws the game board.

        This method uses Pygame to draw a grid on the screen.
        """
        self.screen.fill((255, 255, 255))

        # Draw grid lines
        for i in range(0, self.width, 20):
            pygame.draw.line(self.screen, (200, 200, 200), (i, 0), (i, self.height))
        for i in range(0, self.height, 20):
            pygame.draw.line(self.screen, (200, 200, 200), (0, i), (self.width, i))

        pygame.display.flip()

    def check_collision(self, snake_body: list) -> bool:
        """
        Checks if the snake's position is outside the board or if it collides with itself.

        Args:
            snake_body (list): A list of tuples representing the x and y coordinates of the snake's body parts.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        # Check if the snake is outside the board
        head_x, head_y = snake_body[0]
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return True

        # Check if the snake collides with itself
        for body_part in snake_body[1:]:
            if body_part == (head_x, head_y):
                return True

        return False

    def update_game_state(self, snake_body: list) -> None:
        """
        Updates the game state after a move.

        Args:
            snake_body (list): A list of tuples representing the x and y coordinates of the snake's body parts.
        """
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # Draw grid lines
        for i in range(0, self.width, 20):
            pygame.draw.line(self.screen, (200, 200, 200), (i, 0), (i, self.height))
        for i in range(0, self.height, 20):
            pygame.draw.line(self.screen, (200, 200, 200), (0, i), (self.width, i))

        # Draw the snake's body
        for x, y in snake_body:
            pygame.draw.rect(self.screen, (0, 255, 0), (x, y, 20, 20))

        pygame.display.flip()

# Example usage:
if __name__ == "__main__":
    board = Board()
    clock = pygame.time.Clock()

    running = True
    snake_body = [(100, 100), (120, 100), (140, 100)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the snake
        new_head_x, new_head_y = snake_body[0]
        new_head_x += 20
        snake_body.insert(0, (new_head_x, new_head_y))
        snake_body.pop()

        # Check for collisions
        if board.check_collision(snake_body):
            print("Game Over")
            running = False

        # Update the game state
        board.update_game_state(snake_body)

        clock.tick(10)

    pygame.quit()
