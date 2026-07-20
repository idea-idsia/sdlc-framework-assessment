## game.py

import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, width: int, height: int):
        """
        Initialize the game with a given screen size.
        
        :param width: Width of the game window
        :param height: Height of the game window
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake((100, 50))  # Starting position for the snake
        self.food = Food(width, height)
        self.score = 0

    def run(self):
        """
        Main game loop.
        """
        while True:
            self.update()
            self.draw()

    def update(self):
        """
        Update game state (move snake, check collision, generate new food if needed).
        """
        self.snake.move()
        
        # Check for collisions
        if self.snake.check_collision():
            pygame.quit()
            exit()  # Game over

        # Check if the snake eats the food
        if self.snake.body[-1] == self.food.position:
            self.snake.grow(self.food.position)
            self.score += 10
            self.food.generate_new_position(self.snake.body)

    def draw(self):
        """
        Draw game elements (snake, food) on the screen.
        """
        self.screen.fill((0, 0, 0))  # Clear the screen with black

        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 20, 20))

        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], 20, 20))

        # Display score
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()
        self.clock.tick(10)  # Cap the frame rate to 10 FPS
