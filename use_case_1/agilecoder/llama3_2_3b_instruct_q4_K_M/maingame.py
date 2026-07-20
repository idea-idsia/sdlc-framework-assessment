'''
Manages the game state and updates the display.
'''
import pygame
class MainGame:
    def __init__(self):
        self.board = Board(10, 10)
        self.snake = Snake(0, 0, 10, board=self.board)
        pygame.init()
        screen = pygame.display.set_mode((400, 400))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.snake.move(player_input.handle_key_down(event.key))
            screen.fill((255, 255, 255))
            self.board.draw(screen)
            self.snake.draw(screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
game = MainGame()