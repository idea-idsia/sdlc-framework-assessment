'''
Main game class. Handles game logic, updates, and rendering.
'''
import pygame
from food import Food
from grid import Grid
from ui import UI
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(self.width, self.height)
        self.food = Food(self.width, self.height)
        self.grid = Grid(self.width, self.height)
        self.ui = UI(self.width, self.height)
        self.game_over = False
        self.score = 0
        self.clock = pygame.time.Clock()
    def update(self):
        """Updates the game state."""
        if not self.game_over:
            self.snake.move()
            if self.snake.body[0].colliderect(self.food.rect):
                self.snake.grow()
                self.food = Food(self.width, self.height)
                self.score += 1
            if self.snake.check_wall_collision() or self.snake.check_self_collision():
                self.game_over = True
    def render(self):
        """Renders the game elements on the screen."""
        self.screen.fill((0, 0, 0))  # Black background
        self.grid.draw(self.screen)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.ui.draw_score(self.screen, self.score)
        if self.game_over:
            self.ui.draw_game_over(self.screen, self.score)
        pygame.display.flip()
    def run(self):
        """Main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.direction != "right":
                        self.snake.change_direction("left")
                    if event.key == pygame.K_RIGHT and self.snake.direction != "left":
                        self.snake.change_direction("right")
                    if event.key == pygame.K_UP and self.snake.direction != "down":
                        self.snake.change_direction("up")
                    if event.key == pygame.K_DOWN and self.snake.direction != "up":
                        self.snake.change_direction("down")
            self.update()
            self.render()
            self.clock.tick(10) # Control the game speed