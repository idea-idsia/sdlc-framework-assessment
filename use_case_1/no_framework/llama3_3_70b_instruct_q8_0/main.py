import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 10

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up font
font = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = "RIGHT"
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE
            y = random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE
            if (x, y) not in self.snake:
                return x, y

    def draw_grid(self):
        for i in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(win, WHITE, (i, 0), (i, HEIGHT))
        for i in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(win, WHITE, (0, i), (WIDTH, i))

    def draw_snake(self):
        for pos in self.snake:
            pygame.draw.rect(win, GREEN, (pos[0], pos[1], GRID_SIZE, GRID_SIZE))

    def draw_food(self):
        pygame.draw.rect(win, RED, (self.food[0], self.food[1], GRID_SIZE, GRID_SIZE))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                    self.direction = "RIGHT"

    def update_snake(self):
        head = self.snake[-1]
        if self.direction == "UP":
            new_head = (head[0], head[1] - GRID_SIZE)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + GRID_SIZE)
        elif self.direction == "LEFT":
            new_head = (head[0] - GRID_SIZE, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + GRID_SIZE, head[1])

        self.snake.append(new_head)

        if self.snake[-1] == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

    def check_collision(self):
        head = self.snake[-1]
        if (head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT or
                head in self.snake[:-1]):
            return True
        return False

    def draw_score(self):
        text = font.render(f"Score: {self.score}", True, WHITE)
        win.blit(text, (10, 10))

def main():
    clock = pygame.time.Clock()
    game = SnakeGame()

    while True:
        game.handle_events()
        game.update_snake()

        if game.check_collision():
            win.fill((0, 0, 0))
            text = font.render("Game Over!", True, WHITE)
            win.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 18))
            pygame.display.update()
            time.sleep(1)
            break

        win.fill((0, 0, 0))
        game.draw_grid()
        game.draw_snake()
        game.draw_food()
        game.draw_score()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()