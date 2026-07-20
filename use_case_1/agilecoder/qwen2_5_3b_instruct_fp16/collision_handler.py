'''
Collision handling module.
Detects collisions between the snake's head, boundaries, and body.
'''
from typing import List, Tuple
def handle_collision(snake: si.Snake) -> bool:
    """Check for any collision."""
    if any([pos[0] < 0 or pos[0] >= GRID_SIZE or pos[1] < 0 or pos[1] >= GRID_SIZE for pos in snake.body]):
        return True
    elif (snake.body[0][0], snake.body[0][1]) in snake.body[:-1]:
        return True
    return False
def display_collision(snake: si.Snake) -> None:
    """Display collision messages."""
    if handle_collision(snake):
        print("Game Over")