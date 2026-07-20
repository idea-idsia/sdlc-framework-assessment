"""
Main file for the Snake Game project.

This module contains the implementation of the Game class and UI class.
"""

import pygame
from typing import List, Tuple
from snake_game import SnakeGame, Direction  # Import SnakeGame and Direction from snake_game.py

class Game:
    """
    Represents the game state.

    Attributes:
        snake_game (SnakeGame): The snake game instance.
        score (int): The current score.
        game_over (bool): Whether the game is over.
    """

    def __init__(self, width: int = 800, height: int = 600):
        """
        Initializes the Game instance.

        Args:
            width (int): Width of the game board. Defaults to 800.
            height (int): Height of the game board. Defaults to 600.
        """
        self.snake_game = SnakeGame(width, height)
        self.score = 0
        self.game_over = False

    def update(self) -> None:
        """
        Updates the game state.

        Raises:
            ValueError: If the game is over.
        """
        if not self.game_over:
            self.snake_game.update()
            self.check_collision()
            self.check_score()

    def check_collision(self) -> None:
        """
        Checks for collision with the wall or itself.
        """
        head_x, head_y = self.snake_game.snake[-1]
        if (head_x < 0 or head_x >= self.snake_game.width or
                head_y < 0 or head_y >= self.snake_game.height or
                head_x in [x for x, y in self.snake_game.snake[:-1]]):
            self.game_over = True

    def check_score(self) -> None:
        """
        Checks if the score has increased.
        """
        if not self.game_over:
            self.score += 1

class UI:
    """
    Represents the user interface.

    Attributes:
        game (Game): The game instance.
        screen (pygame.Surface): The game screen.
    """

    def __init__(self, game: Game) -> None:
        """
        Initializes the UI instance.

        Args:
            game (Game): The game instance.
        """
        self.game = game
        self.screen = pygame.display.set_mode((game.snake_game.width, game.snake_game.height))

    def draw(self) -> None:
        """
        Draws the game screen.
        """
        self.screen.fill((0, 0, 0))
        for x, y in self.game.snake_game.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (x, y, 10, 10))
        if self.game.food:
            pygame.draw.rect(self.screen, (255, 0, 0), (*self.game.food, 10, 10))
        pygame.display.update()

def main() -> None:
    """
    Main function.
    """
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()
    ui = UI(game)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake_game.change_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    game.snake_game.change_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    game.snake_game.change_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.snake_game.change_direction(Direction.RIGHT)
        ui.draw()
        if not game.game_over:
            game.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
