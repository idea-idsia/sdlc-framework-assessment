import random
from typing import List
class Segment:
    def __init__(self, position: tuple):
        self.position = position
        self.direction = "RIGHT"
    def turn_left(self) -> str:
        if self.direction == "LEFT":
            return "UP"  # Snake turns around to go up from the right
        elif self.direction == "UP":
            return "RIGHT"
        elif self.direction == "DOWN":
            return "LEFT"
        else:  # LEFT
            return "DOWN"
    def turn_right(self) -> str:
        if self.direction == "RIGHT":
            return "UP"
        elif self.direction == "UP":
            return "LEFT"
        elif self.direction == "DOWN":
            return "RIGHT"
        else:  # DOWN
            return "LEFT"
class Snake:
    def __init__(self, game_board: 'GameBoard'):
        self.segments = [Segment((0, 0)), Segment((1, 0)), Segment((2, 0))]
        self.game_board = game_board
        self.direction = "RIGHT"
    def move(self):
        head_position = self.segments[0].position
        if self.direction == "LEFT":
            new_head = (head_position[0] - 1, head_position[1])
        elif self.direction == "RIGHT":
            new_head = (head_position[0] + 1, head_position[1])
        elif self.direction == "UP":
            new_head = (head_position[0], head_position[1] - 1)
        else:  # DOWN
            new_head = (head_position[0], head_position[1] + 1)
        self.segments.insert(0, Segment(new_head))
        del self.segments[-1]
    def set_direction(self, direction):
        if direction == "LEFT":
            self.direction = "LEFT"
        elif direction == "RIGHT":
            self.direction = "RIGHT"
        elif direction == "UP":
            self.direction = "UP"
        else:  # DOWN
            self.direction = "DOWN"
class Food:
    def __init__(self, game_board: 'GameBoard'):
        self.position = None
        self.game_board = game_board
    def generate(self) -> tuple:
        possible_positions = [(x, y) for x in range(game_board.grid_size) 
                              for y in range(game_board.grid_size)]
        while True:
            position = random.choice(possible_positions)
            if position not in [segment.position for segment in self.game_board.snake.segments]:
                self.position = position
                return self.position
class Scoreboard:
    def __init__(self, screen):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.screen = screen
    def draw_score(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        rect = text.get_rect()
        rect.topleft = (10, 10)
        screen.blit(text, rect)
class GameBoard:
    def __init__(self, grid_size: int):
        self.grid_size = grid_size
        self.board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    def display(self, screen):
        # Display the board on the screen using ASCII characters
        for row in self.board:
            print(' '.join(row), file=screen)