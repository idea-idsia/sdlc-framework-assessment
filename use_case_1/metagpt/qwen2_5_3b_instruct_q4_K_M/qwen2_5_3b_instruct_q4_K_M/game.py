## game.py

import pygame
from snake import Snake  # Assuming Snake class is defined in snake.py
from food import Food    # Assuming Food class is defined in food.py

class Game:
    def __init__(self, width: int, height: int):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake = Snake(width, height)
        self.food = Food(width, height)
        self.score = 0

    def run(self):
        while True:
            self.handle_events()
            self.update_score(self.snake.body_length - 1)
            self.snake.move()
            if self.check_collision():
                break
            self.food.spawn()
            self.snake.grow() if self.snake.eat_food(self.food.position) else None
            self.draw()

    def update_score(self, new_score: int):
        self.score = new_score

    def draw(self):
        self.screen.fill((0, 255, 0))  # Fill the screen with green color
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def check_collision(self) -> bool:
        if self.snake.body_length == 1 and not self.snake.check_food_collision(self.food.position):
            return True
        for segment in self.snake.body[1:]:
            if self.snake.head().distance(segment) < 1:
                return True
        return False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction.y != 1:
                    self.snake.set_direction(pygame.math.Vector2(0, -1))
                elif event.key == pygame.K_DOWN and self.snake.direction.y != -1:
                    self.snake.set_direction(pygame.math.Vector2(0, 1))
                elif event.key == pygame.K_LEFT and self.snake.direction.x != 1:
                    self.snake.set_direction(pygame.math.Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT and self.snake.direction.x != -1:
                    self.snake.set_direction(pygame.math.Vector2(1, 0))

    def __del__(self):
        pygame.quit()
