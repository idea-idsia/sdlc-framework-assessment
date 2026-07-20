import sys

import pygame


class SnakeGame:
    def __init__(self):
        self.snake = [(0, 0), (1, 0), (2, 0)]
        self.direction = 'right'
        self.food = None
        self.score = 0

    def update(self):
        # Update snake position based on direction
        head = self.snake[-1]
        if self.direction == 'up':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'down':
            new_head = (head[0] + 1, head[1])
        elif self.direction == 'left':
            new_head = (head[0], head[1] - 1)
        elif self.direction == 'right':
            new_head = (head[0], head[1] + 1)

        # Check for collision with food
        if new_head == self.food:
            self.score += 10
            self.food = None
            self.generate_food()
        else:
            self.snake.append(new_head)
            if len(self.snake) > 3:
                self.snake.pop(0)

    def generate_food(self):
        # Randomly generate food position
        import random
        self.food = (random.randint(0, 19), random.randint(0, 39))

    def draw(self, screen):
        # Draw snake and food on the screen
        for x, y in self.snake:
            pygame.draw.rect(screen, (0, 255, 0), (x * 20, y * 20, 20, 20))
        if self.food:
            pygame.draw.rect(screen, (255, 0, 0), (self.food[0] * 20, self.food[1] * 20, 20, 20))

class Game:
    def __init__(self):
        self.snake_game = SnakeGame()
        self.screen = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake_game.direction != 'down':
                        self.snake_game.direction = 'up'
                    elif event.key == pygame.K_DOWN and self.snake_game.direction != 'up':
                        self.snake_game.direction = 'down'
                    elif event.key == pygame.K_LEFT and self.snake_game.direction != 'right':
                        self.snake_game.direction = 'left'
                    elif event.key == pygame.K_RIGHT and self.snake_game.direction != 'left':
                        self.snake_game.direction = 'right'

            self.snake_game.update()
            self.screen.fill((0, 0, 0))
            self.snake_game.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(10)

    def get_score(self):
        return self.snake_game.score