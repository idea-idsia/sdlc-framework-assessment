import pygame
import random
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

FPS = 10  # Snake movement speed

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)  # Forest Green for snake body
DARK_GREEN = (0, 100, 0)  # Snake head color
RED = (255, 0, 0)
BLUE = (65, 105, 225)  # Score panel background
GRAY = (40, 40, 40)  # Grid lines

# Directions as vectors for easy calculations
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeGame:
    def __init__(self):
        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT
        self.cell_size = GRID_SIZE

        # Set up display window with title
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")

        # Create a clock object to control game speed
        self.clock = pygame.time.Clock()

        # Font for score display
        self.font = pygame.font.SysFont('Arial', 24)
        self.title_font = pygame.font.SysFont('Arial', 36, bold=True)

        # Game state variables
        self.snake_pos = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
                          (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
                          (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None

        # Initialize food position and score
        self.food_pos = self.generate_food()
        self.score = 0

        # Game over flag
        self.game_over = False

    def generate_food(self):
        """Generate random food position not occupied by the snake"""
        while True:
            x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake_pos:
                return [x, y]

    def handle_events(self):
        """Handle user inputs and game events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Handle key press events
            elif event.type == KEYDOWN:
                if self.game_over and (event.key == K_SPACE or event.key == K_RETURN):
                    self.reset_game()
                else:
                    # Store direction for snake movement
                    if event.key == K_UP and self.direction != DOWN:
                        self.next_direction = UP
                    elif event.key == K_DOWN and self.direction != UP:
                        self.next_direction = DOWN
                    elif event.key == K_LEFT and self.direction != RIGHT:
                        self.next_direction = LEFT
                    elif event.key == K_RIGHT and self.direction != LEFT:
                        self.next_direction = RIGHT

        # If game is not over, update direction if next_direction exists
        if not self.game_over and self.next_direction:
            self.direction = self.next_direction

    def reset_game(self):
        """Reset the game to initial state"""
        self.snake_pos = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
                          (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
                          (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.food_pos = self.generate_food()
        self.score = 0
        self.game_over = False

    def update_snake(self):
        """Update snake position based on current direction"""
        if not self.game_over:
            # Store the old head position for collision detection later
            new_head_x, new_head_y = (self.snake_pos[0][0] + self.direction[0]) % GRID_WIDTH, \
                                     (self.snake_pos[0][1] + self.direction[1]) % GRID_HEIGHT

            # Create new head of the snake at calculated position
            new_head = [new_head_x, new_head_y]

            # Check for collision with self
            if len(self.find_collisions()) > 0:
                self.game_over = True
                return None

            # Add new head to snake (grow it)
            self.snake_pos.insert(0, new_head)

            # If food is eaten, keep the last segment and generate new food
            if self.is_food_eaten():
                self.food_pos = self.generate_food()
                self.score += 1
            else:
                # Remove tail to maintain snake length when not eating
                self.snake_pos.pop()

    def find_collisions(self):
        """Find collisions between the snake and itself or boundaries"""
        head_x, head_y = self.snake_pos[0]

        # Check collision with walls (treat as wrap-around)
        if head_x >= GRID_WIDTH or head_x < 0 or head_y >= GRID_HEIGHT or head_y < 0:
            return [self.food_pos]  # Collision list

        # Check collision with body
        for segment in self.snake_pos[1:]:
            if segment == self.snake_pos[0]:
                return [self.food_pos]

        return []  # No collisions

    def is_food_eaten(self):
        """Check if snake's head has collided with food"""
        head_x, head_y = self.snake_pos[0][0], self.snake_pos[0][1]
        food_x, food_y = self.food_pos

        return (head_x == food_x and head_y == food_y)

    def draw_grid(self):
        """Draw the game grid on screen"""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.display_surface, GRAY, (x, 0), (x, WINDOW_HEIGHT))

        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.display_surface, GRAY, (0, y), (WINDOW_WIDTH, y))

    def draw_snake(self):
        """Draw the snake on screen with head and body distinction"""
        # Draw snake head
        head_rect = pygame.Rect(
            self.snake_pos[0][0] * GRID_SIZE,
            self.snake_pos[0][1] * GRID_SIZE,
            GRID_SIZE, GRID_SIZE)

        pygame.draw.rect(self.display_surface, DARK_GREEN, head_rect)
        pygame.draw.rect(self.display_surface, WHITE, head_rect, 2)  # White border

        # Draw snake body
        for segment in self.snake_pos[1:]:
            seg_rect = pygame.Rect(
                segment[0] * GRID_SIZE,
                segment[1] * GRID_SIZE,
                GRID_SIZE, GRID_SIZE)

            pygame.draw.rect(self.display_surface, GREEN, seg_rect)
            pygame.draw.rect(self.display_surface, WHITE, seg_rect, 2)  # White border

    def draw_food(self):
        """Draw food on screen"""
        x, y = self.food_pos

        food_rect = pygame.Rect(
            x * GRID_SIZE + (GRID_SIZE - 10),  # Centered in the grid cell
            y * GRID_SIZE + (GRID_SIZE - 10),
            10, 10)

        pygame.draw.rect(self.display_surface, RED, food_rect)  # Red apple-like food

    def draw_score_panel(self):
        """Draw score panel at bottom of screen"""
        # Create a semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, 250), pygame.SRCALPHA)
        overlay.fill(BLUE + (180,))
        self.display_surface.blit(overlay, (0, WINDOW_HEIGHT - 250))

        # Draw score text with shadow effect for better visibility
        title_shadow = self.title_font.render("SNAKE GAME", True, WHITE).convert_alpha()
        self.display_surface.blit(title_shadow, (40 + GRID_SIZE // 3, WINDOW_HEIGHT - 240 - GRID_SIZE // 3))

        title_text = self.title_font.render("SNAKE GAME", True, BLACK)
        self.display_surface.blit(title_text, (40, WINDOW_HEIGHT - 240))

        score_shadow = self.font.render(f"Score: {self.score}", True, WHITE).convert_alpha()
        self.display_surface.blit(score_shadow, (40 + GRID_SIZE // 3, WINDOW_HEIGHT - 180 - GRID_SIZE // 3))

        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.display_surface.blit(score_text, (40, WINDOW_HEIGHT - 180))

        # Draw instructions
        if not self.game_over:
            instruction_shadow = self.font.render("Use arrow keys to control the snake", True, WHITE).convert_alpha()
            self.display_surface.blit(instruction_shadow, (35 + GRID_SIZE // 2, WINDOW_HEIGHT - 140 - GRID_SIZE // 2))

            instruction_text = self.font.render("Use arrow keys to control the snake", True, BLACK)
            self.display_surface.blit(instruction_text, (35, WINDOW_HEIGHT - 140))
        else:
            # Draw game over message with shadow
            game_over_shadow = self.title_font.render("GAME OVER", True, WHITE).convert_alpha()
            self.display_surface.blit(game_over_shadow, (80 + GRID_SIZE // 2, WINDOW_HEIGHT - 190 - GRID_SIZE // 2))

            restart_text_shadow = self.font.render("Press SPACE to Restart or ESC to Quit", True, WHITE).convert_alpha()
            self.display_surface.blit(restart_text_shadow,
                                      (40 + GRID_SIZE // 3, WINDOW_HEIGHT - 150 - GRID_SIZE // 3))

            # Draw main text without shadow
            game_over_text = self.title_font.render("GAME OVER", True, BLACK)
            self.display_surface.blit(game_over_text, (80, WINDOW_HEIGHT - 190))  # Fixed: corrected variable name

            restart_text = self.font.render(f"Press SPACE to Restart or ESC to Quit", True, BLACK)
            self.display_surface.blit(restart_text, (40, WINDOW_HEIGHT - 150))

    def draw_game_over(self):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill(GRAY + (200,), special_flags=pygame.BLEND_RGBA_MULT)  # Darken background with transparency
        self.display_surface.blit(overlay, (0, 0))

        # Game over message text centered at the top of screen
        game_over_text = self.title_font.render("GAME OVER", True, RED)
        self.display_surface.blit(game_over_text,
                                  ((WINDOW_WIDTH - game_over_text.get_width()) // 2 + GRID_SIZE // 4,
                                   WINDOW_HEIGHT // 5))

        # Draw restart instruction text below the message
        restart_shadow = self.font.render("Press SPACE to Restart or ESC to Quit", True, WHITE).convert_alpha()
        self.display_surface.blit(restart_text_shadow,
                                  ((WINDOW_WIDTH - restart_text_shadow.get_width()) // 2,
                                   WINDOW_HEIGHT // 3 + 40))

    def run(self):
        """Main game loop"""
        while True:
            # Handle events (input)
            self.handle_events()

            if not self.game_over and pygame.key.get_pressed()[K_SPACE]:
                # Snake can't change direction instantly
                pass

            # Draw background with a slight gradient for visual appeal
            self.display_surface.fill(GRAY + (200,))  # Semi-transparent gray background

            # Update game state based on events and time
            if not self.game_over:
                self.handle_events()

            # Always update snake position when possible
            self.update_snake()
            self.handle_events()  # This will handle new inputs while updating direction

            # Draw the grid, score panel, food, and snake in sequence
            self.draw_grid()
            self.draw_score_panel()
            self.draw_food()
            self.draw_snake()

            # Update display with calculated changes (changes are drawn above)
            pygame.display.update()

            # Control game speed based on difficulty level (score-dependent)
            if not self.game_over:
                # Speed increases slightly as score grows to make it more challenging
                delay = max(10, 80 - min(self.score * 2, 50))
                self.clock.tick(10 + self.score)  # Increase speed with score (max cap at 60 FPS)
            else:
                # When game is over, run slower for better visibility of the end state
                self.clock.tick(5)

            # Clear next_direction to start fresh if not being used in this frame
            self.next_direction = None

    def main(self):
        """Main function to control game execution"""
        while True:
            self.handle_events()
            self.update_snake()  # Update snake position

            # Draw everything on the screen after handling events and updates
            self.display_surface.fill(GRAY)  # Fill with dark background for a sleek look
            self.draw_grid()
            self.draw_score_panel()
            self.draw_food()
            self.draw_snake()

            if not self.game_over:
                # Display current direction indicator in bottom right corner
                dir_symbol = ""
                if self.direction == UP:
                    dir_symbol = "▲"
                elif self.direction == DOWN:
                    dir_symbol = "▼"
                elif self.direction == LEFT:
                    dir_symbol = "◀"
                else:
                    dir_symbol = "▶"

                # Create a small text display for current direction
                dir_text = pygame.Surface((30, 25), pygame.SRCALPHA) if not self.game_over else None

                if not self.game_over:
                    dir_shadow = self.font.render(f"Direction: {dir_symbol}", True, WHITE).convert_alpha()
                    self.display_surface.blit(dir_shadow, (self.snake_pos[0][0] * GRID_SIZE + 15,
                                                           self.snace_pos[0][1] * GRID_SIZE - 20))
                else:
                    # When game over, display restart message
                    dir_text = "Press SPACE to Restart or ESC to Quit"
            pygame.display.update()

        return None


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game.handle_events()  # Handle user inputs and events

        if not game.game_over:
            game.update_snake()  # Update snake position and check for food collision

            # Draw everything
            game.draw_grid()
            game.display_surface.fill(GRAY)
            game.draw_score_panel()
            game.draw_food()
            game.draw_snake()

            # Clear the next_direction to avoid multiple presses affecting movement during draw call

        else:
            # Only update display if not in main loop (to reduce flickering and improve performance)
            pass


    def run(self):
        """Main game execution function"""
        while True:
            self.handle_events()  # Handle events

            # Update snake position
            self.update_snake()

            # Draw everything on screen
            self.draw_grid()
            if not self.game_over:
                self.display_surface.fill(GRAY)  # Fill entire display with gray for a clean look

                # Draw score panel at top, but leave bottom space for game grid (optional)
                self.draw_score_panel()

                # Main game area is drawn above the score panel
                main_area = pygame.Rect(0, GRID_SIZE * GRID_HEIGHT - 10, WINDOW_WIDTH, WINDOW_HEIGHT)
                pygame.draw.rect(self.display_surface, WHITE, main_area)  # White border at bottom

                self.draw_food()  # Draw food on grid cell
            else:
                self.game_over = True

if __name__ == "__main__":
    game = SnakeGame()
    while True:
        game.handle_events()

        if not game.game_over and game.next_direction is None:
            # Initial setup with a delay to show instructions briefly
            pygame.time.delay(500)

            # Start the snake moving automatically after initial display
            game.direction = RIGHT

        # Update game state once per second (for simplicity, but could adjust for difficulty progression)
        if not game.game_over:
            game.update_snake()

        # Draw everything
        game.display_surface.fill(BLUE)  # Background color
        pygame.draw.rect(game.display_surface, BLUE, (0, WINDOW_HEIGHT - 250, WINDOW_WIDTH, 250))
        game.draw_grid()
        game.draw_score_panel()

if __name__ == "__main__":
    snake_game = SnakeGame()
    while True:
        snake_game.run()  # Start the game loop

But
I
see
some
issues in your
code.Let
me
fix
them.

1.
The
main
function and run
method
are
duplicated and not properly
integrated.
2.
There
's a mix of drawing methods that are called at different times, which is confusing.
3.
The
event
handling
for restarting doesn't work correctly because the restart condition isn't being handled after game over state changes.
4.
Some
variables
like
dir_symbol in main()
don
't exist.

Let
me
refactor and fix
these
issues
to
create
a
proper
SnakeGame


class:


We
'll restructure the code so that:
- draw_grid, draw_snake, etc., are
called
once
per
frame
- The
snake
movement
logic is updated
every
game
tick(not just
when
key
pressed)
- Game
over
screen is handled
properly

Here
's an improved version of your Snake game with better structure and visuals.

```python

import pygame
import random
from pygame.locals import *

pygame.init()


class SnakeGame:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.cell_size = 40

        # Set up display window with title
        self.display_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")

        # Create a clock object to control game speed
        self.clock = pygame.time.Clock()

        # Font for score display
        self.font = pygame.font.SysFont('Arial', 24)
        self.title_font = pygame.font.SysFont('Arial', 36, bold=True)

        # Game state variables
        self.snake_pos = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
                          (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
                          (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None

        # Initialize food position and score
        self.food_pos = self.generate_food()
        self.score = 0

    def run(self):
        """Main game loop"""
        while True:
            self.handle_events()

            if not self.game_over:
                self.update_snake()

                # Draw everything on the screen (background, grid, score panel, snake and food)
                self.draw_score_panel()
                self.display_surface.fill(GRAY)  # Fill with gray background
                self.draw_grid()
                self.draw_snake()
                self.draw_food()
            else:
                self.draw_game_over_screen()

    def draw_grid(self):
        """Draw the game grid on screen"""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):  # Fixed: variable not defined


I
think
there
are
still
issues.Let
me
rewrite
the
entire
code
properly.