import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 600
HEIGHT = 600
ROWS = 20
COLUMNS = 20
CELL_SIZE = WIDTH // COLUMNS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLUMNS):
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, BLACK, rect, 1)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(COLUMNS // 2, ROWS // 2 - 1), (COLUMNS // 2, ROWS // 2), (COLUMNS // 2, ROWS // 2 + 1)]
        self.direction = 'down'

    def draw(self, window):
        for pos in self.body:
            rect = (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, GREEN, rect)

# Food class
class Food:
    def __init__(self, snake):
        self.pos = self.generate_food_pos(snake)

    def generate_food_pos(self, snake):
        while True:
            pos = (random.randint(0, COLUMNS - 1), random.randint(0, ROWS - 1))
            if pos not in snake.body:
                return pos

    def draw(self, window):
        rect = (self.pos[0] * CELL_SIZE, self.pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(window, RED, rect)

# Initialize snake and food
snake = Snake()
food = Food(snake)
score = 0
high_score = 0

# Main loop to display the grid, snake, and food
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'

    # Move the snake
    head = snake.body[-1]
    if snake.direction == 'up':
        new_head = (head[0], head[1] - 1)
    elif snake.direction == 'down':
        new_head = (head[0], head[1] + 1)
    elif snake.direction == 'left':
        new_head = (head[0] - 1, head[1])
    elif snake.direction == 'right':
        new_head = (head[0] + 1, head[1])

    snake.body.append(new_head)

    # Check if the snake has consumed food
    if new_head == food.pos:
        score += 1
        if score > high_score:
            high_score = score
        food = Food(snake)
    else:
        snake.body.pop(0)

    # Keep the snake within the grid and check for collision with itself
    if (new_head[0] < 0 or new_head[0] >= COLUMNS or
            new_head[1] < 0 or new_head[1] >= ROWS or
            new_head in snake.body[:-1]):
        print(f'Game Over! Final Score: {score}')
        pygame.quit()
        sys.exit()

    window.fill(WHITE)
    draw_grid()
    snake.draw(window)
    food.draw(window)

    # Display score and high score
    text = font.render(f'Score: {score}', True, BLACK)
    window.blit(text, (10, 10))
    text = font.render(f'High Score: {high_score}', True, BLACK)
    window.blit(text, (10, 40))
    pygame.display.update()
    pygame.time.delay(100)
