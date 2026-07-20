class GameBoard:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(self.width // 20)] for _ in range(self.height // 20)]
    
    def display(self) -> str:
        return '\n'.join([''.join(row) for row in self.grid])
    
    def update_grid(self, grid: list[list[str]]):
        self.grid = [row[:] for row in grid]
