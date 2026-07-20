class KeyHandler:
    def __init__(self, controller: GameController):
        self.controller = controller
    def handle_input(self):
        # Handle key inputs (arrow keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.controller.direction != 'RIGHT':
                    self.controller.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.controller.direction != 'LEFT':
                    self.controller.direction = 'RIGHT'
                elif event.key == pygame.K_UP and self.controller.direction != 'DOWN':
                    self.controller.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.controller.direction != 'UP':
                    self.controller.direction = 'DOWN'
        return True