import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
    def __init__(self):
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'right'
        self.food = None
        self.score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def move_snake(self):
        head = self.snake[-1]
        if self.direction == 'right':
            new_head = (head[0] + 1, head[1])
        elif self.direction == 'left':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'up':
            new_head = (head[0], head[1] - 1)
        elif self.direction == 'down':
            new_head = (head[0], head[1] + 1)

        if new_head in self.snake or new_head[0] < 0 or new_head[0] >= GRID_SIZE or new_head[1] < 0 or new_head[1] >= GRID_SIZE:
            print("Game over!")
            return False

        self.snake.append(new_head)
        if self.food == new_head:
            self.score += 1
            self.generate_food()
        else:
            self.snake.pop(0)

        return True

    def draw_game(self):
        screen.fill(BLACK)
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        for pos in self.snake:
            pygame.draw.rect(screen, WHITE, (pos[0] * CELL_SIZE + 1, pos[1] * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        if self.food:
            pygame.draw.rect(screen, (255, 0, 0), (self.food[0] * CELL_SIZE + 1, self.food[1] * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(text, (10, 10))
        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    game = SnakeGame()
    game.generate_food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and game.direction != 'right':
                    game.direction = 'left'
                elif event.key == pygame.K_RIGHT and game.direction != 'left':
                    game.direction = 'right'
                elif event.key == pygame.K_UP and game.direction != 'down':
                    game.direction = 'up'
                elif event.key == pygame.K_DOWN and game.direction != 'up':
                    game.direction = 'down'

        if not game.move_snake():
            running = False
        game.draw_game()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()