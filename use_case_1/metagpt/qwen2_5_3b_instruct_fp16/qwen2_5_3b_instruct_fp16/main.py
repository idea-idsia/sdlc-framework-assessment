import numpy as np
from pygame.locals import *
from game_board import GameBoard
from snake import Snake
from food import Food
from collision_handler import CollisionHandler
from score_display import ScoreDisplay

class Main:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.game_board = GameBoard(self.width, self.height)
        self.snake = Snake((400, 300), 'right')
        self.food = Food(self.game_board)
        self.collision_handler = CollisionHandler()
        self.score_display = ScoreDisplay()

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False

            keys = pygame.key.get_pressed()
            self.snake.move(keys)

            # Check collision
            is_collision = self.collision_handler.check_collision(self.snake, self.food.position, self.game_board)
            if is_collision:
                self.snake.grow()
                self.food.generate_food(self.game_board)
            
            # Update game board
            grid = np.full((self.height // 20, self.width // 20), ' ')
            for row in range(15):
                for col in range(40):
                    if (col * 20 + 10, row * 20) == self.snake.position:
                        grid[row][col] = 'S'
                    elif (col * 20 + 10, row * 20) == self.food.position:
                        grid[row][col] = 'F'
            self.game_board.update_grid(grid)

            # Display score
            self.score_display.display_score()

            pygame.display.flip()
            clock.tick(10)
        
        pygame.quit()

if __name__ == "__main__":
    main_game = Main()
    main_game.run_game()
