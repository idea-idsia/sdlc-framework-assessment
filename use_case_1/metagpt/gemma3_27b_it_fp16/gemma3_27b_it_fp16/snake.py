## snake.py
import pygame

class Snake:
    """
    Represents the snake.
    """

    def __init__(self, start_position: tuple = (10, 10), color: tuple = (0, 255, 0)):
        """
        Initializes the snake.

        Args:
            start_position (tuple, optional): The starting position of the snake. Defaults to (10, 10).
            color (tuple, optional): The color of the snake. Defaults to green.
        """
        self.body = [start_position]
        self.direction = (1, 0)  # Initial direction: right
        self.color = color

    def move(self):
        """
        Moves the snake in the current direction.
        """
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the tail

    def grow(self):
        """
        Grows the snake by adding a new segment to the tail.
        """
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

    def check_collision(self, width: int, height: int) -> bool:
        """
        Checks if the snake has collided with the walls or itself.

        Args:
            width (int): The width of the game board in blocks.
            height (int): The height of the game board in blocks.

        Returns:
            bool: True if the snake has collided, False otherwise.
        """
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    def draw(self, screen: pygame.Surface, block_size: int):
        """
        Draws the snake on the screen.

        Args:
            screen (pygame.Surface): The screen to draw the snake on.
            block_size (int): The size of each block in pixels.
        """
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(screen, self.color, (x * block_size, y * block_size, block_size, block_size))

    def get_head_position(self) -> tuple:
        """
        Returns the position of the snake's head.

        Returns:
            tuple: The position of the snake's head.
        """
        return self.body[0]
