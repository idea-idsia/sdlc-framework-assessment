import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 10
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE
            y = random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def draw_grid(self):
        for i in range(WIDTH // GRID_SIZE + 1):
            pygame.draw.line(screen, (255, 255, 255), (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT))
        for i in range(HEIGHT // GRID_SIZE + 1):
            pygame.draw.line(screen, (255, 255, 255), (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))

    def draw_snake(self):
        for x, y in self.snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.circle(screen, SNAKE_COLOR, ((x + GRID_SIZE // 2), (y + GRID_SIZE // 2)), GRID_SIZE // 4)

    def draw_food(self):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.food, *GRID_SIZE))

    def check_collision(self):
        head_x, head_y = self.snake[-1]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        for x, y in self.snake[:-1]:
            if (x, y) == (head_x, head_y):
                return True
        return False

    def update_score(self):
        global font
        text = font.render(f'Score: {self.score}', 1, (255, 255, 255))
        screen.blit(text, (10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.direction = 'RIGHT'

    def update_game_state(self):
        head_x, head_y = self.snake[-1]
        if self.direction == 'UP':
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + GRID_SIZE, head_y)

        if self.check_collision():
            return False

        self.snake.append(new_head)
        if self.food == new_head:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

        return True

    def run(self):
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((0, 0, 0))

            self.draw_grid()
            self.draw_snake()
            self.draw_food()

            self.handle_events()
            self.update_game_state()

            if self.check_collision():
                text = font.render('Game Over', 1, (255, 255, 255))
                screen.blit(text, ((WIDTH - 100) // 2, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                return

            self.update_score()

            pygame.display.flip()
            clock.tick(10)

game = SnakeGame()
game.run()