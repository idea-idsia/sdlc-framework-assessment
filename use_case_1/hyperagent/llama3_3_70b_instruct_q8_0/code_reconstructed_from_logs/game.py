import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (255, 255, 255)
FOOD_COLOR = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font for the score
font = pygame.font.Font(None, 36)

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Set up the snake and food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
direction = 'RIGHT'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move the snake
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - 20)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + 20)
    elif direction == 'LEFT':
        new_head = (head[0] - 20, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + 20, head[1])

    snake.append(new_head)

    # Check if the snake has eaten the food
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - 20) // 20 * 20, random.randint(0, HEIGHT - 20) // 20 * 20)
    else:
        snake.pop(0)

    # Check for collisions with the edge of the screen
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT):
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Check for collisions with the snake's body
    if snake[-1] in snake[:-1]:
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    for x, y in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, 20, 20))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], 20, 20))

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(10)