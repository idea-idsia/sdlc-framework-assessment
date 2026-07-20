import pygame
import sys
'''
This class handles the game over condition.
'''
class GameOverCondition:
    def __init__(self, snake, game_board, food, collision_handler):
        self.snake = snake
        self.game_board = game_board
        self.food = food
        self.collision_handler = collision_handler
    '''
    Checks for game over.
    '''
    def check_game_over(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(text, (self.game_board.screen_width // 2 - 75, self.game_board.screen_height // 2 - 18))
        font = pygame.font.Font(None, 36)
        text = font.render('Press Space to restart or Esc to quit', True, (255, 255, 255))
        screen.blit(text, (self.game_board.screen_width // 2 - 150, self.game_board.screen_height // 2 + 18))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.snake.body = [(200, 200), (220, 200), (240, 200)]
                        self.snake.length = 3
                        self.food.pos = self.food.generate_new_food()
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()  