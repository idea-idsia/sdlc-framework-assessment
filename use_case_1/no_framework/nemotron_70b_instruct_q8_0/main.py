import pygame
import sys
import random
import time

# Game Constants
GRID_SIZE = 10
BLOCK_SIZE = 40
FPS = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((GRID_SIZE*BLOCK_SIZE, GRID_SIZE*BLOCK_SIZE))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake_pos = [200, 200]
        self.snake_body = [[200, 200], [220, 200], [240, 200]]
        self.food_pos = self.generate_food()
        self.direction = 'RIGHT'
        self.score = 0

    def generate_food(self):
        while True:
            pos = [random.randint(0, GRID_SIZE-1)*BLOCK_SIZE, random.randint(0, GRID_SIZE-1)*BLOCK_SIZE]
            if pos not in self.snake_body:
                return pos

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_SPACE:
                        self.reset_game()

            # Move the snake
            if self.direction == 'RIGHT':
                self.snake_pos[0] += BLOCK_SIZE
            elif self.direction == 'LEFT':
                self.snake_pos[0] -= BLOCK_SIZE
            elif self.direction == 'UP':
                self.snake_pos[1] -= BLOCK_SIZE
            elif self.direction == 'DOWN':
                self.snake_pos[1] += BLOCK_SIZE

            self.snake_body.insert(0, list(self.snake_pos))

            # Check for collisions with food
            if self.snake_pos == self.food_pos:
                self.score += 1
                self.food_pos = self.generate_food()
            else:
                self.snake_body.pop()

            # Check for collisions with wall or itself
            if (self.snake_pos[0] < 0 or self.snake_pos[0] >= GRID_SIZE*BLOCK_SIZE) or \
               (self.snake_pos[1] < 0 or self.snake_pos[1] >= GRID_SIZE*BLOCK_SIZE) or \
               self.snake_pos in self.snake_body[1:]:
                print(f"Game Over! Final Score: {self.score}")
                time.sleep(2)
                self.reset_game()

            # Draw everything
            self.display.fill(BLACK)
            for pos in self.snake_body:
                pygame.draw.rect(self.display, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {self.score}", True, WHITE)
            self.display.blit(text, (10, 10))

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = SnakeGame()
    game.play()