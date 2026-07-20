import pygame
import random
import time

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define grid size and block size
GRID_SIZE = 20
BLOCK_SIZE = 20

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * BLOCK_SIZE, GRID_SIZE * BLOCK_SIZE))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Snake initialization
snake_body = [[5, 5]]  # Initial snake body (list of coordinates)
snake_direction = "right"  # Initial direction

# Food initialization
food_position = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]

# Score
score = 0
font = pygame.font.Font(None, 36)  # Using default font and size 36

def generate_food():
    """Generates food at a random position, ensuring it's not on the snake's body."""
    while True:
        new_food = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        if new_food not in snake_body:
            return new_food

def draw_grid():
    """Draws the grid lines."""
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, WHITE, (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, GRID_SIZE * BLOCK_SIZE))
        pygame.draw.line(screen, WHITE, (0, i * BLOCK_SIZE), (GRID_SIZE * BLOCK_SIZE, i * BLOCK_SIZE))

def draw_snake(snake_body):
    """Draws the snake on the screen."""
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food_position):
    """Draws the food on the screen."""
    pygame.draw.rect(screen, RED, (food_position[0] * BLOCK_SIZE, food_position[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def display_score(score):
    """Displays the score on the screen."""
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))  # Position the score in the top-left corner

def game_over_screen(screen, score):
    """Displays a game over message and restart option."""
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over!", True, RED)
    text_rect = text.get_rect(center=(GRID_SIZE * BLOCK_SIZE // 2, GRID_SIZE * BLOCK_SIZE // 2))
    screen.blit(text, text_rect)

    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_rect = score_text.get_rect(center=(GRID_SIZE * BLOCK_SIZE // 2, GRID_SIZE * BLOCK_SIZE // 2 + 50))
    screen.blit(score_text, score_rect)

    restart_text = font.render("Press 'R' to Restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(GRID_SIZE * BLOCK_SIZE // 2, GRID_SIZE * BLOCK_SIZE // 2 + 100))
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart the game

# Main game loop
def main():
    game_running = True
    game_over = False

    global score
    score = 0
    snake_body = [[5, 5]]
    snake_direction = "right"
    food_position = generate_food()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != "right":
                    snake_direction = "left"
                if event.key == pygame.K_RIGHT and snake_direction != "left":
                    snake_direction = "right"
                if event.key == pygame.K_UP and snake_direction != "down":
                    snake_direction = "up"
                if event.key == pygame.K_DOWN and snake_direction != "up":
                    snake_direction = "down"

        # Update snake position
        head = snake_body[0]
        if snake_direction == "left":
            new_head = [head[0] - 1, head[1]]
        elif snake_direction == "right":
            new_head = [head[0] + 1, head[1]]
        elif snake_direction == "up":
            new_head = [head[0], head[1] - 1]
        elif snake_direction == "down":
            new_head = [head[0], head[1] + 1]

        # Check for collision with boundaries
        if (
            new_head[0] < 0
            or new_head[0] >= GRID_SIZE
            or new_head[1] < 0
            or new_head[1] >= GRID_SIZE
            or new_head in snake_body
        ):
            game_over = True
            break

        snake_body.insert(0, new_head)  # Add new head to the snake

        # Check for food consumption
        if new_head == food_position:
            score += 1
            food_position = generate_food()
        else:
            snake_body.pop()  # Remove the tail segment if no food eaten

        # Draw everything
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake_body)
        draw_food(food_position)
        display_score(score)

        pygame.display.flip()
        clock.tick(15)  # Control game speed (frames per second)

    if game_over:
        game_over_screen(screen, score)
        restart = True  # Reset the 'restart' flag

    pygame.quit()

if __name__ == "__main__":
    main()