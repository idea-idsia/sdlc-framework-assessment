'''
Main entry point for the Snake Game.
Initializes and starts the game loop.
'''
import pygame
from snake import Snake
from food import Food
from grid import Grid
from utils import draw_text, handle_animations
from colors import WHITE, BLACK, GREEN, RED  # Import colors from new module
# Initialize Pygame
pygame.init()
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
def main():
    clock = pygame.time.Clock()
    while True:  # Add an outer loop to handle restarts
        game_over = False
        snake = Snake(grid)
        food = Food(grid, snake)
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Allow restart with 'R' key
                        game_over = True
                    else:
                        snake.change_direction(event.key)
            snake.move(food)
            if snake.check_collision():
                draw_game_over(screen, "Game Over! Press R to Restart")
                pygame.display.flip()
                wait_for_restart()  # Wait for 'R' key press to restart
                game_over = True
            if snake.eat_food(food):
                food.spawn()
                snake.score += 1
            screen.fill(BLACK)
            grid.draw_grid(screen, CELL_SIZE)
            snake.draw(screen, CELL_SIZE)
            food.draw(screen, CELL_SIZE)
            draw_text(screen, f'Score: {snake.score}', WHITE, 20, 10, 10)
            handle_animations(screen, CELL_SIZE, snake, food)
            pygame.display.flip()
            clock.tick(15)
def draw_game_over(screen, message):
    draw_text(screen, message, RED, 48, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 2 - 30)
def wait_for_restart():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False
if __name__ == '__main__':
    grid = Grid(SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
    main()