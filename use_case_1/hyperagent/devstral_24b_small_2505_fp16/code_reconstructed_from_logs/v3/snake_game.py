import random

class SnakeGame:
  def __init__(self, width=10, height=10):
      self.width = width
      self.height = height
      self.grid = [[' ' for _ in range(width)] for _ in range(height)]
      self.snake = [(height // 2, width // 2)]
      self.direction = (0, 1)  # Starting direction: right

  def display_grid(self):
      for row in self.grid:
          print(' '.join(row))
      print()

  def main_loop(self):
      while True:
          # Game loop logic here
          pass

if __name__ == "__main__":
  game = SnakeGame()
  game.display_grid()
  game.main_loop()