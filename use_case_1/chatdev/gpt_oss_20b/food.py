'''
food
'''
import random
import pygame
from constants import *
class Food:
    """Food class: generate random food not on snake."""
    def __init__(self, snake):
        """Create a new food object. The initial position is generated relative to the current snake."""
        self.position = None
        self.generate(snake)
        self.effect_timer = 0  # Timer for consumption visual effect
    def generate(self, snake):
        """Place food at a random free cell."""
        occupied = set(snake.body)
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in occupied:
                self.position = (x, y)
                break
    def draw(self, surface):
        """Render the food on the given surface."""
        x, y = self.position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)
        # Simple consumption effect: a fading circle that expands then disappears
        if self.effect_timer > 0:
            alpha = int(255 * self.effect_timer / 15)
            radius = CELL_SIZE * self.effect_timer / 15 * 1.5
            # Create a per‑pixel‑alpha surface for the effect
            effect_surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(
                effect_surf,
                (255, 0, 0, alpha),                # RGBA – the alpha is only for this surface
                (CELL_SIZE // 2, CELL_SIZE // 2),  # centre
                int(radius)
            )
            surface.blit(effect_surf, (x * CELL_SIZE, y * CELL_SIZE))
            self.effect_timer -= 1