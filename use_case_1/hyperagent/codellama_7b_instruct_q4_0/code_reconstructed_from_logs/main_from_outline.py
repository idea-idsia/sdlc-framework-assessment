import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

board_width = 10
board_height = 10
board = [[False for _ in range(board_width)] for _ in range(board_height)]

snake_x = board_width // 2
snake_y = board_height // 2
direction = RIGHT

food_x = random.randrange(0, board_width)
food_y = random.randrange(0, board_height)

def draw_board():
    for y in range(board_height):
        for x in range(board_width):
            if board[y][x]:
                pygame.draw.rect(screen, (0, 255, 0), (x*10, y*10, 10, 10))
    pygame.display.update()

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, (0, 0, 255), (segment[0]*10, segment[1]*10, 10, 10))
    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = LEFT
            elif event.key == K_RIGHT:
                direction = RIGHT
            elif event.key == K_UP:
                direction = UP
            elif event.key == K_DOWN:
                direction = DOWN

def update():
    global snake_x, snake_y, direction
    if direction == LEFT:
        snake_x -= 10
    elif direction == RIGHT:
        snake_x += 10
    elif direction == UP:
        snake_y -= 10
    elif direction == DOWN:
        snake_y += 10
    if snake_x < 0 or snake_x >= board_width*10 or snake_y < 0 or snake_y >= board_height*10:
        sys.exit()
    if board[snake_y // 10][snake_x // 10]:
        sys.exit()

def handle_food():
    global snake, food_x, food_y
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, board_width)
        food_y = random.randrange(0, board_height)
        snake.append((snake[-1][0] + 10, snake[-1][1]))

def game_over():
    pygame.display.set_caption("Game Over!")
    text = font.render("Press any key to restart", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    handle_events()
    update()
    handle_food()
    draw_board()
    draw_snake()
    clock.tick(60)