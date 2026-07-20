class Scoreboard:
    def __init__(self, screen):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.screen = screen
    def draw_score(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        rect = text.get_rect()
        rect.topleft = (10, 10)
        screen.blit(text, rect)
    def increment_score(self):
        self.score += 1