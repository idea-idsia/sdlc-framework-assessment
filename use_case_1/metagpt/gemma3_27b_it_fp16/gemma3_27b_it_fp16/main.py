## main.py
import pygame
from snake import Snake
from food import Food
from game_board import GameBoard

class Main:
    """
    Represents the main game class.
    """

    def __init__(self, width: int = 20, height: int = 20, block_size: int = 20, game_speed: int = 10, start_position: tuple = None):
        """
        Initializes the main game.

        Args:
            width (int, optional): The width of the game board in blocks. Defaults to 20.
            height (int, optional): The height of the game board in blocks. Defaults to 20.
            block_size (int, optional): The size of each block in pixels. Defaults to 20.
            game_speed (int, optional): The game speed (frames per second). Defaults to 10.
            start_position (tuple, optional): The starting position of the snake. Defaults to the center.
        """
        self.width = width
        self.height = height
        self.block_size = block_size
        self.game_speed = game_speed
        self.game_board = GameBoard(self.width, self.height, self.block_size)
        if start_position is None:
            self.snake = Snake(start_position=(self.width // 2, self.height // 2), color=(0, 255, 0))
        else:
            self.snake = Snake(start_position=start_position, color=(0, 255, 0))
        self.food = Food(self.width, self.height, color=(255, 0, 0))
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        """
        Runs the main game loop.
        """
        pygame.init()
        screen = pygame.display.set_mode((self.width * self.block_size, self.height * self.block_size))
        pygame.display.set_caption("Snake Game")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = (1, 0)
                    elif event.key == pygame.K_UP:
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = (0, 1)

            # Check for self-collision BEFORE moving the snake
            head_x, head_y = self.snake.get_head_position()
            for i in range(len(self.snake.body)):
                if (head_x, head_y) == self.snake.body[i]:
                    self.running = False
                    print("Game Over! Hit self")
                    break
            if not self.running:
                break

            self.snake.move()

            if self.snake.check_collision(self.width, self.height):
                self.running = False
                print("Game Over! Hit wall")
                break

            head_x, head_y = self.snake.get_head_position()
            food_x, food_y = self.food.get_position()

            if (head_x, head_y) == (food_x, food_y):
                self.snake.grow()
                self.food.generate(self.width, self.height)

            screen.fill((0, 0, 0))  # Clear the screen
            self.game_board.draw(screen)
            self.snake.draw(screen, self.block_size)
            self.food.draw(screen, self.block_size)
            pygame.display.flip()
            self.clock.tick(self.game_speed)

        pygame.quit()

if __name__ == "__main__":
    game = Main(start_position=(5, 5))  # Example: Start snake at (5, 5)
    game.run()
