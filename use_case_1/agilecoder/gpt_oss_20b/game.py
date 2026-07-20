'''
Main game engine that orchestrates the Snake game loop, rendering, and events.
'''
import pygame
import sys
from constants import *
from snake import Snake
from food import Food
class Game:
    """
    Core game class responsible for initializing Pygame, handling the game loop,
    rendering, and user interactions.
    """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.font = pygame.font.SysFont(None, 36)
        self.reset_game()
    def reset_game(self):
        """
        Reset all game state to start a new game.
        """
        self.snake = Snake(GRID_SIZE)
        self.food = Food(GRID_SIZE, self.snake)
        self.score = 0
        self.game_over = False
        pygame.time.set_timer(MOVE_EVENT, MOVE_DELAY)
    def run(self):
        """
        Main game loop. Handles events, updates, and rendering until exit.
        """
        while True:
            self.handle_events()
            if not self.game_over:
                self.update()
            self.render()
            self.clock.tick(FPS)
    def handle_events(self):
        """
        Process all Pygame events, including keyboard input and timers.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOVE_EVENT and not self.game_over:
                self.check_collisions_and_move()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction((1, 0))
                elif event.key == pygame.K_UP:
                    self.snake.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction((0, 1))
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
    def update(self):
        """
        Update game logic per frame (currently handled in events).
        """
        pass  # All updates are event-driven
    def check_collisions_and_move(self):
        """
        Check for collisions with walls, self, or food before moving,
        then move the snake and handle post-move effects.
        """
        head_x, head_y = self.snake.body[0]
        dx, dy = self.snake.direction
        new_head = (head_x + dx, head_y + dy)
        # Wall collision
        if not (0 <= new_head[0] < GRID_SIZE and 0 <= new_head[1] < GRID_SIZE):
            self.game_over = True
            pygame.time.set_timer(MOVE_EVENT, 0)
            return
        # Self collision (including tail cell)
        if new_head in self.snake.body:
            self.game_over = True
            pygame.time.set_timer(MOVE_EVENT, 0)
            return
        # Store old tail before moving
        old_tail = self.snake.body[-1]
        # Move snake
        self.snake.move()
        # Food collision
        if self.food.position is not None and self.snake.body[0] == self.food.position:
            # Grow correctly by re-adding the old tail position
            self.snake.body.append(old_tail)
            self.score += 1
            self.food.respawn()
    def render(self):
        """
        Draw the current game state to the screen.
        """
        self.screen.fill(COLOR_BG)
        self.draw_grid()
        self.draw_food()
        self.draw_snake()
        self.draw_score()
        if self.game_over:
            self.draw_game_over()
        pygame.display.flip()
    def draw_grid(self):
        """
        Draw the grid lines for visual guidance.
        """
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_TEXT, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_TEXT, (0, y), (SCREEN_WIDTH, y))
    def draw_snake(self):
        """
        Render the snake on the board.
        """
        for segment in self.snake.body:
            rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, COLOR_SNAKE, rect)
    def draw_food(self):
        """
        Render the food item on the board.
        """
        if self.food.position is None:
            return
        x, y = self.food.position
        center = (x * CELL_SIZE + CELL_SIZE//2, y * CELL_SIZE + CELL_SIZE//2)
        radius = CELL_SIZE // 2 - 4
        pygame.draw.circle(self.screen, COLOR_FOOD, center, radius)
    def draw_score(self):
        """
        Display the current score at the top-left corner.
        """
        score_surf = self.font.render(f'Score: {self.score}', True, COLOR_TEXT)
        self.screen.blit(score_surf, (10, 10))
    def draw_game_over(self):
        """
        Display game over message and restart instruction, ensuring score
        remains visible above the semi-transparent overlay.
        """
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        # Score displayed on top of overlay
        score_surf = self.font.render(f'Score: {self.score}', True, COLOR_TEXT)
        score_rect = score_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30))
        self.screen.blit(score_surf, score_rect)
        # Game over message
        msg = self.font.render('Game Over! Press R to Restart', True, COLOR_TEXT)
        msg_rect = msg.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
        self.screen.blit(msg, msg_rect)