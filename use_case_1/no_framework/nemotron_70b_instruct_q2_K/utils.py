def display_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_over_screen(screen, score):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 48)
    text = font.render(f'Game Over! Score: {score}', True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)