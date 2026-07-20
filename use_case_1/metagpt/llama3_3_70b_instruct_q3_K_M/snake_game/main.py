import pygame
import random
import sys

# Initialize Pygame
pygame.init()

class Board:
    def __init__(self, width=800, height=600, grid_size=20):
        self.width = width
        self.height = height
        self.grid_size = grid_size

    def draw_grid(self, screen):
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, self.height))
        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(screen, (200, 200, 200), (0, y), (self.width, y))


class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'

    def move(self):
        head = self.body[-1]
        if self.direction == 'RIGHT':
            new_head = (head[0] + 20, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0] - 20, head[1])
        elif self.direction == 'UP':
            new_head = (head[0], head[1] - 20)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + 20)
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        last_segment = self.body[-1]
        if self.direction == 'RIGHT':
            new_segment = (last_segment[0] - 20, last_segment[1])
        elif self.direction == 'LEFT':
            new_segment = (last_segment[0] + 20, last_segment[1])
        elif self.direction == 'UP':
            new_segment = (last_segment[0], last_segment[1] + 20)
        elif self.direction == 'DOWN':
            new_segment = (last_segment[0], last_segment[1] - 20)
        self.body.insert(0, new_segment)

    def check_collision(self, board):
        head = self.body[-1]
        if (head[0] < 0 or head[0] >= board.width or
                head[1] < 0 or head[1] >= board.height):
            return True
        for segment in self.body[:-1]:
            if segment == head:
                return True
        return False


class Food:
    def __init__(self, x=400, y=300):
        self.x = x
        self.y = y

    def generate_new_food(self, board, snake):
        possible_positions = [(x, y) for x in range(0, board.width, 20) 
                             for y in range(0, board.height, 20)]
        valid_positions = [pos for pos in possible_positions if pos not in snake.body]
        if not valid_positions:
            raise Exception("No empty spaces on the board. Game Over.")
        self.x, self.y = random.choice(valid_positions)


class Game:
    def __init__(self):
        self.board = Board()
        self.snake = Snake()
        self.food = Food()
        self.screen = pygame.display.set_mode((self.board.width, self.board.height))
        self.clock = pygame.time.Clock()
        self.score = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                        self.snake.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                        self.snake.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                        self.snake.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                        self.snake.direction = 'RIGHT'

            self.snake.move()
            if self.snake.check_collision(self.board):
                print("Game Over. Final Score:", self.score)
                break

            if (self.snake.body[-1][0] == self.food.x and 
                    self.snake.body[-1][1] == self.food.y):
                self.snake.grow()
                self.food.generate_new_food(self.board, self.snake)
                self.score += 1

            self.screen.fill((0, 0, 0))
            self.board.draw_grid(self.screen)
            for pos in self.snake.body:
                pygame.draw.rect(self.screen, (0, 255, 0), (pos[0], pos[1], 20, 20))
            pygame.draw.rect(self.screen, (255, 0, 0), (self.food.x, self.food.y, 20, 20))
            font = pygame.font.Font(None, 36)
            text = font.render("Score: " + str(self.score), True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
            pygame.display.update()
            self.clock.tick(10)


if __name__ == "__main__":
    game = Game()
    game.run()

