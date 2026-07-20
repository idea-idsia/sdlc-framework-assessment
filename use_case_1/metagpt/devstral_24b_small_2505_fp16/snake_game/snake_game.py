import pygame
import random
from typing import List, Tuple

class Snake:
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    def __init__(self):
        self.body: List[Tuple[int, int]] = [(100, 100), (90, 100), (80, 100)]
        self.direction: str = Snake.RIGHT

    def move(self) -> None:
        head_x, head_y = self.body[0]
        if self.direction == Snake.UP:
            new_head = (head_x, head_y - 10)
        elif self.direction == Snake.DOWN:
            new_head = (head_x, head_y + 10)
        elif self.direction == Snake.LEFT:
            new_head = (head_x - 10, head_y)
        elif self.direction == Snake.RIGHT:
            new_head = (head_x + 10, head_y)

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self) -> None:
        self.body.append(self.body[-1])

    def check_collision(self, screen_width: int = 800, screen_height: int = 600) -> bool:
        # Check collision with itself
        if self.body[0] in self.body[1:]:
            return True

        # Check collision with walls (using passed parameters)
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= screen_width or head_y < 0 or head_y >= screen_height:
            return True

        return False

class Food:
    def __init__(self):
        self.position: Tuple[int, int] = (0, 0)
        self.generate_random_position()

    def generate_random_position(self, grid_width: int = 80, grid_height: int = 60, snake_body: List[Tuple[int, int]] = []) -> None:
        while True:
            position = (random.randint(0, grid_width - 1) * 10, random.randint(0, grid_height - 1) * 10)
            if position not in snake_body:
                self.position = position
                break

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()
        self.score: int = 0

    def run(self) -> None:
        running = True
        while running:
            self.handle_events()
            if not self.update():
                running = False
            self.draw()

        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != Snake.DOWN:
                    self.snake.direction = Snake.UP
                elif event.key == pygame.K_DOWN and self.snake.direction != Snake.UP:
                    self.snake.direction = Snake.DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != Snake.RIGHT:
                    self.snake.direction = Snake.LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != Snake.LEFT:
                    self.snake.direction = Snake.RIGHT

    def update(self) -> bool:
        self.snake.move()

        # Check if snake eats food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            grid_width = self.screen.get_width() // 10
            grid_height = self.screen.get_height() // 10
            self.food.generate_random_position(grid_width, grid_height, self.snake.body)
            self.score += 1

        return not self.snake.check_collision(self.screen.get_width(), self.screen.get_height())

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))

        # Draw snake
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))

        # Draw food
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], 10, 10))

        # Draw score
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()
        self.clock.tick(15)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
