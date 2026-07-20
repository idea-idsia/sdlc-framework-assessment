import random

class Food:
    def __init__(self, game_board):
        self.position = self.generate(game_board, None)

    def generate(self, game_board, snake):
        while True:
            x = random.randint(0, game_board.width - 1)
            y = random.randint(0, game_board.height - 1)
            if (x, y) not in [snake.body] if snake else []:
                self.position = (x, y)
                break

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0] * 80, self.position[1] * 80, 80, 80))