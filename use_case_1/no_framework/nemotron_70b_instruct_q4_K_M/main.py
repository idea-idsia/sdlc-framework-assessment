import pygame
import sys
import random
import time

# **Game Constants**
BLOCK_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.food_pos = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            food_pos = [random.randrange(1, (GRID_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                        random.randrange(1, (GRID_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
            if food_pos not in self.snake_body:
                return food_pos

    def draw_grid(self):
        for x in range(0, GRID_WIDTH * BLOCK_SIZE, BLOCK_SIZE):
            for y in range(0, GRID_HEIGHT * BLOCK_SIZE, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.display, WHITE, rect, 1)

    def draw_snake(self):
        for pos in self.snake_body:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    def show_score(self):
        font = pygame.font.SysFont('arial', 25)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        self.display.blit(score_text, (10, GRID_HEIGHT * BLOCK_SIZE - 30))

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.change_to = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.change_to = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.change_to = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.change_to = 'RIGHT'

            # Moving the snake
            if self.change_to == 'UP':
                self.snake_pos[1] -= BLOCK_SIZE
            elif self.change_to == 'DOWN':
                self.snake_pos[1] += BLOCK_SIZE
            elif self.change_to == 'LEFT':
                self.snake_pos[0] -= BLOCK_SIZE
            elif self.change_to == 'RIGHT':
                self.snake_pos[0] += BLOCK_SIZE

            self.direction = self.change_to

            # Extending the snake body
            self.snake_body.insert(0, list(self.snake_pos))
            if self.snake_pos == self.food_pos:
                self.score += 1
                self.food_pos = self.generate_food()
            else:
                self.snake_body.pop()

            # Collision with boundaries or itself
            if (self.snake_pos[0] < 0 or self.snake_pos[0] >= GRID_WIDTH * BLOCK_SIZE or
                    self.snake_pos[1] < 0 or self.snake_pos[1] >= GRID_HEIGHT * BLOCK_SIZE or
                    self.snake_pos in self.snake_body[1:]):
                time.sleep(1)
                print(f"Game Over! Final Score: {self.score}")
                self.reset_game()

            # Drawing everything
            self.display.fill(BLACK)
            self.draw_grid()
            self.draw_snake()
            self.draw_food()
            self.show_score()
            pygame.display.update()

            self.clock.tick(10)  # Controls the speed of the snake

if __name__ == "__main__":
    game = SnakeGame()
    game.play()