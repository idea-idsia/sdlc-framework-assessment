# Python
'''
This module contains the Game class.
It handles game logic, including game board creation, snake initialization, movement, collision detection, scoring, and game over conditions.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.snake = Snake()
        self.food = Food()
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = (1, 0)
            running = self.update()
            if not running:
                # Add game over logic here
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over!", True, (255, 255, 255))
                self.screen.fill((0, 0, 0))
                self.screen.blit(text, (10, 10))
                pygame.display.flip()
                pygame.time.wait(2000)  # wait for 2 seconds
                break
            self.render()
            clock.tick(10)
    def update(self):
        self.snake.move()
        if self.snake.collides_with_wall():
            print("Game Over: Snake collided with wall")
            return False
        elif self.snake.collides_with_self():
            print("Game Over: Snake collided with itself")
            return False
        elif self.snake.eats_food(self.food):
            self.snake.grow()
            self.snake.growing = False
            self.food.generate_new_position()
        return True
    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(len(self.snake.body)), True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        for pos in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (pos[0], pos[1], 20, 20))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food.position[0], self.food.position[1], 20, 20))
        pygame.display.flip()