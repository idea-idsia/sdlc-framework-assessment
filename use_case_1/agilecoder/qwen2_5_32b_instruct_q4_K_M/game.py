'''
This script runs a basic version of the Snake game with core functionalities such as snake movement,
collision detection, food generation, and score tracking. It also includes restart functionality after
game over to enhance user experience.
The UI has been improved for better clarity and consistency, including initial automatic snake movement.
Additionally, it addresses edge cases in collision detection for robust gameplay.
'''
import pygame
import random
from snake import Snake  # Import the Snake class from snake.py
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(400, 300)  # Use the imported Snake class
        self.food_pos = None
        self.score = 0
        self.game_over = False
        self.place_food()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif not self.game_over and event.type == pygame.KEYDOWN:
                    # Handle direction change based on key input.
                    self.handle_key_input(event)
            if not self.game_over:
                # Ensure continuous movement.
                self.snake.move(self.food_pos)
                self.game_over = self.check_collisions()
            else:
                if pygame.key.get_pressed()[pygame.K_r]:
                    running, game_over = self.restart_game()
                elif pygame.key.get_pressed()[pygame.K_q]:
                    running = False
            # Redraw everything.
            self.screen.fill(BLACK)
            self.snake.draw(self.screen, WHITE)  # Pass the color here
            if not self.game_over:
                pygame.draw.rect(self.screen, RED, [self.food_pos[0], self.food_pos[1], 10, 10])
                font = pygame.font.SysFont('Arial', 32)
                text_surface = font.render(f'Score: {self.score}', True, WHITE)
                self.screen.blit(text_surface, dest=(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 50))
            else:
                self.draw_game_over_message()
            pygame.display.flip()
            self.clock.tick(10) # Limit to 10 frames per second
    def handle_key_input(self, event):
        if event.key == pygame.K_UP and not (self.snake.direction == 'DOWN'):
            self.snake.change_direction('UP')
        elif event.key == pygame.K_DOWN and not (self.snake.direction == 'UP'):
            self.snake.change_direction('DOWN')
        elif event.key == pygame.K_LEFT and not (self.snake.direction == 'RIGHT'):
            self.snake.change_direction('LEFT')
        elif event.key == pygame.K_RIGHT and not (self.snake.direction == 'LEFT'):
            self.snake.change_direction('RIGHT')
    def place_food(self):
        while True:
            x, y = random.randint(0, SCREEN_WIDTH // 10 - 1) * 10, random.randint(0, SCREEN_HEIGHT // 10 - 1) * 10
            if (x, y) not in self.snake.positions:
                break
        self.food_pos = (x, y)
    def check_collisions(self):
        head_x, head_y = self.snake.get_head_position()
        # Check for food collision and grow snake
        if (head_x, head_y) == self.food_pos:
            self.score += 1
            self.place_food()
            self.snake.grow()
        # Check boundaries
        if (
                head_x < 0 or head_x >= SCREEN_WIDTH or 
                head_y < 0 or head_y >= SCREEN_HEIGHT
        ):
            return True
        # Check for collision with itself
        if [head_x, head_y] in self.snake.positions[1:]:
            return True
        return False
    def draw_game_over_message(self):
        font = pygame.font.SysFont('Arial', 32)
        text_surface = font.render(f'Game Over! Score: {self.score}', True, WHITE)
        self.screen.blit(text_surface, dest=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    def restart_game(self):
        self.snake.reset_snake()
        self.food_pos = None
        self.place_food()
        self.score = 0
        self.game_over = False