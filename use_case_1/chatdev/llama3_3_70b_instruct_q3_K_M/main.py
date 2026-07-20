import pygame
import sys
from snake import Snake
from food import Food
from game_board import GameBoard
'''
The main function initializes Pygame, sets up the game window, and starts the game loop.
'''
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake Game')
    snake = Snake(screen)
    food = Food(screen)
    game_board = GameBoard(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        snake.handle_events()  
        snake.move(food)
        food.generate_new_food(snake.body)
        game_board.draw_grid()
        snake.check_collisions(food, game_board)
        screen.fill((0, 0, 0))
        snake.draw_snake()
        food.draw_food()
        game_board.draw_boundaries()
        snake.display_score()
        pygame.display.flip()
        clock.tick(10)
if __name__ == "__main__":
    main()