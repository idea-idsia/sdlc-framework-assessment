"""
This module contains the Snake class, which represents the snake object in the game.
"""

import pygame
from typing import List

class Snake:
    """
    Represents the snake with its body and direction.
    
    Attributes:
        body (List[List[int]]): A list of coordinates representing the snake's body.
        direction (str): The current direction of the snake, either 'up', 'down', 'left', or 'right'.
    """

    def __init__(self):
        """
        Initializes a new Snake instance with default values.
        """
        self.body: List[List[int]] = [[5, 5], [4, 5], [3, 5]]
        self.direction: str = 'right'

    def move(self, board_width: int, board_height: int):
        """
        Moves the snake in its current direction.

        Note:
            This method modifies the snake's body and direction.
        """
        head_x, head_y = self.body[0]
        if self.direction == 'up':
            new_head = [head_x, head_y - 1]
        elif self.direction == 'down':
            new_head = [head_x, head_y + 1]
        elif self.direction == 'left':
            new_head = [head_x - 1, head_y]
        elif self.direction == 'right':
            new_head = [head_x + 1, head_y]

        # Collision detection with board edges
        if (new_head[0] < 0 or new_head[0] >= board_width or 
            new_head[1] < 0 or new_head[1] >= board_height):
            raise ValueError("Snake collided with the board edge")

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        """
        Grows the snake by adding a new segment to its body.

        Note:
            This method modifies the snake's body.
        """
        tail_x, tail_y = self.body[-1]
        if len(self.body) > 1:
            second_last_x, second_last_y = self.body[-2]
            if self.direction == 'up':
                new_tail = [tail_x, tail_y + 1]
            elif self.direction == 'down':
                new_tail = [tail_x, tail_y - 1]
            elif self.direction == 'left':
                new_tail = [tail_x + 1, tail_y]
            elif self.direction == 'right':
                new_tail = [tail_x - 1, tail_y]
        else:
            if self.direction == 'up':
                new_tail = [tail_x, tail_y + 1]
            elif self.direction == 'down':
                new_tail = [tail_x, tail_y - 1]
            elif self.direction == 'left':
                new_tail = [tail_x + 1, tail_y]
            elif self.direction == 'right':
                new_tail = [tail_x - 1, tail_y]

        self.body.append(new_tail)

    def check_collision_with_self(self):
        """
        Checks if the snake has collided with itself.

        Returns:
            bool: True if the snake has collided with itself, False otherwise.
        """
        head_x, head_y = self.body[0]
        for x, y in self.body[1:]:
            if x == head_x and y == head_y:
                return True
        return False

    def update_score(self):
        """
        Updates the game's score when the snake consumes food.

        Note:
            This method should be called after the snake has consumed food.
        """
        # TO DO: implement scoring system
        pass

# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    snake = Snake()
    board_width = 20
    board_height = 20
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black color
        for x, y in snake.body:
            rect = pygame.Rect(x * 20, y * 20, 20, 20)
            pygame.draw.rect(screen, (255, 255, 255), rect)

        try:
            snake.move(board_width, board_height)
        except ValueError as e:
            print(e)
            running = False

        if snake.check_collision_with_self():
            print("Snake collided with itself")
            running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
