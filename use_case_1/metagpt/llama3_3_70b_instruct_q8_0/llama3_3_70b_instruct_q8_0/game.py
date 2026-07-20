"""
This module contains the Game class, which represents the main game loop and handles user input.
"""

import pygame
from board import Board
from snake import Snake
from food import Food

class Game:
    """
    Represents the game with its board, snake, food, and score.

    Attributes:
        board (Board): The game board.
        snake (Snake): The snake object.
        food (Food): The food object.
        score (int): The current score.
    """

    def __init__(self, width: int = 20, height: int = 20):
        """
        Initializes a new Game instance with the given width and height.

        Args:
            width (int, optional): The width of the board. Defaults to 20.
            height (int, optional): The height of the board. Defaults to 20.
        """
        self.board: Board = Board(width, height)
        self.snake: Snake = Snake()
        self.food: Food = Food(width, height)
        self.score: int = 0

    def run(self):
        """
        Runs the game loop.

        Note:
            This method initializes Pygame and handles user input.
        """
        pygame.init()
        screen = pygame.display.set_mode((400, 400))
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_events(event.key)

            screen.fill((0, 0, 0))  # Fill the screen with black color
            self.board.draw_grid()  # Draw the grid on the screen

            try:
                self.update()
            except ValueError as e:
                print(e)
                running = False

            if self.snake.check_collision_with_self():
                print("Snake collided with itself")
                running = False

            for x, y in self.snake.body:
                rect = pygame.Rect(x * 20, y * 20, 20, 20)
                pygame.draw.rect(screen, (255, 255, 255), rect)

            self.food.draw_food(screen)  # Draw the food on the screen

            pygame.display.flip()
            clock.tick(10)

        pygame.quit()

    def handle_events(self, key: int):
        """
        Handles user input events.

        Args:
            key (int): The pressed key.
        """
        if key == pygame.K_UP and self.snake.direction != 'down':
            self.snake.direction = 'up'
        elif key == pygame.K_DOWN and self.snake.direction != 'up':
            self.snake.direction = 'down'
        elif key == pygame.K_LEFT and self.snake.direction != 'right':
            self.snake.direction = 'left'
        elif key == pygame.K_RIGHT and self.snake.direction != 'left':
            self.snake.direction = 'right'

    def update(self):
        """
        Updates the game state.

        Note:
            This method moves the snake, checks for collisions with food, and updates the score.
        """
        self.snake.move(self.board.width, self.board.height)
        if (self.snake.body[0][0] == self.food.x and 
            self.snake.body[0][1] == self.food.y):
            self.score += 1
            self.snake.grow()
            self.food.generate_new_position(self.snake.body)

# Example usage:
if __name__ == "__main__":
    game = Game(20, 20)
    game.run()
