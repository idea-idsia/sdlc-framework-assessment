from game import Game

def main():
    """Start a new game with two players."""
    game = Game()
    player1 = "Player 1"
    player2 = "Player 2"
    game.start_game(player1, player2)
    while not game.is_finished():
        move = input("Enter a move: ")
        try:
            game.make_move(move)
        except ValueError as e:
            print(f"Invalid move: {e}")
    winner = game.get_winner()
    if winner is None:
        print("Game is a draw.")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()
