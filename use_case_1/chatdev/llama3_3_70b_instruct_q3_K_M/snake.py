import pygame
import sys
class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'right'
        self.score = 0
        self.should_grow = False
    def move(self, food):
        if self.direction == 'right':
            new_head = (self.body[-1][0] + 20, self.body[-1][1])
        elif self.direction == 'left':
            new_head = (self.body[-1][0] - 20, self.body[-1][1])
        elif self.direction == 'up':
            new_head = (self.body[-1][0], self.body[-1][1] - 20)
        elif self.direction == 'down':
            new_head = (self.body[-1][0], self.body[-1][1] + 20)
        self.body.append(new_head)
        if not self.should_grow and len(self.body) > self.score + 3:
            self.body.pop(0)
        self.should_grow = False
    def check_collisions(self, food, game_board):
        head = self.body[-1]
        if (head[0] < 0 or head[0] >= 800 or 
            head[1] < 0 or head[1] >= 600):
            self.game_over()
            # restart the game
            self.body = [(200, 200), (220, 200), (240, 200)]
            self.direction = 'right'
            self.score = 0
        for part in self.body[:-1]:
            if part == head:
                self.game_over()
                # restart the game
                self.body = [(200, 200), (220, 200), (240, 200)]
                self.direction = 'right'
                self.score = 0
        if food.food_position == head:
            self.score += 1
            self.should_grow = True
    def update_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
    def draw_snake(self):
        for pos in self.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (pos[0], pos[1], 20, 20))
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'down':
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN and self.direction != 'up':
                    self.direction = 'down'
                elif event.key == pygame.K_LEFT and self.direction != 'right':
                    self.direction = 'left'
                elif event.key == pygame.K_RIGHT and self.direction != 'left':
                    self.direction = 'right'
    def display_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
    def game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render('Game Over', True, (255, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(text, (300, 250))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Final Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(text, (350, 350))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False