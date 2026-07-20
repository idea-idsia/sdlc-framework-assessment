from game import Game

def main():
    # Initialize the game with a difficulty level of 1
    game = Game(difficulty_level=1)
    
    # Play the game and get the score
    score = game.play()
    
    # Print the score
    print(f"Score: {score}")
