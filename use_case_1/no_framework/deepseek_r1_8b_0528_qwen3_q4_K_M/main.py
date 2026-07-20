import pygame
import random
import sys
from pygame.locals import *

# Initialize constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors (RGB)
BACKGROUND_COLOR = (15, 56, 90)
GRID_COLOR = (30, 60, 100)
SNAKE_HEAD_COLOR = (42, 237, 18)  # Light green
SNAKE_BODY_COLOR = (42, 200, 100)  # Medium green
FOOD_COLOR = (255, 50, 50)  # Red

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

FPS = 8  # Game speed (frames per second)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset the snake to its initial state"""
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.score = 0

        # Initialize with a base body (snake head at center)
        for i in range(1, self.length):
            self.positions.append((self.positions[0][0] - i * self.direction[0],
                                   self.positions[0][1] - i * self.direction[1]))

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        """Update the snake's position based on current direction"""
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0] + x) % GRID_WIDTH  # Wrap around horizontally
        new_y = (head[1] + y) % GRID_HEIGHT  # Wrap around vertically

        # Check if snake collides with itself
        if len(self.positions) > 2 and (new_x, new_y) in self.positions[:-1]:
            return False  # Game over condition

        # Update positions: insert at beginning and remove the last one to maintain length
        self.positions.insert(0, (new_x, new_y))

        # If snake hasn't grown yet this movement, remove the tail segment
        if len(self.positions) > self.length:
            self.positions.pop()

        return True  # Game continues

    def draw(self, surface):
        """Draw the snake on the game board"""
        for i, p in enumerate(self.positions):
            rect = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))

            if i == 0:  # Snake head
                pygame.draw.rect(surface, SNAKE_HEAD_COLOR, rect)
                pygame.draw.rect(surface, BACKGROUND_COLOR, rect, 1)  # Border

                # Draw eyes on the head based on direction
                eye_size = GRID_SIZE // 5
                if self.direction == RIGHT:
                    pygame.draw.circle(surface, (0, 0, 0), (rect.right - GRID_SIZE // 4, rect.top + GRID_SIZE // 3),
                                       eye_size)
                    pygame.draw.circle(surface, (0, 0, 0), (rect.right - GRID_SIZE // 4, rect.bottom - GRID_SIZE // 3),
                                       eye_size)
                elif self.direction == LEFT:
                    pygame.draw.circle(surface, (0, 0, 0), (rect.left + GRID_SIZE // 4, rect.top + GRID_SIZE // 3),
                                       eye_size)
                    pygame.draw.circle(surface, (0, 0, 0), (rect.left + GRID_SIZE // 4, rect.bottom - GRID_SIZE // 3),
                                       eye_size)
                elif self.direction == UP:
                    pygame.draw.circle(surface, (0, 0, 0), (rect.left + GRID_SIZE // 3, rect.top + GRID_SIZE // 4),
                                       eye_size)
                    pygame.draw.circle(surface, (0, 0, 0), (rect.right - GRID_SIZE // 3, rect.top + GRID_SIZE // 4),
                                       eye_size)
                elif self.direction == DOWN:
                    pygame.draw.circle(surface, (0, 0, 0), (rect.left + GRID_SIZE // 3, rect.bottom - GRID_SIZE // 4),
                                       eye_size)
                    pygame.draw.circle(surface, (0, 0, 0), (rect.right - GRID_SIZE // 3, rect.bottom - GRID_SIZE // 4),
                                       eye_size)
            else:  # Snake body segments
                pygame.draw.rect(surface, SNAKE_BODY_COLOR, rect)
                pygame.draw.rect(surface, BACKGROUND_COLOR, rect, 1)  # Border

    def change_direction(self, direction):
        """Change the snake's direction if it won't cause a collision"""
        head = self.get_head_position()

        # Prevent turning directly opposite to current direction (would hit itself instantly)
        if (direction[0] * -1, direction[1]) == self.direction:
            return

        self.direction = direction


class Food:
    def __init__(self):
        """Initialize food with random position"""
        self.position = None
        self.color = FOOD_COLOR
        self.randomize_position()

    def randomize_position(self):
        """Set the food to a new random position on grid, not where snake is"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.positions[:-1]:
                self.position = (x, y)
                break

    def draw(self, surface):
        """Draw the food on the game board"""
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE),
                           (GRID_SIZE, GRID_SIZE))

        # Draw apple-like shape
        pygame.draw.rect(surface, self.color, rect)

        # Add a stem to make it look like an apple
        stem_rect = pygame.Rect((self.position[0] * GRID_SIZE + GRID_SIZE // 2 - 1,
                                 self.position[1] * GRID_SIZE + GRID_SIZE // 3), (2, 5))
        pygame.draw.rect(surface, (46, 139, 87), stem_rect)  # Brown stem


def draw_grid(surface):
    """Draw the grid lines on the game board"""
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            rect = pygame.Rect((x, y), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BACKGROUND_COLOR, rect, 1)


def display_score(surface, score):
    """Display the current score on the game board"""
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    surface.blit(text, (10, 10))


def display_game_over(surface):
    """Display game over message"""
    # Semi-transparent overlay
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surface.blit(overlay, (0, 0))

    font_large = pygame.font.SysFont('Arial', 50)
    font_medium = pygame.font.SysFont('Arial', 30)

    game_over_text = font_large.render('GAME OVER!', True, (255, 50, 50))
    score_text = font_medium.render(f'Final Score: {snake.score}', True, (255, 255, 255))
    restart_text = font_medium.render('Press SPACE to Restart or ESC to Quit', True, (255, 255, 255))

    surface.blit(game_over_text,
                 (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2,
                  WINDOW_HEIGHT // 2 - 60))
    surface.blit(score_text,
                 (WINDOW_WIDTH // 2 - score_text.get_width() // 2,
                  WINDOW_HEIGHT // 2))
    surface.blit(restart_text,
                 (WINDOW_WIDTH // 2 - restart_text.get_width() // 2,
                  WINDOW_HEIGHT // 2 + 50))


def main():
    global snake

    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Handle arrow keys and restart/restart
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if game_over:
                    if event.key == K_SPACE:
                        snake.reset()
                        food.randomize_position()
                        game_over = False
                else:
                    if event.key == K_UP:
                        snake.change_direction(UP)
                    elif event.key == K_DOWN:
                        snake.change_direction(DOWN)
                    elif event.key == K_LEFT:
                        snake.change_direction(LEFT)
                    elif event.key == K_RIGHT:
                        snake.change_direction(RIGHT)

        # Update game state if not in game over
        if not game_over and snake.update():
            # Check for collision with food
            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 10

                # Add new position to keep the head at current position (snake grows)
                positions_to_add = [(food.position[0], food.position[1])]

                while len(snake.positions) > snake.length - 1 and all(
                        p != food.position for p in positions_to_add):
                    pass

                # Generate a new food after eating
                food.randomize_position()

        screen.fill(BACKGROUND_COLOR)

        if not game_over:
            draw_grid(screen)
            snake.draw(screen)
            food.draw(screen)
            display_score(screen, snake.score)

            # Check for boundary collision (game over condition)
            head = snake.get_head_position()
            if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
                game_over = True

        else:
            display_game_over(screen)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    game_over = False
    main()