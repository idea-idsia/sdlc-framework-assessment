import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the width and height of each snake segment
SEGMENT_SIZE = 20

# Set the dimensions of the grid
GRID_WIDTH = 30
GRID_HEIGHT = 20

# Set the margin between the grid and the window border
MARGIN = 50

# Set the size of the window
WINDOW_SIZE = (GRID_WIDTH * SEGMENT_SIZE + 2 * MARGIN, GRID_HEIGHT * SEGMENT_SIZE + 2 * MARGIN)

# Create a window with the specified size
window = pygame.display.set_mode(WINDOW_SIZE)

# Set the font for the score text
font = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            food_x = random.randint(0, GRID_WIDTH - 1) * SEGMENT_SIZE + MARGIN
            food_y = random.randint(0, GRID_HEIGHT - 1) * SEGMENT_SIZE + MARGIN
            if (food_x, food_y) not in self.snake:
                return (food_x, food_y)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.direction = 'RIGHT'
                elif event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.direction = 'DOWN'

        head_x, head_y = self.snake[-1]
        if self.direction == 'LEFT':
            new_head = (head_x - SEGMENT_SIZE, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + SEGMENT_SIZE, head_y)
        elif self.direction == 'UP':
            new_head = (head_x, head_y - SEGMENT_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + SEGMENT_SIZE)

        self.snake.append(new_head)

        if self.food == new_head:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

        if (new_head[0] < MARGIN or new_head[0] >= GRID_WIDTH * SEGMENT_SIZE + MARGIN or
                new_head[1] < MARGIN or new_head[1] >= GRID_HEIGHT * SEGMENT_SIZE + MARGIN or
                new_head in self.snake[:-1]):
            return False

        return True

    def draw(self):
        window.fill(BLACK)
        for x, y in self.snake:
            pygame.draw.rect(window, GREEN, (x, y, SEGMENT_SIZE, SEGMENT_SIZE))
        pygame.draw.rect(window, RED, (*self.food, SEGMENT_SIZE, SEGMENT_SIZE))

        score_text = font.render(f'Score: {self.score}', True, WHITE)
        window.blit(score_text, (MARGIN, MARGIN // 2))

        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    game = SnakeGame()

    while True:
        if not game.update():
            break
        game.draw()
        clock.tick(10)

    window.fill(BLACK)
    game_over_text = font.render('Game Over!', True, WHITE)
    window.blit(game_over_text, (WINDOW_SIZE[0] // 2 - 50, WINDOW_SIZE[1] // 2))
    pygame.display.update()

    time.sleep(2)

if __name__ == '__main__':
    main()