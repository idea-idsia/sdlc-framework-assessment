'''
snake
'''
from collections import deque
import pygame
from constants import *
class Snake:
    """Snake class: manages snake body, movement, growth, and pixel‑based animation."""
    def __init__(self, init_pos=(5,5), init_length=3, init_dir=(1,0)):
        """
        Initialise the snake.
        :param init_pos: (x, y) starting position of the head (grid coordinates).
        :param init_length: initial number of segments.
        :param init_dir: initial movement direction (dx, dy).
        """
        self.body = deque([
            (init_pos[0] - i * init_dir[0], init_pos[1] - i * init_dir[1])
            for i in range(init_length)
        ])
        self.direction = init_dir
        self.grow_flag = False
        # Pixel based positions for smooth animation
        # Each element: {'pos': (x_px, y_px), 'target': (x_px, y_px)}
        start_px = (self.body[0][0] * CELL_SIZE, self.body[0][1] * CELL_SIZE)
        self.segments = [{'pos': start_px, 'target': start_px} for _ in self.body]
        # Animation speed (pixels per frame)
        self.step = CELL_SIZE / 10
    def set_direction(self, new_dir):
        """Update movement direction, but prevent reversing onto itself."""
        if (new_dir[0] == -self.direction[0] and new_dir[1] == -self.direction[1]):
            return
        self.direction = new_dir
    def move(self):
        """Advance the snake by one cell. If the snake has eaten food, it grows (head is added but tail is not removed)."""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.appendleft(new_head)
        # Update pixel targets for animation
        new_target_px = (new_head[0] * CELL_SIZE, new_head[1] * CELL_SIZE)
        self.segments.insert(0, {'pos': self.segments[0]['pos'], 'target': new_target_px})
        if not self.grow_flag:
            self.body.pop()
            self.segments.pop()
        else:
            self.grow_flag = False
    def grow(self):
        """Trigger a growth on the next move."""
        self.grow_flag = True
    def get_head(self):
        """Return the current head position (grid coordinates)."""
        return self.body[0]
    def collides_with_self(self):
        """Detect self‑collision."""
        return self.get_head() in list(self.body)[1:]
    def update_pixels(self):
        """Move each segment a little bit towards its target for smooth animation."""
        for seg in self.segments:
            px, py = seg['pos']
            tx, ty = seg['target']
            dx = tx - px
            dy = ty - py
            dist = (dx*dx + dy*dy) ** 0.5
            if dist < self.step:
                seg['pos'] = seg['target']
            else:
                seg['pos'] = (px + dx / dist * self.step, py + dy / dist * self.step)
        # If head has reached its target, shift targets for following segments
        if self.segments[0]['pos'] == self.segments[0]['target'] and len(self.segments) > 1:
            for i in range(len(self.segments)-1, 0, -1):
                self.segments[i]['target'] = self.segments[i-1]['target']
    def draw(self, surface):
        """Render the snake on the given surface."""
        for idx, seg in enumerate(self.segments):
            color = DARK_GREEN if idx == 0 else GREEN
            pos = seg['pos']
            rect = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)