import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20

# Create a game board
grid = [[0 for _ in range(HEIGHT // BLOCK_SIZE)] for _ in range(WIDTH // BLOCK_SIZE)]

class Snake:
    def __init__(self):
        self.direction = "right"
        self.position = [0, 0]
        self.length = 1

    def move(self):
        if self.direction == "up":
            new_position = [self.position[0], self.position[1] - BLOCK_SIZE]
        elif self.direction == "down":
            new_position = [self.position[0], self.position[1] + BLOCK_SIZE]
        elif self.direction == "left":
            new_position = [self.position[0] - BLOCK_SIZE, self.position[1]]
        else:
            new_position = [self.position[0] + BLOCK_SIZE, self.position[1]]

        # Ensure boundaries
        if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]):
            self.position = new_position

    def eat(self):
        self.length += 1
        self.position.append(self.position[-1])

def main():
    # Create a game board display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    food_x, food_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "down":
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN and snake.direction != "up":
                    snake.direction = "down"
                elif event.key == pygame.K_LEFT and snake.direction != "right":
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT and snake.direction != "left":
                    snake.direction = "right"

        # Update the snake's position
        if snake.length > 1:
            for i in range(snake.length - 2, 0, -1):
                snake.position[i] = snake.position[i-1]
        snake.move()

        # Check for collisions with food
        if (snake.position[-1][0], snake.position[-1][1]) == (food_x, food_y):
            snake.eat()
            food_x, food_y = pygame.random.randint(0, len(grid)-1), pygame.random.randint(0, len(grid[0])-1)

        # Display the game board and update it
        screen.fill((255, 255, 255))
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (x, y) == snake.position[-1]:
                    pygame.draw.rect(screen, (255, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                elif (x, y) == (food_x, food_y):
                    pygame.draw.rect(screen, (0, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Draw the score
        font = pygame.font.Font(None, 36)
        text = font.render(str(len(snake.length)), True, (10, 10, 10))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()