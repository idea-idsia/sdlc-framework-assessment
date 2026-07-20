"""
This module contains the Game class with methods for running the game, drawing the board, and handling user input.

Attributes:
    board (Board): The game's board instance.
    snake (Snake): The game's snake instance.
    food (Food): The game's food instance.
"""

import pygame
from board import Board
from snake import Snake
from food import Food

class Game:
    """
    A class representing the game.

    Attributes:
        board (Board): The game's board instance.
        snake (Snake): The game's snake instance.
        food (Food): The game's food instance.
    """

    def __init__(self):
        """
        Initializes a new Game instance.
        """
        self.board = Board()
        self.snake = Snake()
        self.food = Food(self.board)

    def run(self) -> None:
        """
        Runs the game.

        This method initializes the Pygame window, sets up the game loop, and handles user input.
        """
        pygame.init()
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.snake.handle_user_input(event)

            # Move the snake
            self.snake.move()

            # Check for collisions with the board or itself
            if self.snake.check_collision(self.board):
                print("Game Over")
                running = False

            # Check for collision with food
            if self.snake.check_food_collision(self.food):
                self.snake.grow()
                self.food.generate(self.snake.body)

            # Update the display
            self.board.screen.fill((0, 0, 0))  
            self.draw_board()
            self.food.draw()
            self.draw_snake()
            pygame.display.flip()
            clock.tick(10)

        pygame.quit()

    def draw_board(self) -> None:
        """
        Draws the game board.

        This method uses Pygame to draw a grid representing the game board.
        """
        for x in range(0, self.board.width, 20):
            pygame.draw.line(self.board.screen, (40, 40, 40), (x, 0), (x, self.board.height))
        for y in range(0, self.board.height, 20):
            pygame.draw.line(self.board.screen, (40, 40, 40), (0, y), (self.board.width, y))

    def draw_snake(self) -> None:
        """
        Draws the snake on the game board.

        This method uses Pygame to draw a green rectangle for each segment of the snake's body.
        """
        for pos in self.snake.body:
            pygame.draw.rect(self.board.screen, (0, 255, 0), (pos[0], pos[1], 20, 20))

# Example usage:
if __name__ == "__main__":
    game = Game()
    game.run()
