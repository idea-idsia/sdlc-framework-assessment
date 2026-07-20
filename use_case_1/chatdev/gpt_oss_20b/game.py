'''
game
'''
import pygame
from pygame.locals import *
from constants import *
from snake import Snake
from food import Food
class Game:
    """Game class: main game loop, rendering, input handling, and animations."""
    def __init__(self):
        """Initialise pygame, screen, clock and fonts."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.reset()
    def reset(self):
        """Reset all game state for a new run."""
        self.snake = Snake(init_pos=(GRID_WIDTH // 4, GRID_HEIGHT // 2),
                           init_length=3, init_dir=(1, 0))
        self.food = Food(self.snake)
        self.score = 0
        self.game_over = False
        self.move_delay = 150  # milliseconds per move
        self.last_move_time = pygame.time.get_ticks()
        self.game_over_timer = 0  # For flashing effect
    def handle_input(self):
        """Process user input (arrow keys & restart)."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.snake.set_direction((0, -1))
                elif event.key == K_DOWN:
                    self.snake.set_direction((0, 1))
                elif event.key == K_LEFT:
                    self.snake.set_direction((-1, 0))
                elif event.key == K_RIGHT:
                    self.snake.set_direction((1, 0))
                elif event.key == K_r and self.game_over:
                    self.reset()
    def update(self):
        """Update game logic: movement, collision detection, scoring."""
        if self.game_over:
            return
        now = pygame.time.get_ticks()
        if now - self.last_move_time >= self.move_delay:
            self.snake.move()
            self.last_move_time = now
            # Collision with walls
            head_x, head_y = self.snake.get_head()
            if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
                self.game_over = True
                return
            # Collision with self
            if self.snake.collides_with_self():
                self.game_over = True
                return
            # Collision with food
            if self.snake.get_head() == self.food.position:
                self.score += 1
                self.snake.grow()
                self.food.effect_timer = 15  # Show effect next frame
                self.food.generate(self.snake)
        # Smooth animation step
        self.snake.update_pixels()
    def draw(self):
        """Render everything on the screen."""
        self.screen.fill(WHITE)
        # Draw grid lines
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
        # Draw snake and food
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        # Draw score
        score_surf = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_surf, (10, 10))
        # Add instructions (only when not game over)
        if not self.game_over:
            instr_surf = self.font.render(
                "Use arrow keys to move. Press R to restart after Game Over.",
                True, BLACK)
            self.screen.blit(instr_surf, (10, 40))
        # Game over overlay with flash effect
        if self.game_over:
            self.game_over_timer += 1
            if self.game_over_timer % 20 < 10:  # Flash every 20 frames
                over_surf = self.font.render("Game Over! Press R to Restart", True, RED)
                over_rect = over_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                self.screen.blit(over_surf, over_rect)
        pygame.display.flip()
    def run(self):
        """Main loop."""
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)