class Scoreboard:
    def __init__(self):
        self.current_score = 0
    @property
    def current_score(self):
        return self._current_score
    @current_score.setter
    def current_score(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Score must be a positive integer.")
        self._current_score = value