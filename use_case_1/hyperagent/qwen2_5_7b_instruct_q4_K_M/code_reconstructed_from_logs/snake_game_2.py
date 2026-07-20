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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'

        # Update the snake position based on direction
        head_x, head_y = snake_pos[0]
        if snake_direction == 'UP':
            head_y -= 1
        elif snake_direction == 'DOWN':
            head_y += 1
        elif snake_direction == 'LEFT':
            head_x -= 1
        elif snake_direction == 'RIGHT':
            head_x += 1

        # Add new head position to the front of the snake
        new_head = (head_x, head_y)
        snake_pos.insert(0, new_head)

        # Remove the tail if the snake does not eat food
        if new_head != food_pos:
            snake_pos.pop()

        # Draw snake and food
        draw_snake(snake_pos)
        pygame.draw.rect(screen, WHITE, (food_pos[0] * CELL_WIDTH, food_pos[1] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

        # Update display
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()