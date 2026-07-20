'''
Main entry point for the Snake game. Initializes the game components and runs the game loop.
Handles user input and updates game state accordingly.
'''
import pygame
from constants import GRID_SIZE, COLORS
from sound import Sound
from ui import UserInterface
from board import Board
from snake import Snake
def main():
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    game_speed = 10
    font = pygame.font.Font(None, 36)
    snake = Snake(GRID_SIZE)
    sound = Sound()
    ui = UserInterface(screen, width, height)
    board = Board(width, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.change_direction((1, 0))
        screen.fill(COLORS['BLACK'])
        # Game logic
        if not snake.move():
            sound.play_game_over_sound()
            ui.game_over_screen()
            running = False
        board.draw(screen)
        snake.draw(screen)
        # Display score and other UI elements
        ui.display_score(snake.length - 1) 
        pygame.display.flip()
        clock.tick(game_speed)
    pygame.quit()
if __name__ == "__main__":
    main()