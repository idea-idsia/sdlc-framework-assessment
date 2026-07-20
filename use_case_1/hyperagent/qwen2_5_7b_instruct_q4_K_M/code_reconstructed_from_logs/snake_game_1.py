import pygame

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 10
CELL_WIDTH = 50
CELL_HEIGHT = 50
SCREEN_WIDTH = GRID_SIZE * CELL_WIDTH
SCREEN_HEIGHT = GRID_SIZE * CELL_HEIGHT

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake initialization
snake_pos = [(GRID_SIZE // 2, GRID_SIZE // 2)]
snake_direction = 'RIGHT'

# Food initialization
food_pos = (0, 0)

def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(screen, WHITE, (pos[0] * CELL_WIDTH, pos[1] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw snake and food (for now, just drawing the initial positions)
        draw_snake(snake_pos)
        pygame.draw.rect(screen, WHITE, (food_pos[0] * CELL_WIDTH, food_pos[1] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

        # Update display
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()