## game.py

import pygame
from typing import List, Tuple

class Game:
    def __init__(self, width: int = 640, height: int = 480):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake = Snake(initial_length=3)
        self.food = Food()
        self.score = 0

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    self.snake.change_direction(event.key)

            self.snake.move()

            if self.check_food_collision():
                self.snake.grow()
                self.food.generate_new_position()
                self.update_score(self.score + 10)
                continue

            if self.snake.collide_with_self() or self.snake.is_out_of_bounds(self.screen.get_size()):
                self.handle_game_over()

            self.draw()

    def update_score(self, new_score: int) -> None:
        self.score = new_score

    def check_food_collision(self) -> bool:
        snake_head_position = self.snake.segments[0]
        return snake_head_position == self.food.position

    def handle_game_over(self) -> None:
        print("Game Over!")
        pygame.quit()
        exit()

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(10)

class Snake:
    def __init__(self, initial_length: int = 3):
        self.segments = [(20 * i, 20) for i in range(initial_length)]
        self.direction = (20, 0)

    def move(self) -> None:
        head_position = self.segments[0]
        new_head_position = (
            (head_position[0] + self.direction[0], head_position[1] + self.direction[1])
            if not self.collide_with_self()
            else head_position
        )
        self.segments.insert(0, new_head_position)
        self.segments.pop()

    def grow(self, new_segment: Tuple[int, int]) -> None:
        self.segments.append(new_segment)

    def collide_with_self(self) -> bool:
        return any(segment for segment in self.segments[1:] if segment == self.segments[0])

    def is_out_of_bounds(self, screen_size: Tuple[int, int]) -> bool:
        head_position = self.segments[0]
        return (
            head_position[0] < 0 or
            head_position[0] >= screen_size[0] or
            head_position[1] < 0 or
            head_position[1] >= screen_size[1]
        )

    def change_direction(self, key: int) -> None:
        if key == pygame.K_UP and self.direction != (0, 20):
            self.direction = (0, -20)
        elif key == pygame.K_DOWN and self.direction != (0, -20):
            self.direction = (0, 20)
        elif key == pygame.K_LEFT and self.direction != (20, 0):
            self.direction = (-20, 0)
        elif key == pygame.K_RIGHT and self.direction != (-20, 0):
            self.direction = (20, 0)

    def draw(self, screen: pygame.Surface) -> None:
        for segment in self.segments:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(segment[0], segment[1], 20, 20))

class Food:
    def __init__(self):
        self.position = (0, 0)

    def generate_new_position(self) -> None:
        while True:
            new_position = (20 * (pygame.randint(0, int(self.screen.get_width() / 20))), 20 * (pygame.randint(0, int(self.screen.get_height() / 20))))
            if not any(segment == new_position for segment in self.game.snake.segments):
                break
        self.position = new_position

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], 20, 20))
