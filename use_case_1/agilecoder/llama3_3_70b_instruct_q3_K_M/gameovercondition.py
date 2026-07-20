import pygame
import sys
'''
The GameOverCondition class handles the game over condition.
'''
class GameOverCondition:
    def __init__(self, snake, game_board, food, collision_handler):
        self.snake = snake
        self.game_board = game_board
        self.food = food
        self.collision_handler = collision_handler
    '''
    Checks for game over and displays a message.
    '''
    def check_game_over(self, screen):
        if not self.collision_handler.check_collisions():
            font = pygame.font.Font(None, 64)
            text = font.render('Game Over', True, (255, 0, 0))
            screen.fill((0, 0, 0))
            screen.blit(text, (self.game_board.screen_width // 2 - 150, self.game_board.screen_height // 2 - 50))
            font = pygame.font.Font(None, 36)
            text = font.render('Press Space to restart or Esc to quit', True, (255, 255, 255))
            screen.blit(text, (self.game_board.screen_width // 2 - 150, self.game_board.screen_height // 2 + 50))
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.snake.reset()
                            self.food.pos = self.food.generate_food(self.snake)
                            waiting = False
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()