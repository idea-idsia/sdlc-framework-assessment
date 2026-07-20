import pygame
import random
import sys

# NEW SECTION

pygame.init()

# NEW SECTION

black = (0, 0, 0)
white = (255, 255, 255)

# NEW SECTION

WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# NEW SECTION

win = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
def init(self):
self.snake_pos = [200, 200]
self.direction = 'RIGHT'
self.food_pos = self.generate_food()
self.length = 1
self.score = 0

def generate_food(self):
return [random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE]

def draw_grid(self):
for i in range(WIDTH // BLOCK_SIZE):
for j in range(HEIGHT // BLOCK_SIZE):
pygame.draw.rect(win, black, (i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_snake(self):
for x, y in self.snake_pos:
pygame.draw.rect(win, white, (x, y, BLOCK_SIZE, BLOCK_SIZE))

def draw_food(self):
pygame.draw.rect(win, (255, 0, 0), (*self.food_pos, BLOCK_SIZE, BLOCK_SIZE))

def move_snake(self):
if self.direction == 'RIGHT':
for i in range(len(self.snake_pos) - 1, 0, -1):
x, y = self.snake_pos[i]
self.snake_pos[i] = (x - BLOCK_SIZE, y)
elif self.direction == 'LEFT':
for i in range(len(self.snake_pos) - 1, 0, -1):
x, y = self.snake_pos[i]
self.snake_pos[i] = (x + BLOCK_SIZE, y)
elif self.direction == 'UP':
for i in range(len(self.snake_pos) - 1, 0, -1):
x, y = self.snake_pos[i]
self.snake_pos[i] = (x, y - BLOCK_SIZE)
elif self.direction == 'DOWN':
for i in range(len(self.snake_pos) - 1, 0, -1):
x, y = self.snake_pos[i]
self.snake_pos[i] = (x, y + BLOCK_SIZE)

def check_collision_boundaries(self):
if self.snake_pos[0][0] < 0 or self.snake_pos[0][0] >= WIDTH:
return True
elif self.snake_pos[0][1] < 0 or self.snake_pos[0][1] >= HEIGHT:
return True
else:
return False

def check_collision_body(self):
for x, y in self.snake_pos[:-1]:
if (x == self.snake_pos[-1][0]) and (y == self.snake_pos[-1][1]):
return True
return False

def check_collision_food(self):
if (self.food_pos[0] == self.snake_pos[-1][0]) and (self.food_pos[1] == self.snake_pos[-1][1]):
self.length += 1
self.score += 1
self.generate_food()
else:
return False
return True

def game_over(self):
win.fill(black)
font = pygame.font.Font(None, 100)
text = font.render("Game Over", True, white)
text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
win.blit(text, text_rect)
pygame.display.update()
time.sleep(1)
return False

def run(self):
clock = pygame.time.Clock()
running = True
while running:
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False
elif event.type == pygame.KEYDOWN:
if event.key == pygame.K_RIGHT and self.direction != 'LEFT':
self.direction = 'RIGHT'
elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
self.direction = 'LEFT'
elif event.key == pygame.K_UP and self.direction != 'DOWN':
self.direction = 'UP'
elif event.key == pygame.K_DOWN and self.direction != 'UP':
self.direction = 'DOWN'

win.fill(black)
self.draw_grid()
self.draw_snake()
self.draw_food()

if not self.check_collision_boundaries():
continue
if not self.check_collision_body():
continue

if self.food_pos == self.snake_pos[-1]:
running = self.game_over()

self.move_snake()
for x, y in self.snake_pos:
pygame.draw.rect(win, (0, 255, 0), (x, y, BLOCK_SIZE, BLOCK_SIZE))

font = pygame.font.Font(None, 20)
text = font.render(f'Score: {self.score}', True, white)
win.blit(text, (10, 10))
text = font.render(f'Length: {self.length}', True, white)
win.blit(text, (10, 30))

pygame.display.update()
clock.tick(SPEED)

pygame.quit()
sys.exit()
game = SnakeGame()
game.run()