import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 10

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the font
font = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = "RIGHT"
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            food = (x, y)
            if food not in self.snake:
                return food

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

    def move_snake(self):
        head = self.snake[-1]
        if self.direction == "UP":
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + BLOCK_SIZE)
        elif self.direction == "LEFT":
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + BLOCK_SIZE, head[1])

        self.snake.append(new_head)

        if self.food == new_head:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

    def check_collisions(self):
        head = self.snake[-1]
        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in self.snake[:-1]):
            return True
        return False

    def draw_everything(self):
        screen.fill((0, 0, 0))
        for pos in self.snake:
            pygame.draw.rect(screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    game = SnakeGame()

    while True:
        game.handle_events()
        game.move_snake()
        if game.check_collisions():
            text = font.render("Game Over!", True, WHITE)
            screen.fill((0, 0, 0))
            screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 18))
            pygame.display.flip()
            pygame.time.wait(2000)

            game = SnakeGame()

        game.draw_everything()
        clock.tick(FPS)

if __name__ == "__main__":
    main()