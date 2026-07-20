import pygame
from game_board import GameBoard
from snake import Snake
from food import Food

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    game_board = GameBoard(width=10, height=10)
    snake = Snake(initial_length=3, starting_position=(5, 5), direction='RIGHT')
    food = Food(game_board)

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        game_board.draw(screen)
        snake.update(game_board, food)
        food.draw(screen)

        if snake.is_collision():
            running = False

        score += 1
        utils.display_score(screen, score)

        pygame.display.flip()
        clock.tick(10)

    utils.game_over_screen(screen, score)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()