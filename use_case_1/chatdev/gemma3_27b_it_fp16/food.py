'''
Represents the food in the game.
'''
import pygame
import random
class Food:
    def __init__(self, width, height, snake):
        """
        Initializes the food.
        Args:
            width: The width of the game screen.
            height: The height of the game screen.
            snake: The snake object.
        """
        self.width = width
        self.height = height
        self.snake = snake
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.spawn()
    def spawn(self):
        """
        Spawns the food at a random location, avoiding the snake's body.
        """
        while True:
            self.rect.x = random.randint(0, self.width - 20)
            self.rect.y = random.randint(0, self.height - 20)
            collision = False
            for body_part in self.snake.body:
                if self.rect.colliderect(body_part):
                    collision = True
                    break
            if not collision:
                break