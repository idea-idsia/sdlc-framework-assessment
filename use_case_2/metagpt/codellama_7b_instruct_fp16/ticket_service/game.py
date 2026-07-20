class Game:
    def __init__(self):
        self.game_state = None
        self.player_turn = None
        self.board = None
        self.player1 = None
        self.player2 = None
        self.winner = None

    def start_game(self, player1, player2):
        """Start a new game with two players."""
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.game_state = GameState.PLAYING
        self.player_turn = player1

    def make_move(self, move):
        """Make a move on the board."""
        if not self.is_valid_move(move):
            raise ValueError("Invalid move")
        self.board.make_move(move)
        self.player_turn = self.player1 if self.player_turn == self.player2 else self.player2

    def is_valid_move(self, move):
        """Check if a move is valid."""
        return self.board.is_valid_move(move) and self.game_state == GameState.PLAYING

    def get_winner(self):
        """Get the winner of the game."""
        if self.game_state != GameState.FINISHED:
            return None
        return self.player1 if self.winner == 1 else self.player2

    def is_finished(self):
        """Check if the game is finished."""
        return self.game_state == GameState.FINISHED
