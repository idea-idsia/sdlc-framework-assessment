class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen):
        cell_size = 80
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)